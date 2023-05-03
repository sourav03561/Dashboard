import pandas as pd
import streamlit as st
import numpy as np



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
        
        

if __name__ == "__main__":
    main()
