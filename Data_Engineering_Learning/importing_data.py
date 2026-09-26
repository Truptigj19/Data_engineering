"""
Data Ingestion Basics
---------------------
Examples of importing data from common file formats
and relational databases using Python.

Learning Source:
DataCamp - Importing Data in Python
https://www.datacamp.com/completed/statement-of-accomplishment/course/e5388415ee0a06941f094ec7d0829fc1bab5569c
Topics covered:
- Text files
- NumPy flat files
- CSV files with pandas
- Excel files
- Pickle files
- SAS / Stata files
- HDF5 files
- MATLAB files
- Relational databases
- SQL queries
- JOINs
"""

# ============================================================
# 1. IMPORTING A TEXT FILE
# ============================================================

# "with" automatically closes the file after reading.
with open("data.txt", "r") as file:
    text = file.read()

print(text)


# ============================================================
# 2. IMPORTING NUMERICAL FLAT FILES USING NUMPY
# ============================================================

import numpy as np

# Import a numerical CSV/flat file.
data = np.loadtxt(
    "data.csv",
    delimiter=","
)

print(data)


# Useful options:
#
# skiprows=1  -> skip the first row (e.g. header)
# usecols=[0, 2] -> import only columns 0 and 2
# dtype=str -> read values as strings
#
# Example:
#
# data = np.loadtxt(
#     "data.csv",
#     delimiter=",",
#     skiprows=1,
#     usecols=[0, 2]
# )


# For files containing missing values or more complex data,
# genfromtxt() is more flexible than loadtxt().
#
# data = np.genfromtxt(
#     "data.csv",
#     delimiter=",",
#     skip_header=1
# )


# ============================================================
# 3. IMPORTING CSV / TABULAR DATA USING PANDAS
# ============================================================

import pandas as pd

df = pd.read_csv("data.csv")

print(df.head())
print(df.info())
print(df.shape)
print(df.columns)


# ============================================================
# 4. IMPORTING EXCEL FILES
# ============================================================

# Load an Excel workbook.
excel = pd.ExcelFile("sales.xlsx")

# See available sheet names.
print(excel.sheet_names)

# Import a sheet by name.
sales_df = excel.parse("Sales")

print(sales_df.head())


# Import a sheet by index.
# 0 = first sheet
# 1 = second sheet

first_sheet = excel.parse(0)

print(first_sheet.head())


# Useful options while importing:
#
# skiprows=[0] -> skip the first row
# names=[...]  -> provide custom column names
# usecols=[0]  -> import only the first column
#
# Example:
#
# df = excel.parse(
#     0,
#     skiprows=[0],
#     names=["Country", "Population"]
# )


# ============================================================
# 5. IMPORTING PICKLE FILES
# ============================================================

import pickle

# "rb" = read binary
with open("data.pkl", "rb") as file:
    pickle_data = pickle.load(file)

print(pickle_data)

# Pickle can store Python objects such as:
# lists, dictionaries, NumPy arrays, DataFrames, etc.
#
# IMPORTANT:
# Never load an untrusted pickle file because
# pickle can execute malicious code during loading.


# ============================================================
# 6. IMPORTING SAS FILES
# ============================================================

# SAS dataset (.sas7bdat)
#
# from sas7bdat import SAS7BDAT
#
# with SAS7BDAT("data.sas7bdat") as file:
#     sas_df = file.to_data_frame()
#
# print(sas_df.head())


# ============================================================
# 7. IMPORTING STATA FILES
# ============================================================

# Stata files normally use the .dta format.
#
# stata_df = pd.read_stata("data.dta")
#
# print(stata_df.head())


# ============================================================
# 8. IMPORTING HDF5 FILES
# ============================================================

import h5py

# "r" = read-only mode
#
# hdf_data = h5py.File("data.h5", "r")
#
# # View groups/datasets inside the file
# print(hdf_data.keys())
#
# # Example of accessing a group and dataset:
# # strain_group = hdf_data["strain"]
# # strain = np.array(strain_group["Strain"])
#
# hdf_data.close()


# ============================================================
# 9. IMPORTING MATLAB FILES
# ============================================================

import scipy.io

# .mat files can contain MATLAB workspace variables.
#
# mat_data = scipy.io.loadmat("workspace.mat")
#
# print(mat_data.keys())
#
# # Access a variable:
# # x = mat_data["x"]


# ============================================================
# 10. RELATIONAL DATABASES
# ============================================================

from sqlalchemy import create_engine, inspect

# Create a database engine.
#
# For SQLite:
#
# engine = create_engine("sqlite:///Northwind.sqlite")


# Get table names.
#
# inspector = inspect(engine)
# tables = inspector.get_table_names()
#
# print(tables)


# ============================================================
# 11. QUERYING A DATABASE USING SQL
# ============================================================

# Example SQL query:
#
# query = "SELECT * FROM Orders"


# Manual database connection approach:
#
# con = engine.connect()
#
# result = con.execute(query)
#
# rows = result.fetchall()
#
# df = pd.DataFrame(rows)
# df.columns = result.keys()
#
# con.close()


# ============================================================
# 12. QUERYING DATABASE DIRECTLY INTO PANDAS
# ============================================================

# A simpler approach is read_sql_query().
#
# query = "SELECT * FROM Orders"
#
# df = pd.read_sql_query(query, engine)
#
# print(df.head())


# ============================================================
# 13. SELECTING SPECIFIC COLUMNS
# ============================================================

# Instead of selecting every column:
#
# query = """
# SELECT OrderID, OrderDate
# FROM Orders
# """
#
# df = pd.read_sql_query(query, engine)


# ============================================================
# 14. FETCHING LIMITED ROWS
# ============================================================

# fetchall() -> retrieves all rows
#
# result.fetchall()


# fetchmany(5) -> retrieves 5 rows
#
# result.fetchmany(5)


# ============================================================
# 15. JOINING RELATIONAL TABLES
# ============================================================

# Example:
# Orders.CustomerID is related to Customers.CustomerID.
#
# query = """
# SELECT
#     Orders.OrderID,
#     Customers.CompanyName
# FROM Orders
# INNER JOIN Customers
# ON Orders.CustomerID = Customers.CustomerID
# """
#
# df = pd.read_sql_query(query, engine)
#
# print(df.head())


# ============================================================
# QUICK REFERENCE
# ============================================================

"""
Text file       -> open()
Numerical file  -> NumPy (loadtxt / genfromtxt)
CSV             -> pandas.read_csv()
Excel           -> pandas.read_excel() / ExcelFile()
Pickle          -> pickle.load()
SAS             -> SAS7BDAT
Stata           -> pandas.read_stata()
HDF5            -> h5py
MATLAB          -> scipy.io.loadmat()
Database        -> SQLAlchemy
SQL query       -> pd.read_sql_query()
JOIN            -> SQL JOIN
"""