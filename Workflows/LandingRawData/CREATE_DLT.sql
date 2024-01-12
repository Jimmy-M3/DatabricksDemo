-- Databricks notebook source
create or refresh live table dlt_demo as 
select name,address,birthday from bronze.client_brz
