**Scripts used to reproduced results represented in `Integrated single-nucleus and spatial transcriptomics captures transitional states in soybean nodule maturation`**

## Requirments
  1. Data Required
      - Genome file
        - Soybean (a2.v1)
        - Arabidopsis (v11)
      - Raw data
        10x and stereo-seq data can be downloaded at [CNCB data base](https://ngdc.cncb.ac.cn/bioproject/browse/PRJCA009893)
  2. Softwares Required
      - CellRanger (Used for processing 10x raw data)
      - SAW (Used for processing stereo-seq raw data)
      - scanpy  (Used for downstream analysis of 10X data)
      - Seurat (Used for downstream analysis of 10X data)
      - scDblFinder (Used for removing putative doublets)
      - scvi-tools (Used to implement 10X data integration)
      - scanorama (Used to implement 10X data integration)
      - harmonypy (Used to implement 10X data integration)
      - stereopy (Used for downstream analysis of stereoseq data)
      - Sctransform (Used for normalization of stereopy data)
      - muon (Used for normalization of stereopy data)
      - scVelo (Used to implement trajectory inference)
      - monocle3 (Used to implement trajectory inference)
      - cellrank (Used to implement trajectory inference)
      - diffxpy (Used to identify DEGs)
      - AUCell (Used for calculating gene set expression score)
      - pyscenic (Used for calculating gene set expression score)
      - jpy_tools (A wrapper of single-cell analysis tools, which is available here [jpy_tools](main/jpy_tools))
      - OrthoFinder (Used to find orthologs between arabidopsis and soybean)
      - rpy2 (Used to implement invocation of R packages in python environment)
      - clusterprofiler (Used to perform GO enrichmenth analysis)

## Main steps

### Preprocessing
1. Get 10X cell-gene matrix using the [snakemake file](main/snakemake_cellranger/snakefile)
2. Get stereo-seq cell-gene matrix using the [script](main/scripts/run_orthofinder.sh)
3. Get orthologs between arabidopsis and soybean using the [script](main/scripts/run_orthofinder.sh)

### Analysis

This [jupyter file](main/jupyter/all_merged.ipynb) contains the scripts needed for downstream analysis. Github often fails to preview large jupyter files, You can download this [html version](main/jupyter/all_merged.html) and view it directly in your browser as an alternative. 

## Others
- The processed file can be downloaded at [OMIX data base](https://ngdc.cncb.ac.cn/omix/release/OMIX002290)
- The gene expression pattern can be explored at our [website](http://159.138.151.218:3569/)
  - If you found any bugs in our website, please reported [here](https://github.com/ZhaiLab-SUSTech/soybean_sn_st/issues/new)
