# Convert_Timestamps

This script was written while working on an application analysis project.


JamiDB_csv_date_time.py may be used to convert the timestamps found in history.db.

history.db is the name of a database which is associated to a Jami Messenger user account.

The script converts the UNIX timestamps (10 digits) found in the table 'interactions' within history.db.

The information from the table 'interactions' is written to a csv file. 

The converted timestamps are to be found in the column 'date_time'. 

Note: For the purpose of experimentation an exe file was created by using pyinstaller. The exe file (JamiDB_csv_date_time.exe)
is found in the Resource folder.
