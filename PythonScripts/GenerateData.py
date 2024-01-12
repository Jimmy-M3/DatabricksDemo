# Databricks notebook source
# DBTITLE 1,Import Dependencies
from faker import Faker
from random import randint
from datetime import date

# COMMAND ----------

# DBTITLE 1,Randomly Append New Data
fake = Faker(locale='en_US')
rows_number = randint(10,100)

with open("/dbfs/data/quality/raw/raw_data_{}.csv".format(date.today()),"w") as file:    
    for i in range(rows_number):
        fake_info = "|".join([fake.name(),fake.address().replace('\n',' '),fake.date_of_birth().strftime("%Y-%m-%d"),"\n"])
        file.writelines(fake_info)


# COMMAND ----------


