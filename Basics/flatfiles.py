# Python 
# All the different flat file formats supported by pandas - CSV, TSV, fixed-width, etc.

import pandas as pd 

# import csv file 

#pd.read_csv('C:\\Users\\vgpsa\\Python Projects\\Data Analyst\\ata Collection\\data\\data\\sample.csv')
#C:\Users\vgpsa\Python Projects\Data Analyst\Data Collection\data\sample.csv

import pandas as pd

# Since your CSV and script are in the same folder, you can just use:
df = pd.read_csv(r'C:\Users\vgpsa\OneDrive\Documents\Python\practice\csvfile.csv')

df.head()

# import excel file 

# import JSON file 

# import XML file

# import parquet file

# open a text file 
