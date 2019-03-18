import pandas as pd
import os

file_a = r'data/in_data_a.csv'  # in_data_a location.
file_p = r'data/in_data_p.csv'  # in_data_p location.

# In in_data_a and in_data_p the columns are named differently,
# so I decided to use custom names to work inside the program
# without changing the source files.

# This is where the data from the files is read.
# Assigning column custom names.
read_a = pd.read_csv(file_a, index_col=False,
                     names=['date', 'campaign',
                            'id', 'ad_id', 'os',
                            'installs', 'app'])

read_p = pd.read_csv(file_p, index_col=False,
                     names=['date', 'campaign_id',
                            'ad_id', 'spend'])

# Merging two tables by date and ad_id.
mergeTables = read_a.merge(read_p, 'right', on=['date', 'ad_id'])

# Delete rows that have no data.
mergeTables = mergeTables.dropna()

# Computing a number of rows in the table.
sLength = len(mergeTables['date'])


# That formula is computing cpi for 'i' row.
# First step we check each part of the equation is greater than zero.
# Since the data in the dataframe is written using string data,
# we compare it with string '0.000'.
# Second step is the calculation of the cpi, for that we convert data to float.
def cpi_formula(i):
    if (mergeTables['installs'][i] != '0.000' and
            mergeTables['spend'][i] != '0.000'):
        cpi_result = (float(mergeTables['spend'][i]) /
                      float(mergeTables['installs'][i]))
        return cpi_result
    else:
        return 'none'


# Here we will create a list in which we will write cpi for each rows.
# After that, we add that list to merged table.
def expp():
    cpi_list = []
    for i in range(0, sLength, 1):
        cpi_list.append(cpi_formula(i))
    mergeTables['cpi'] = cpi_list


expp()

# Sorting data by name of the app and date.
mergeTables = mergeTables.sort_values(by=['app', 'date'])

# Creating additional file to manipulate data.
mergeTables.to_csv(r'output/help_file.csv', index=False)

# With help_file, we can read merged table
# and select columns we need(in the order we need).
out = pd.read_csv(r'output/help_file.csv',
                  usecols=['app', 'date',
                           'campaign', 'os',
                           'installs', 'spend',
                           'cpi'])[['app', 'date',
                                    'campaign', 'os',
                                    'installs', 'spend', 'cpi']]
# Saving data to out.csv.
out.to_csv(r'output/out.csv', index=False)
# Removing help file.
os.remove(r'output/help_file.csv')
