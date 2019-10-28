# LendingClub

## Table of Contents

1. [Motivation](#motivation)
2. [Overview](#overview)
3. [Dataset](#dataset)
4. [Conversion](#conversion)
5. [Transformation](#transformation)
6. [Database](#database)
7. [Visualization](#visualization)
8. [Vision](#vision)
9. [Notes](#notes-on-setting-the-environment)

# Overview
This project aims at creating a data pipeline for integrating the multiple datasets about single-family mortgage loans and training a robust machine learning model to predict the mortgage default.

Raw data are released by Freddie Mac and Fannie Mae, which are the top two goverment-sponsored enterprises in US.

# DataPipeline

Following along the pipeline, I first ingest the dataset with a total size of 254.6G from the Fannie Mae and Freddie mac to AWS S3; clean, tranforming and combing the data in Spark, and then save the clean dataset in Postgres; traning the ML models in Spark and deploy the model at Flask.

The structure of the directory is mapped according to this tree:

|- data_pipeline.png
|- README.md
|- db
    |- schema.sql
|- flask
    |- run.py
    |- views.py
    |- requirements.txt
|- src
    |- create_table.py
    |- ml_postgres.py
    |- freddie_prepare.py
    |- fannie_prepare.py


