# Databricks notebook source
# MAGIC %scala
# MAGIC // Define Schema
# MAGIC import org.apache.spark.sql.types.{StructType,StructField,StringType,DateType}
# MAGIC val schema:StructType = StructType(Array(
# MAGIC    StructField("name",StringType,false),
# MAGIC    StructField("address",StringType,false),
# MAGIC    StructField("birthday",DateType,false)
# MAGIC  )
# MAGIC )

# COMMAND ----------

# MAGIC %scala
# MAGIC // Read daliy csv file
# MAGIC import java.time.LocalDate
# MAGIC import java.time.format.DateTimeFormatter
# MAGIC
# MAGIC val currentDate = LocalDate.now()
# MAGIC val formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd")
# MAGIC val currentDateAsString = currentDate.format(formatter)
# MAGIC
# MAGIC val path:String = s"/data/quality/raw/raw_data_$currentDateAsString.csv"
# MAGIC val df = spark.read.format("csv").schema(schema).option("sep","|").load(path)

# COMMAND ----------

# MAGIC %scala
# MAGIC // Write into Bronze Table
# MAGIC df.write.mode("append").saveAsTable("bronze.client_brz")
