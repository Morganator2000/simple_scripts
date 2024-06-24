if(!requireNamespace("BiocManager")){
  install.packages("BiocManager")
}
BiocManager::install("phyloseq")
BiocManager::install("microbiome")
# https://github.com/joey711/phyloseq
library(phyloseq)
?phyloseq
?otu_table

