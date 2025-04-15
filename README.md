# Introduction

The Paleobiology Database (PBDB) is a valuable public resource developed for the global scientific community, created by the Encyclopedia of Life. This multi-disciplinary, international effort has been organized to provide comprehensive, collection-based occurrence and taxonomic data for marine and terrestrial life forms across any geological era. The overarching goals of the PBDB include fostering collaboration and integrating large datasets into a cohesive database infrastructure. Freely accessible at http://paleobiodb.org/, the Paleobiology Database is maintained by an international group of paleontologists and is released under a Creative Commons Attribution 4.0 International license. For citation purposes, the data set is officially referenced as "Encyclopedia of Life. (2025). Paleobiology Database (PBDB) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.14829528."

# Getting Started

When you first download the data from the Paleobiology Database, you will need to retain only the file named `taxon.tab` for this project. This file contains the primary taxonomic data essential for your research or analysis. To manage this data effectively, you can run the script `split_taxon.py` to divide the original `taxon.tab` file into more manageable parts. Alternatively, you can directly use the already split version that includes `Version v710.5281/zenodo.14829528` with files `taxon_part1.tab` and `taxon_part2.tab`, which are part of the repository.

# Additional Notes 

By default, vue-cli-service configures the server to use HTTP, as generating and managing SSL certificates for HTTPS on local development setups can add unnecessary complexity.