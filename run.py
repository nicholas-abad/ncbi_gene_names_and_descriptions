import pandas as pd
import os
from datetime import datetime

# Descriptions of each data file can be found here: https://ftp.ncbi.nlm.nih.gov/gene/DATA/README

# Read in the gene_info.gz zipped file in batches.
# NOTE: Due to this being a large file, this may take some time.
print("(1/4) Reading in gene_info.gz...")
iter_gene_info = pd.read_csv(
    "https://ftp.ncbi.nlm.nih.gov/gene/DATA/gene_info.gz", 
    compression="gzip", delimiter="\t", 
    usecols=["#tax_id", "GeneID", "Symbol", "description"], 
    iterator=True, chunksize=100000
)

homo_sapiens_gene_info = pd.concat(
    [
        chunk[chunk['#tax_id'] == 9606] for chunk in iter_gene_info
    ]
)

# Read in the gene_summary.gz
print("(2/4) Reading in gene_summary.gz...")
gene_summary = pd.read_csv(
    "https://ftp.ncbi.nlm.nih.gov/gene/DATA/gene_summary.gz", 
    compression="gzip", delimiter="\t"
)

homo_sapiens_gene_summary = gene_summary[
    gene_summary["#tax_id"] == 9606
]

# Merge the two dataframes together.
print("(3/4) Merging the two dataframes together...")
result = pd.merge(
    homo_sapiens_gene_summary, 
    homo_sapiens_gene_info.drop("#tax_id", axis=1), 
    left_on="GeneID", 
    right_on="GeneID", 
    how="left"
)

# Write the dataframe.
print("(4/4) Writing the dataframe...")
current_time = datetime.now().strftime('%Y-%b-%d_%H:%M:%S')
if not os.path.exists("./outputs"):
    os.mkdir("outputs")
output_filename = f"./outputs/gene_names_and_descriptions_{current_time}.csv"
result.to_csv(
    output_filename,
    index=False, sep="\t"
)

print(f"File successfully written to: {output_filename}")