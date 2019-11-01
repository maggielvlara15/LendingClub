
import pandas as pd
from data_cleaning import *
import configparser
import ast
import time
import sys
import logging

# Create a config file that can store path and lists
config = configparser.ConfigParser()
config.read('config.ini')

def read_file(file_with_path):
    '''
    input: path+file_name (string type)
    output: dataframe
    function: read in files
    '''
    try:
       df = pd.read_csv(file_with_path,low_memory=False)
       return df
    except IOError:
       logging.exception('')          

# get data from 2007-2015
def data_range(df, begin_year=2007, end_year=2015):
    '''
    input: dataframe, start year, end year
    output: dataframe
    function: get the dataframe whithin the given date range
    '''
    df_series = pd.to_datetime(df['issue_d'])
    df['year'] = df_series.dt.year
    df = df[(df['year'] >= begin_year) & (df['year'] <= end_year)]
    return df

# clean data(remove columns)
def remove_unique(df):
    ''' 
    Input: dataframe 
    output: dataframe 
    function: remove columns has only one value
    '''
    df = df.loc[:,df.nunique()!=1]
    return df

def remove_missing(df,ratio=0.9):
    '''
    input: dataframe, the ratio of missing data
    output: dataframe
    function: remove columns who have more than 90% missing data
    Comment: The ratio can be changed
    '''
    count = ratio*len(df)
    df = df.dropna(thresh=count,axis=1)
    return df

def remove_redundant(df):
    '''
    input: dataframe
    output: dataframe
    function: remove the columns that have redundant information
    '''
    lst_string = config['columns']['redundant_columns']
    lst = ast.literal_eval(lst_string)
    for i in lst:
       if i in df.columns.tolist(): 
           df = df.drop(i,axis=1)
    return df    

def process_column(file_with_path):
    '''
    input: path+file_name (string type)
    output: dataframe
    function: read in data and go through the column processing
    '''
    raw_data = read_file(file_with_path)
    raw_data_range = data_range(raw_data)
    df = remove_unique(raw_data_range)
    df = remove_missing(df)
    df = remove_redundant(df)
    return df

def clean_data(df_column_clean):
    '''
    input: dataframe after processing columns
    output: dataframe after data cleaning
    function: cleaning the data
    ''' 
    df = change_date_type(df_column_clean)
    df = remove_duplicates(df)
    df = emp_length_to_int(df)
    df = validate_negative(df)
    df = validate_number(df)
    df = validate_type(df)
    df = df.reset_index()
    return df

def main(file_with_path,result_with_path):
    '''
    input1: file name with path (string type)
    input2: result name with path (string type)
    main function to run through all the processes
    '''
    df = process_column(file_with_path)
    df_clean = clean_data(df)
    df_clean.to_csv(result_with_path, index=False)    

if __name__ == '__main__':
   main(sys.argv[1],sys.argv[2])
    
    


    


    
    

