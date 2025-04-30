# Netflix-data-cleaning

netflix-data-engineering-project/
│
├── data/
│   └── (README explaining data is downloaded via Kaggle API)
│
├── notebooks_or_scripts/
│   └── data_extraction.py       # Python script using Kaggle API
│   └── README.md                # Explain what each script does
│
├── sql/
│   └── create_tables.sql        # SQL code for raw, fact, and dimension tables
│   └── transform_data.sql       # Data cleaning and transformation queries
│   └── analysis_queries.sql     # Final queries to answer business questions
│
├── requirements.txt             # List of Python libraries (e.g., kaggle)
├── .gitignore                   # Exclude API keys or credentials
├── README.md                    # Main project explanation
└── kaggle.json                  # (Add to .gitignore; don’t upload this!)
📝 README.md Content Template
Here’s what your README.md should contain:

🎬 Netflix Data Engineering Pipeline (SQL + Python)
📌 Overview
This project demonstrates an end-to-end data engineering pipeline using Python and SQL Server. It walks through the process of data extraction from Kaggle, loading it into SQL Server, transforming the data using SQL, and finally performing business analytics queries.

🧰 Tools & Technologies Used
Python (for automation and API access)

Kaggle API (for downloading the dataset)

SQL Server (for storing, transforming, and analyzing data)

Libraries: kaggle, pandas (if used)

📂 Project Structure

Folder / File	Purpose
data/	Placeholder for dataset info or samples
notebooks_or_scripts/	Python scripts for data extraction and automation
sql/	SQL files for table creation, transformation, queries
requirements.txt	Python dependencies
📥 Dataset Source
Source: Netflix Titles on Kaggle

Access via Kaggle API (requires kaggle.json authentication)

🔧 How to Run
Clone the repository

Install dependencies:

nginx
Copy
Edit
pip install -r requirements.txt
Add your kaggle.json to the root (⚠ Do not commit it!)

Run the data_extraction.py to download data

Use the SQL scripts in sql/ to:

Create and populate raw table

Transform data into dimensional model

Run analysis queries

📈 Final Output
One fact table

Four dimension tables

Answers to 5+ analytical questions

🧠 Learning Goals
Practice with ELT pipeline

Hands-on with SQL data modeling

Integration of APIs and databases

Real-world data engineering simulation
