

'''  Creates a csv file of Jami database table 'interactions'.
     csv file name = 'interactions.csv'
     Adds a column named 'date_time' to 'interactions.csv' file.
     Adds converted timestamps to 'date_time' column.
'''

__author__ = "Andre Sele"

import csv
from datetime import datetime
import os
import pandas as pd
import sqlite3



# csv file name
file_name = 'interactions.csv'

# Jami database name
db_file = 'history.db'

# Open connection and create cursor object.
# Converts values in 'timestamp' column to date/time.
# Creates list of date/time values.
with sqlite3.connect(db_file, isolation_level=None,
                       detect_types=sqlite3.PARSE_COLNAMES) as conn:
    c = conn.cursor()
    li = []
    for val in c.execute("SELECT timestamp FROM interactions"):
        # Convert tuple to integer.
        result = int(''.join(map(str, val)))

        dt_object = datetime.fromtimestamp(result)
        li.append(dt_object)

# Creates temp csv file of datase table 'interactions'.
db_df = pd.read_sql_query("SELECT * FROM interactions", conn)
db_df.to_csv('temp1.csv', index=False)

# Creates new column 'date_time' in dataframe.
# Enters list values into 'date_time' column.
df = pd.read_csv('temp1.csv')
df.loc[:,'date_time'] = li

# Writes dataframe to new csv file named 'interactions.csv'
df.to_csv(file_name, index=False)
# Deletes temp file.
os.remove('temp1.csv')







