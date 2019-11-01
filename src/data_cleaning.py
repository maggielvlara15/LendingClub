
import pandas as pd
import numpy as np
import configparser
import ast

# Create a config file that can store path and lists
config = configparser.ConfigParser()
config.read('config.ini')

def change_date_type(df):  
    '''
    input:dataframe
    output:dataframe
    purpose: convert string to datetime format
    '''   
    df[['issue_d','last_pymnt_d','last_credit_pull_d','earliest_cr_line']]=\
    df[['issue_d','last_pymnt_d','last_credit_pull_d','earliest_cr_line']].apply(pd.to_datetime)
    return df

def remove_duplicates(df):   
    '''
    input: dataframe
    output: dataframe
    purpose: remove duplicate records(in rows)
    '''   
    df = df.drop_duplicates()
    return df

def emp_length_to_int(df): 
    '''
    input: dataframe
    output: dataframe
    purpose: Create a new column and convert emp_length to integers
    '''  
    df['emp_length_int']=np.nan
    df.loc[df['emp_length'] == '10+ years', "emp_length_int"] = 10
    df.loc[df['emp_length'] == '9 years', "emp_length_int"] = 9
    df.loc[df['emp_length'] == '8 years', "emp_length_int"] = 8
    df.loc[df['emp_length'] == '7 years', "emp_length_int"] = 7
    df.loc[df['emp_length'] == '6 years', "emp_length_int"] = 6
    df.loc[df['emp_length'] == '5 years', "emp_length_int"] = 5
    df.loc[df['emp_length'] == '4 years', "emp_length_int"] = 4
    df.loc[df['emp_length'] == '3 years', "emp_length_int"] = 3
    df.loc[df['emp_length'] == '2 years', "emp_length_int"] = 2
    df.loc[df['emp_length'] == '1 year', "emp_length_int"] = 1
    df.loc[df['emp_length'] == '< 1 year', "emp_length_int"] = 0.5
    df.loc[df['emp_length'] == 'n/a', "emp_length_int"] = 0
    return df       

def validate_negative(df):    
    '''
    input: dataframe
    output: dataframe
    purpose: add a flag column that marks negative values in important columns
    '''  
    lst = ['loan_amnt','int_rate','installment','annual_inc','dti']
    df['negative_flag'] = np.where((~(df[lst]<0)).all(1),'Yes','No')
    return df

def validate_number(df,loan_max=5000000,int_max=100,installment_max=10000,dti_max=1000):    
    '''
    input: dataframe, max boudaries
    output: dataframe
    purpose: add a flag column that mark the outliers
    '''   
    df['outlier_flag'] = np.where(((df['loan_amnt']<=loan_max)&(df['int_rate']<=int_max)&(df['installment']<=installment_max)\
            &(df['dti']<=dti_max)),'No','Yes')
    return df

# term, home_ownership,addr_state,application_type
def validate_type(df):   
    '''
    input: dataframe
    output: dataframe
    purpose: add a flag column that mark the wrong categories
    note: the category lists are saved at config.ini and can be updated
    '''  
    term_string = config['categories']['term']
    home_ownership_string = config['categories']['home_ownership']
    addr_state_string = config['categories']['addr_state']
    application_type_string = config['categories']['application_type']
    term = ast.literal_eval(term_string)
    home_ownership = ast.literal_eval(home_ownership_string)
    addr_state = ast.literal_eval(addr_state_string)
    application_type = ast.literal_eval(application_type_string)
    df['invalid_type_flag'] = np.where(((df['term'].isin(term))&(df['home_ownership'].isin(home_ownership))\
                         &(df['addr_state'].isin(addr_state))&(df['application_type'].isin(application_type)))\
                         ,'No','Yes')
    return df
    

    
    
    
    
    
    
    
    
    
    