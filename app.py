# app.py

# ---- Import Libraries ----
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# ---- Load Data ----
file_path = "metadata.csv"
df = pd.read_csv(file_path, low_memory=False)

# ---- Data Cleaning ----
df = df.dropna(subset=["title", "abstract", "publish_time"])
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
df["year"] = df["publish_time"].dt.year

# ---- Streamlit App ----
st.title("CORD-19 Metadata Explorer")
st.write("An interactive app to explore COVID-19 research metadata.")

# Show sample data
st.subheader("Sample Data")
st.dataframe(df.head(10))

# ---- Analysis 1: Publications by Year ----
st.subheader("Publications by Year")
papers_by_year = df["year"].value_counts().sort_index()

fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.barplot(x=papers_by_year.index, y=papers_by_year.values, ax=ax1, palette="Blues_d")
ax1.set_title("Number of Publications by Year")
ax1.set_xlabel("Year")
ax1.set_ylabel("Count")
st.pyplot(fig1)

# ---- Analysis 2: Top Journals ----
st.subheader("Top Journals Publishing COVID-19 Research")
top_journals = df["journal"].value_counts().head(10)

fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax2, palette="viridis")
ax2.set_title("Top 10 Journals")
ax2.set_xlabel("Count")
ax2.set_ylabel("Journal")
st.pyplot(fig2)

# ---- Analysis 3: Distribution by Source ----
if "source_x" in df.columns:  # some CORD-19 versions have source_x column
    st.subheader("Distribution of Paper Counts by Source")
    fig3, ax3 = plt.subplots(figsize=(8, 5))
    sns.countplot(y="source_x", data=df, order=df["source_x"].value_counts().index, ax=ax3, palette="Set2")
    ax3.set_title("Paper Counts by Source")
    st.pyplot(fig3)

# ---- Interactive Filter ----
st.subheader("Filter by Year")
year_selected = st.slider("Select Year", int(df["year"].min()), int(df["year"].max()))
filtered_df = df[df["year"] == year_selected]
st.write(f"Number of papers in {year_selected}: {len(filtered_df)}")
st.dataframe(filtered_df.head(10))
