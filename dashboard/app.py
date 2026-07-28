import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import us


# -----------------------
# Page Configuration
# -----------------------

st.set_page_config(
    page_title="CycloSpy Dashboard",
    page_icon="🦠",
    layout="wide"
)


# -----------------------
# Load Data
# -----------------------

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "processed" / "cyclospora_clean.csv"

TOTAL_CASES_PATH = (
    BASE_DIR /
    "data" /
    "raw" /
    "total_cases.csv"
)


@st.cache_data
def load_data():
    incidence_df = pd.read_csv(DATA_PATH)

    total_cases_df = pd.read_csv(TOTAL_CASES_PATH)

    return incidence_df, total_cases_df


df, total_cases_df = load_data()
filtered_df = df.copy()


def convert_state(state):
    result = us.states.lookup(str(state).strip())
    return result.abbr if result else None


df["State"] = df["State"].apply(convert_state)

def convert_case_range(value):

    low, high = value.split(" to ")

    return (int(low) + int(high)) / 2


total_cases_df["Estimated Cases"] = (
    total_cases_df["Number of Sick People"]
    .apply(convert_case_range)
)

total_cases_df["State"] = total_cases_df["Location"].apply(convert_state)


# -----------------------
# Title
# -----------------------

st.title("🦠 CycloSpy: Cyclosporiasis Surveillance Dashboard")

st.markdown(
    """
    Interactive analysis of reported cyclosporiasis cases 
    using public health surveillance data.
    """
)


# -----------------------
# Executive Summary
# -----------------------

st.header("Executive Summary")

st.markdown("""
### Key Findings

This dashboard analyzes reported cyclosporiasis cases across U.S. states 
and summarizes current case trends, geographic distribution, and incidence rates.

**Major insights:**

- Michigan currently reports the highest incidence rate among tracked states, 
  indicating a higher number of cases relative to its population size.

- Ohio and Colorado also show elevated incidence rates compared with many other states.

- Several states report zero or very low incidence rates, suggesting limited reported 
  cases during the current reporting period.

- Incidence rate provides additional context beyond total cases because it adjusts 
  for differences in state population sizes.

### How to Interpret This Dashboard

- **Current Week Cases:** The number of newly reported cases during the latest reporting period.
- **Cumulative YTD Cases:** Total cases reported since the beginning of the year.
- **Incidence Rate:** Cases per 100,000 people, allowing fair comparison between states.
- **Geographic Map:** Darker areas represent states with higher incidence rates.
""")


# -----------------------
# KPI Metrics
# -----------------------

total_cases = filtered_df["Current week"].sum()

avg_incidence = filtered_df["Incidence Rate"].mean()

highest_state = (
    filtered_df
    .sort_values("Incidence Rate", ascending=False)
    .iloc[0]["Reporting Area"]
)


col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        "Total Cases",
        f"{total_cases:,}"
    )


with col2:
    st.metric(
        "Average Incidence Rate",
        f"{avg_incidence:.2f}"
    )


with col3:
    st.metric(
        "Highest Incidence Area",
        highest_state
    )


# -----------------------
# Charts
# -----------------------

st.header("Cases by Reporting Area")


# -----------------------
# Local Filters
# -----------------------

with st.expander("Filter Options"):

    states = st.multiselect(
        "Select Reporting Areas",
        options=df["Reporting Area"].unique(),
        default=df["Reporting Area"].unique()
    )


filtered_df = df[
    df["Reporting Area"].isin(states)
]


fig_cases = px.bar(
    filtered_df,
    x="Reporting Area",
    y="Current week",
    title="Current Week Cases",
    labels={
        "Current week": "Cases"
    }
)


st.plotly_chart(
    fig_cases,
    use_container_width=True
)



st.header("Incidence Rate Comparison")


fig_rate = px.scatter(
    filtered_df,
    x="Estimated Population",
    y="Incidence Rate",
    size="Current week",
    hover_name="Reporting Area",
    title="Incidence Rate vs Population"
)


st.plotly_chart(
    fig_rate,
    use_container_width=True
)


top_states = (
    df.sort_values(
        "Incidence Rate",
        ascending=False
    )
    .head(10)
)

fig = px.bar(
    top_states,
    x="Incidence Rate",
    y="Reporting Area",
    orientation="h",
    title="Top 10 States by Cyclosporiasis Incidence Rate"
)

st.plotly_chart(fig, use_container_width=True)


# ----------------------------
# Choropleth Map
# ----------------------------

st.header("Geographic Distribution")


fig_map = px.choropleth(
    filtered_df,
    locations="State",
    locationmode="USA-states",
    color="Incidence Rate",
    scope="usa",
    hover_name="Reporting Area",
    hover_data={
        "Current week": True,
        "Cum YTD 2026 †": True,
        "Incidence Rate": True
    },
    color_continuous_scale="Blues",
    title="Cyclosporiasis Incidence Rate by State"
)


fig_map.update_coloraxes(
    colorbar_title="Cases per 100,000",
    cmin=0,
    cmax=5
)


st.plotly_chart(
    fig_map,
    use_container_width=True
)


st.header("Total Reported Cases by State")


fig_total_cases = px.choropleth(
    total_cases_df,
    locations="State",
    locationmode="USA-states",
    color="Estimated Cases",
    scope="usa",
    hover_name="Location",
    hover_data={
        "Number of Sick People": True
    },
    color_continuous_scale="YlGnBu",
    title="Estimated Number of Cyclosporiasis Cases by State"
)


fig_total_cases.update_coloraxes(
    colorbar_title="Estimated Cases",
    cmin=0,
    cmax=500
)


st.plotly_chart(
    fig_total_cases,
    use_container_width=True
)


# -----------------------
# Data Table
# -----------------------

st.header("Cleaned Dataset")

sorted_df = df.sort_values(
    by="Incidence Rate",
    ascending=False
)

sorted_df["Incidence Rate"] = sorted_df["Incidence Rate"].round(2)


st.markdown(
    sorted_df.style
    .format({"Incidence Rate": "{:.2f}"})
    .hide(axis="index")
    .to_html(),
    unsafe_allow_html=True
)