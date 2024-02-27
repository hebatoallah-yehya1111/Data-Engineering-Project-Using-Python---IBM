# -*- coding: utf-8 -*-
"""banks_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Mz5jBYSEHFGjitno8SbhIWMVhgLNpwWx
"""

!pip install pandas
!pip install db-sqlite3

import requests
from bs4  import BeautifulSoup
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime

# Initialization process
url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
csv_path = 'exchange_rate.csv'

def log_progress(message):
    ''' This function logs the mentioned message at a given stage of the code execution to a log file. Function returns nothing'''
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("code_log.txt","a") as f:
        f.write(timestamp + ' : ' + message + '\n')

table_attribs = ['Rank', 'Name', 'MC_USD_Billion']

def extract(url, table_attribs):
    ''' This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''
    page = requests.get(url).text
    data = BeautifulSoup(page,'html.parser')
    df = pd.DataFrame(columns=table_attribs)
    rows = []
    tables = data.find_all('tbody')
    if tables:
        # Find all rows in the table
        table_rows = tables[0].find_all('tr')
        # Iterate over each row (skip the header row)
        for row in table_rows[1:]:
            # Find all columns in the row
            cols = row.find_all(['th', 'td'])
            # Extract the text from each column
            row_data = [col.get_text(strip=True) for col in cols]
            # Append the row data to the list of rows
            rows.append(row_data)
    # Create a DataFrame from the list of rows
    df = pd.DataFrame(rows, columns=table_attribs)
    df.drop(columns=['Rank'], inplace=True)
    return df

df=extract('https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks', table_attribs=table_attribs)

df

def transform(df, csv_path):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''
    ex_rate_df=pd.read_csv(csv_path)
    dict_ex_rate = ex_rate_df.set_index('Currency').to_dict()['Rate']
    df['MC_USD_Billion'] = pd.to_numeric(df['MC_USD_Billion'], errors='coerce')

    df['MC_GBP_Billion'] = [np.round(x*dict_ex_rate['GBP'],2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x*dict_ex_rate['EUR'],2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x*dict_ex_rate['INR'],2) for x in df['MC_USD_Billion']]



    return df

transform(df=df, csv_path='/content/exchange_rate.csv')['MC_EUR_Billion'].sort_values()

def load_to_csv(df, output_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''
    df.to_csv(output_path)

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

def run_query(query_statement, sql_connection):
    ''' This function runs the stated query on the database table and
    prints the output on the terminal. Function returns nothing. '''
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)

log_progress('Preliminaries complete. Initiating ETL process')

df = extract(url, table_attribs)

log_progress('Data extraction complete. Initiating Transformation process')

df = transform(df=df,csv_path=csv_path)

log_progress('Data transformation complete. Initiating loading process')

load_to_csv(df,'Largest_banks_data.csv')

log_progress('Data saved to CSV file')

sql_connection = sqlite3.connect("/content/Banks.db")

log_progress('SQL Connection initiated.')

load_to_db(df, sql_connection,'Largest_banks')

log_progress('Data loaded to Database as table. Running the query')

query_statement_1 = f"SELECT * FROM Largest_banks"
run_query(query_statement_1, sql_connection)

query_statement_2 = f"SELECT AVG(MC_GBP_Billion) FROM Largest_banks"
run_query(query_statement_2, sql_connection)

query_statement_3 = f"SELECT Name from Largest_banks LIMIT 5"
run_query(query_statement_3, sql_connection)


log_progress('Process Complete.')

sql_connection.close()

log_progress('Server Connection closed')
