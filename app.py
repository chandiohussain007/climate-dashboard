import streamlit as st
import pandas as pd

from data_loader import load_data
from charts import trend_chart, gauge_chart, heatmap_chart

st.set_page_config(page_title="Climate Dashboard",layout="wide")

st.title("🌍 Global Climate Analytics Dashboard")

df = load_data()

# ---- FILTER ----
year_range = st.slider(
    "Select Year Range",
    int(df.Year.min()),
    int(df.Year.max()),
    (1900,2023)
)

filtered = df[(df.Year>=year_range[0])&(df.Year<=year_range[1])]

# ---- METRIC CARDS ----
c1,c2,c3 = st.columns(3)

c1.metric(
    "Latest Temperature",
    round(filtered.Temp_Anomaly.iloc[-1],2)
)

c2.metric(
    "Average Last 10 Years",
    round(filtered.Temp_Anomaly.tail(10).mean(),2)
)

c3.metric(
    "Maximum Recorded",
    round(filtered.Temp_Anomaly.max(),2)
)

# ---- GAUGE + HEATMAP ----
col1,col2 = st.columns(2)

col1.plotly_chart(
    gauge_chart(filtered.Temp_Anomaly.iloc[-1]),
    use_container_width=True
)

col2.plotly_chart(
    heatmap_chart(filtered),
    use_container_width=True
)

# ---- TREND GRAPH ----
st.plotly_chart(
    trend_chart(filtered),
    use_container_width=True
)

# ---- TABLE ----
top10 = filtered.sort_values(
    "Temp_Anomaly",
    ascending=False
).head(10)

st.subheader("🔥 Top 10 Hottest Years")

st.dataframe(
    top10.style.background_gradient(cmap="Reds")
)