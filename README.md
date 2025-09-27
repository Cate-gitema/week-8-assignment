📊 COVID-19 Metadata Analysis (CORD-19)

This project analyzes the CORD-19 metadata.csv dataset using Pandas, Seaborn, Matplotlib, and Streamlit.

The dataset is very large (~1 GB, 1,056,660 rows × 19 columns) and therefore is not included in this submission.
👉 It can be downloaded here: CORD-19 Dataset on Kaggle

✅ What This Project Does

Loads and explores the metadata.csv file

Cleans missing data and formats columns (e.g., publish_time)

Analyzes publications by year and journal

Creates visualizations:

📈 Publications over time

📚 Top journals

☁️ Word cloud of titles

📊 Distribution by source

Builds an interactive Streamlit dashboard

📂 Files in This Project
week-8-assignment/
├── app.py          # Streamlit dashboard
├── analysis.py     # Pandas + Matplotlib practice script
├── README.md       # Project explanation
├── requirements.txt# Dependencies

🛠️ How to Run

Install required libraries:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py


Open your browser at http://localhost:8501
 to view the dashboard.

📦 Dependencies

pandas

matplotlib

seaborn

wordcloud

streamlit

🙌 Notes

The dataset is too large to include in this repo. Please download it from Kaggle.

For testing, you can load a smaller sample in Pandas:

df = pd.read_csv("metadata.csv", nrows=50000)
















