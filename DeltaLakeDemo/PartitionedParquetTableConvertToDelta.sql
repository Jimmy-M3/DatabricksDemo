-- Databricks notebook source
-- MAGIC %md
-- MAGIC 1 Create a parquet partitioned table\n
-- MAGIC 2 Insert some data to the table created above\n
-- MAGIC 3 Show paritions\n
-- MAGIC 3 Convert to Delta\n
-- MAGIC 4 Show paritions\n

-- COMMAND ----------

-- DBTITLE 1,Create A Delta Table
Create external table if not exists parquet_demo(
  id int,
  name string
) 
partitioned by (gender string)
stored as parquet
location '/data/delta_demo/parquet_table'

-- COMMAND ----------

insert into parquet_demo values(1001,'Jimmy','M'),(1002,'Ivy','F');

-- COMMAND ----------

Show partitions parquet_demo

-- COMMAND ----------

convert to delta parquet_demo;

-- COMMAND ----------

show partitions parquet_demo;

-- COMMAND ----------

describe extended parquet_demo;
