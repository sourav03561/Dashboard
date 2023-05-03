import pandas as pd
import streamlit as st
import numpy as np
import plotly_express as px


@st.cache_resource
def load_data(file):
    return pd.read_csv(file)

def analysis(df):
    st.write("Data Frame")
    st.dataframe(df)
    st.write("Data Describe")
    st.dataframe(df.describe())
    st.write("Data Correlation")
    st.dataframe(df.corr())
    st.write("Data Rank")
    st.dataframe(df.rank())

def visualizaion(chart_type,df,x_column,y_column):

    if chart_type == 'Bar':
        st.header("Bar chart")
        fig = px.bar(df,x=x_column,y=y_column,color=df.columns[1])
        st.plotly_chart(fig)
    if chart_type == 'Line':
        st.header("Line chart")
        fig = px.line(df,x=x_column,y=y_column,color=df.columns[1])
        st.plotly_chart(fig)
    if chart_type == 'Scatter':
        st.header("Scatter chart")
        fig = px.scatter(df,x=x_column,y=y_column,color=df.columns[1])
        st.plotly_chart(fig)
    if chart_type == 'Histogram':
        st.header("Histogram chart")
        fig = px.histogram(df,x=x_column,y=y_column,color=df.columns[1])
        st.plotly_chart(fig)
    if chart_type == 'pie':
        st.header("Pie chart")
        fig = px.pie(df,names = x_column,values = y_column)
        st.plotly_chart(fig)
    
def main():
    st.image("pandas.png")
   
    st.header("Data Analysis and Data Visualization")
    file = st.sidebar.file_uploader("Upload a data set in CSV or EXCEL format", type=["csv","excel"])
    
    if file is not None:
        df = load_data(file)
        #st.dataframe(df)
        option = st.sidebar.radio(
        "Choose one of them",
        ("Data Analysis", "Data Visualization")
        )
        if option == "Data Analysis":
            
            analysis(df)
        
        if option == "Data Visualization":
            st.sidebar.title("Chart Options")
            
            chart_type = st.sidebar.selectbox("Select a chart type",["Bar","Line","Scatter","Histogram","pie"])

            x_column = st.sidebar.selectbox("Select the X column", df.columns)

            y_column = st.sidebar.selectbox("Select the Y column", df.columns)

            visualizaion(chart_type,df,x_column,y_column)

if __name__ == "__main__":
    main()