# 🎬 Netflix Data Engineering Pipeline (SQL + Python)

This project demonstrates an *end-to-end data engineering pipeline* using *Python* and *SQL Server*. It replicates a real-world ELT (Extract, Load, Transform) workflow — extracting data from Kaggle, loading it into a database, transforming it into a structured schema, and performing analytics to answer business questions.

---

## 🧰 Tools & Technologies Used

- *Python*: For scripting and data extraction via Kaggle API
- *Kaggle API*: To automate the download of the dataset
- *SQL Server*: For data storage, transformation, and analytics
- *Libraries*:
  - kaggle (for dataset download)
  - pandas (optional, if used for preprocessing)

---

## 📁 Project Structure

netflix-data-engineering-project/ │ ├── data/ # Placeholder for dataset or samples │ ├── notebooks_or_scripts/ │ └── data_extraction.py # Script to fetch data from Kaggle │ ├── sql/ │ ├── create_tables.sql # SQL commands to create raw and modeled tables │ ├── transform_data.sql # SQL queries to clean and structure data │ └── analysis_queries.sql # SQL queries for business analysis │ ├── requirements.txt # Python libraries needed ├── .gitignore # To exclude kaggle.json and other sensitive files └── README.md # Project documentation (this file)

yaml
Copy
Edit

---

## 📥 Dataset Information

- *Dataset Name*: Netflix Titles
- *Source*: [Kaggle - Netflix Shows Dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- *Access Method*: Kaggle API

---

## ⚙ How to Run This Project

1. *Clone the Repository*
   ```bash
   git clone https://github.com/your-username/netflix-data-engineering-project.git
   cd netflix-data-engineering-project
Install Python Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Add your Kaggle API Token

Place your kaggle.json file in the root directory

Add it to .gitignore to avoid committing sensitive data

Run the Extraction Script

bash
Copy
Edit
python notebooks_or_scripts/data_extraction.py
Set up SQL Server

Execute sql/create_tables.sql to create raw and structured tables

Run sql/transform_data.sql to clean and model the data

Use sql/analysis_queries.sql to generate business insights

🧠 Learning Objectives
✅ Understand how to build a real-world ELT pipeline
✅ Practice integrating Python scripts with APIs and SQL
✅ Learn to structure raw data into fact and dimension tables
✅ Gain insights using analytical SQL queries

📈 Final Output
✅ One raw data table

✅ One fact table

✅ Four dimension tables

✅ SQL queries that answer key business questions like:

What are the most common genres?

Which country produces the most Netflix content?

How has content production changed over time?

