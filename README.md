📊 COVID-19 Metadata Analysis (CORD-19)

This project analyzes the CORD-19 metadata.csv dataset using Pandas, Seaborn, Matplotlib, and Streamlit.

The dataset is very large — over 1,056,660 rows and 19 columns, with a file size close to 1 GB. It contains COVID-19–related research metadata such as titles, abstracts, publication dates, sources, and identifiers (DOI, PubMed ID, PMC ID).

🚀 Features

Data Loading & Exploration

Load and inspect the large metadata.csv file

Preview first rows, dataset shape, and data types

Identify missing values in key columns (title, abstract, doi, pubmed_id, etc.)

Data Cleaning

Handle missing values by removal or imputation

Convert publish_time into datetime format

Extract publication year for trend analysis

Add derived features like abstract word count

Data Analysis

Count publications by year

Identify top journals publishing COVID-19 research

Check frequency of missing values

Generate descriptive statistics for numerical IDs

Visualization

📈 Trend of publications over time

📚 Bar chart of top publishing journals

☁️ Word cloud of paper titles

📊 Distribution of papers by source

Interactive Dashboard (Streamlit)

View dataset summary

Explore visualizations with filters and widgets

Inspect raw data samples

⚠️ Working with a Large Dataset

The metadata.csv file is very large (~1 GB).

Loading it requires sufficient memory (≥8 GB RAM recommended).

For faster development, you can work on a smaller sample:

df = pd.read_csv("metadata.csv", nrows=50000)  # load first 50k rows


When running the full analysis, Streamlit may take time to process visualizations.

📂 Dataset Snapshot

From the first 5 rows of metadata.csv:

   cord_uid    sha  source_x   title   doi   ...   s2_id
0  ug7v899j   NaN   Elsevier  ...     NaN
1  02tnwd4m   NaN   Elsevier  ...     NaN
2  ejv2xln0   NaN   Elsevier  ...     NaN
3  2b73a28n   NaN   Elsevier  ...     NaN
4  9785vg6d   NaN   Elsevier  ...     NaN


Shape: (1,056,660 rows × 19 columns)

Columns with Missing Data (sample):

sha: 682,894 missing

title: 503 missing

doi: 399,880 missing

pmcid: 667,089 missing

pubmed_id: 557,728 missing

abstract: 235,544 missing

publish_time: 1,814 missing

🛠️ Installation & Setup

Clone the repo:

git clone https://github.com/Cate-gitema/week-8-assignment.git
cd week-8-assignment


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py

📦 Dependencies

pandas

matplotlib

seaborn

wordcloud

streamlit

🙌 Acknowledgements

Dataset: CORD-19: COVID-19 Open Research Dataset

Tools: Python, Pandas, Seaborn, Matplotlib, Streamlit
