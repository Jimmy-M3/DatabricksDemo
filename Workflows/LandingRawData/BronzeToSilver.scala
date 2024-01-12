// Databricks notebook source
val df = spark.table("bronze.client_brz")

// COMMAND ----------

df.write.mode("append").saveAsTable("sliver_cln.client_slv_cln")

// COMMAND ----------


