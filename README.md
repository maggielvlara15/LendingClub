# LendingClub

## Table of Contents

1. [Overview](#overview)
2. [Dataset](#dataset)
3. [Data Exploration](#dataexploration)
4. [Data Processing](#dataprocessing)
5. [Database](#database)
6. [Visualization](#visualization)
7. [FutureWork](#FutureWork)

# Overview
LendingClub is the world's largest peer-to-peer lending platform, where investors provide funds for potential borrowers and investors earn a profit. This project consists of two parts:

1.The first part is to analyze the lending club dataset from 2007 to 2015. I am trying to explore the data and find valuable information from business perspetive and risk perspective. 

2.The second part is to build a pipleline to ingest and process the data in a efficient way. Following along the pipeline, I first ingest the dataset with a total size of 254.6G from the data source provided to AWS S3; clean and validate the dataset in Python3, and then save the dataset in Postgres.

The structure of the directory is mapped according to this tree:
'''
    |- data_pipeline.png
    |- README.md
    |- loan_analysis.ipynb
    |- db
        |- schema.sql
    |- src
        |- create_table.py
        |- data_cleaning.py
        |- config.ini
'''

