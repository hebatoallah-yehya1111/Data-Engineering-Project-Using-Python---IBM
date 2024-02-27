# Top 10 Largest Banks Data Compilation

## Overview
This code compiles a list of the top 10 largest banks in the world ranked by market capitalization in billion USD. It then transforms and stores the data in GBP, EUR, and INR currencies based on the provided exchange rate information available in a CSV file. Finally, the processed information table is saved locally both in CSV format and as a database table.

## Requirements
- Python 3.x
- Pandas
- SQLite3

## Usage
1. Ensure Python 3.x is installed on your system.
2. Install the required libraries using pip:


   ![image](https://github.com/hebatoallah-yehya1111/Data-Engineering-Project-Using-Python---IBM/assets/77882036/2849f332-4289-43da-9ff9-d62844262554)

3. Place the exchange rate information CSV file in the same directory as the script.
4. Run the script `banks_project.py`.
5. The processed information will be saved locally as a CSV file (`Largest_banks_data.csv`) and as a database table (`Largest_banks`) in the SQLite database.

## Project Tasks
1. **Log Progress**: Write a function to log the progress of the code at different stages in a file `code_log.txt`.
2. **Extract Tabular Information**: Extract the tabular information from the given URL and save it to a DataFrame.
3. **Transform DataFrame**: Add columns for Market Capitalization in GBP, EUR, and INR based on the exchange rate information.
4. **Load to CSV**: Load the transformed DataFrame to an output CSV file.
5. **Load to Database**: Load the transformed DataFrame to an SQL database server as a table.
6. **Run Queries on Database**: Run queries on the database table.
7. **Verify Log Entries**: Verify that the log entries have been completed at all stages by checking the contents of the file `code_log.txt`.

## Additional Parameters
- Code Name: `banks_project.py`
- Data URL: [Top 10 Largest Banks](https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks)
- Exchange Rate CSV Path: [Exchange Rate CSV](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv)
- Table Attributes (upon Extraction only): Name, MC_USD_Billion
- Table Attributes (final): Name, MC_USD_Billion, MC_GBP_Billion, MC_EUR_Billion, MC_INR_Billion
- Output CSV Path: `./Largest_banks_data.csv`
- Database Name: `Banks.db`
- Table Name: `Largest_banks`
- Log File: `code_log.txt`

## File Structure
- `banks_project.py`: Main Python script for compiling and processing the bank data.
- `exchange_rate.csv`: CSV file containing exchange rate information.
- `Largest_banks_data.csv`: Output CSV file containing processed bank data.
- `Banks.db`: SQLite database file containing the processed bank data table.
- `code_log.txt`: Log file containing progress entries.

## Example Execution

![image](https://github.com/hebatoallah-yehya1111/Data-Engineering-Project-Using-Python---IBM/assets/77882036/7a6362b1-7929-4181-8473-257909cefd37)



## Note
- Ensure that the script and exchange rate CSV file are in the same directory.


