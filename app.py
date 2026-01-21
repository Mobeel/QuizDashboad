import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(layout="wide", page_title="Global Development Dashboard")
st.title("📊 Global Infrastructure & Economic Report")

# 2. Load Dataset
@st.cache_data
def load_data():
    df = pd.read_csv('agriRuralDevelopment.csv')
    return df

df = load_data()

# 3. Interaction Sidebar
st.sidebar.header("Interactive Filters")
selected_year = st.sidebar.slider("Select Year", 1990, 2018,2020)

filtered_df = df[df['year'] == selected_year].dropna(subset=['Access to electricity (% of population)', 'GDP per capita (current US$)'])

# 4. Layout: Grid with fixed height to prevent scrolling
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# Humne height=300 rakha hai taake 4 graphs screen par fit aayein
with col1:
    fig1 = px.choropleth(filtered_df, locations="Country Code", color="Access to electricity (% of population)",
                         color_continuous_scale="Blues", height=200)
    fig1.update_layout(margin=dict(l=0, r=0, t=30, b=0)) # Margin kam kiya
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    trend_df = df.groupby('year')['Access to electricity (% of population)'].mean().reset_index()
    fig2 = px.line(trend_df, x='year', y='Access to electricity (% of population)', 
                   color_discrete_sequence=['darkorange'], height=200)
    fig2.update_layout(margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig2, use_container_width=True)

with col3:
    fig3 = px.scatter(filtered_df, x="GDP per capita (current US$)", y="Access to electricity (% of population)",
                      log_x=True, color_discrete_sequence=['steelblue'], height=200)
    fig3.update_layout(margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    counts = filtered_df[['Access to electricity (% of population)', 'GDP per capita (current US$)']].count()
    fig4 = px.bar(x=counts.index, y=counts.values, color_discrete_sequence=['#9ECAE1'], height=200)
    fig4.update_layout(margin=dict(l=0, r=0, t=30, b=0))

    st.plotly_chart(fig4, use_container_width=True)



