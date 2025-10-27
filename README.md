# Python-ETL-Project

Project: Python ETL Script

Overview

This project demonstrates a simple Python ETL process. It extracts data from CSV, transforms it using Pandas, and loads it into a SQLite database.

Features

•	Extract data from CSV

•	Transform data (cleaning, formatting)

•	Load data into SQLite

Requirements

•	Python 3.8+

•	pandas

•	sqlalchemy

•	sqlite3

Sample Data

Include products.csv in the data/ folder with sample product information.

Step-by-Step Instructions

1.	Clone the repository

2.	Set up virtual environment:

 	python -m venv venv

source venv/bin/activate  # Linux/Mac

venv\Scripts\activate     # Windows

3.	Install dependencies:

 	pip install pandas sqlalchemy

4.	Run the ETL script:

 	python etl_script.py

5.	Verify the database:

 	sqlite3 products.db

sqlite> SELECT * FROM products;

Output

A SQLite database products.db containing a table products with transformed data.

Repository Structure

Python-ETL-Project/

├── data/           # Sample CSV files

├── etl_script.py   # Python ETL script

└── README.md       # Project documentation

