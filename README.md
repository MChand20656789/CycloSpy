# 🦠 CycloSpy: Cyclosporiasis Surveillance Dashboard

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-blue)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

An interactive public health surveillance dashboard built with **Python**, **Pandas**, **Plotly**, and **Streamlit** to analyze CDC cyclosporiasis surveillance data across the United States.

This project demonstrates an end-to-end data analytics workflow including data cleaning, feature engineering, exploratory data analysis, interactive visualization, and dashboard development.

---

# Project Objectives

Public health officials frequently monitor disease surveillance data to identify trends, compare disease burden across regions, and prioritize interventions.

CycloSpy answers questions such as:

- Which states currently report the most cyclosporiasis cases?
- Which states have the highest incidence rates after adjusting for population?
- How does population size affect reported incidence?
- Which states appear to have unusually high disease burden?

---

# Key Insights

Analysis of the surveillance data revealed several notable patterns:

### 🦠 Michigan has the highest incidence rate

Michigan reports the highest incidence rate among all reporting areas, indicating a disproportionately high number of reported cyclosporiasis cases relative to its population.

---

### 📈 Ohio reports the most current-week cases

Ohio recorded the highest number of newly reported cases during the latest reporting period, suggesting active transmission during the current surveillance week.

---

### 📊 Incidence rate provides better comparisons than raw case counts

States with larger populations often report more total cases simply because more people live there. Calculating incidence rate (cases per 100,000 people) allows for fair comparisons between states of different sizes and helps identify areas with relatively higher disease burden.

---

### 🗺 Geographic patterns vary across the United States

The choropleth maps reveal that disease burden is not evenly distributed across the country. While some states report consistently low or zero incidence, others show substantially higher rates or larger cumulative case counts.

---

### 📉 Many states report few or no current-week cases

Several reporting areas recorded zero current-week cases, indicating that cyclosporiasis activity during this reporting period is concentrated in a relatively small number of states.

---

### 📌 Interactive exploration supports public health analysis

The dashboard enables users to:

- Compare states by incidence rate
- Explore current-week case counts
- Examine relationships between population and disease burden
- Identify states with unusually high reported activity
- View cleaned surveillance data used in the analysis

---

# Features

## Executive Summary

Provides an easy-to-read overview of:

- Key findings
- Highest incidence states
- Interpretation guidance
- Public health context

---

## KPI Cards

Displays:

- Total reported cases
- Average incidence rate
- State with highest incidence rate

---

## Interactive Visualizations

### Cases by Reporting Area

Interactive bar chart showing current weekly reported cases.

---

### Incidence Rate Comparison

Bubble chart comparing:

- Population
- Incidence rate
- Current reported cases

Bubble size represents case counts.

---

### Top 10 States by Incidence Rate

Ranks states by incidence rate to highlight disease hotspots.

---

### Geographic Distribution

Interactive U.S. choropleth map displaying:

- Incidence Rate
- Current Week Cases
- Year-to-Date Cases

Color intensity corresponds to incidence rate.

---

### Total Reported Cases by State

Separate choropleth map displaying estimated cumulative cases by state.

This complements the incidence map by showing:

- Overall disease burden
- Large outbreaks
- Geographic concentration of cases

---

## Interactive Filters

Users can filter the dashboard by reporting area using the expandable filter panel.

---

## Cleaned Dataset

Displays the processed surveillance dataset used throughout the dashboard.

---

# Data Pipeline

```
Raw CDC Surveillance Data
            │
            ▼
      Data Cleaning
            │
            ▼
 Feature Engineering
    • State abbreviations
    • Incidence Rate
    • Population merge
            │
            ▼
 Processed CSV Dataset
            │
            ▼
 Interactive Streamlit Dashboard
```

---

# Data Cleaning

The cleaning pipeline performs:

- Removes unnecessary formatting
- Standardizes state names
- Merges population estimates
- Calculates incidence rates
- Converts state names to USPS abbreviations
- Prepares datasets for visualization

---

# Technologies Used

- Python
- Pandas
- Plotly Express
- Streamlit
- NumPy
- US package (state abbreviation lookup)

---

# Project Structure

```
CycloSpy/
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── raw/
│   │   ├── cyclosporiasis-cases.csv
│   │   ├── estimated-us-state-populations.csv
│   │   └── total_cases.csv
│   │
│   └── processed/
│       └── cyclospora_clean.csv
│
├── src/
│   └── clean_data.py
│
├── requirements.txt
│
└── README.md
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/CycloSpy.git

cd CycloSpy
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### macOS/Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Data Pipeline

Clean the raw data:

```bash
python src/clean_data.py
```

---

# Running the Dashboard

```bash
streamlit run dashboard/app.py
```

---

# Skills Demonstrated

This project demonstrates experience with:

- Data Cleaning
- ETL Pipelines
- Feature Engineering
- Data Visualization
- Dashboard Development
- Public Health Analytics
- Exploratory Data Analysis (EDA)
- Interactive Reporting
- Python Programming
- Git & GitHub
- Streamlit Deployment

---

# Future Improvements

Potential enhancements include:

- Time-series trend analysis
- Forecasting future case counts using machine learning
- Anomaly detection for unusual case spikes
- Automated CDC data ingestion
- SQL database backend
- Historical dashboard with multiple reporting years
- Downloadable reports
- Interactive county-level mapping
- Deployment to Streamlit Community Cloud

---

# Data Sources

- CDC National Notifiable Diseases Surveillance System (NNDSS)
- U.S. Census Bureau Population Estimates

---

# Disclaimer

This dashboard is intended for educational and portfolio purposes only.

The analyses presented here should not be used for clinical or public health decision-making without consulting official CDC surveillance reports.

---

# Author

**Megha Chandrashaker**

Applied & Computational Mathematics

Interested in:

- Data Science
- Public Health Analytics
- Machine Learning
- Data Engineering
- Business Intelligence

GitHub: *Add your GitHub profile here.*

LinkedIn: *Add your LinkedIn profile here.*