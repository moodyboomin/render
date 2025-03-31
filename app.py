
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="World Cup Dashboard", layout="centered")
st.title("🌍 FIFA World Cup Winners Dashboard")

# Dataset
data = {
    "Country": ["Uruguay", "Italy", "Brazil", "Germany", "Argentina", "France", "England", "Spain"],
    "Wins": [2, 4, 5, 4, 3, 2, 1, 1],
    "Code": ["URY", "ITA", "BRA", "DEU", "ARG", "FRA", "GBR", "ESP"],
}

matches = {
    "Year": [
        1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966,
        1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998,
        2002, 2006, 2010, 2014, 2018, 2022
    ],
    "Winner": [
        "Uruguay", "Italy", "Italy", "Uruguay", "West Germany", "Brazil",
        "Brazil", "England", "Brazil", "West Germany", "Argentina",
        "Italy", "Argentina", "West Germany", "Brazil", "France",
        "Brazil", "Italy", "Spain", "Germany", "France", "Argentina"
    ],
    "Runner_Up": [
        "Argentina", "Czechoslovakia", "Hungary", "Brazil", "Hungary",
        "Sweden", "Czechoslovakia", "West Germany", "Italy", "Netherlands",
        "Netherlands", "West Germany", "West Germany", "Argentina", "Italy",
        "Brazil", "Germany", "France", "Netherlands", "Argentina",
        "Croatia", "France"
    ],
    "Score": [
        "4-2", "2-1 (a.e.t.)", "4-2", "2-1", "3-2", "5-2", "3-1", "4-2", "4-1", "2-1",
        "3-1", "3-1", "3-2", "1-0", "0-0 (3–2 p)", "3-0", "2-0", "1-1 (5–3 p)", "1-0",
        "1-0", "4-2", "3-3 (4–2 p)"
    ]
}

df = pd.DataFrame(data)
matches_df = pd.DataFrame(matches)

# Choropleth map of wins using globe style
st.subheader("🌍 Total World Cup Wins by Country (Choropleth Globe)")
fig = px.choropleth(
    df,
    locations="Code",
    color="Wins",
    hover_name="Country",
    color_continuous_scale=px.colors.sequential.Plasma
)

fig.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=True,
        projection_type='orthographic',
        projection_rotation=dict(lon=-30, lat=30),
        landcolor="white",
        oceancolor="lightblue",
        showocean=True
    )
)

st.plotly_chart(fig)

# Country-specific results
st.subheader("📅 World Cup Finals Participation")
selected_country = st.selectbox("Choose a country:", df["Country"])

filtered = matches_df[(matches_df["Winner"] == selected_country) | (matches_df["Runner_Up"] == selected_country)]

st.dataframe(filtered.reset_index(drop=True))
