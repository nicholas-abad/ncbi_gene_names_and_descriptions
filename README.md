# Match Gene Names to NCBI Gene Functions

All used data is directly downloaded from the NCBI FTP fileshare website: [https://ftp.ncbi.nlm.nih.gov/gene/DATA/](https://ftp.ncbi.nlm.nih.gov/gene/DATA/)

## Current Datasets:

* The most recent dataset upload can be found within `outputs/gene_names_and_descriptions_2025-Feb-04_18:24:13.csv`

## How to use the data within Python:

* If you want to use the current dataset, you could either (1) download it locally from Github and use it like a normal csv file or (2) use the direct raw csv link if you want to programmatically use it
  * Example:
  * ```
    import pandas as pd

    data = pd.read_csv("https://media.githubusercontent.com/media/nicholas-abad/ncbi_gene_names_and_descriptions/refs/heads/main/outputs/gene_names_and_descriptions_2025-Feb-04_18%3A24%3A13.csv", delimiter="\t")
    ```

## How to run the code and generate your own file:

1. Open your terminal, navigate to the desired location and clone the repository.
2. Install the necessary Python packages via pip, which is literally only Pandas
3. Run the `run.py` script.
