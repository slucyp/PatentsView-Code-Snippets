#Read-in script for 1978 Claims Data

# Importing necessary packages.
import os
import zipfile as zip
import pandas as pd
import csv
import numpy as np
# Set up file path:
# Please include the folder path of the file you are reading. Ex: os.chdir("C:/Users/johnsmith/Downloads")
os.chdir("")
file_name = "claims_1978.tsv.zip"
f_name = "claims_1978.tsv"
# Selecting the zip file.
zf = zip.ZipFile(file_name)
# Reading the selected file in the zip.
df = pd.read_csv(zf.open(f_name), delimiter="\t", quoting=csv.QUOTE_NONNUMERIC)
# Print first five observations
print(df.head())
# Print summary of data: number of columns, observations, and each variable data type
print(len(df))
df.info()
# Provide additional information on certain variables.
print(df.describe(exclude=[np.number]))


