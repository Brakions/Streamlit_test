import streamlit as st
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from client import lifexp,lifexpe,lifexpa,lifexpaf,lifexpo

def main():
    menu = ["Life Expectancy","Dataset"]
    choice = st.sidebar.selectbox("Menu",menu)

    st.title("Test")

    if choice == "Life Expectancy":
            st.subheader("Life Expectancy")
            if st.checkbox("America"):
                st.write(lifexp())
            if st.checkbox("Europa"):
                st.write(lifexpe())
            if st.checkbox("Asia"):
                st.write(lifexpa())
            if st.checkbox("Africa"):
                st.write(lifexpaf())
            if st.checkbox("Oceania"):
                st.write(lifexpo())
    else :
            
            st.subheader("Dataset")
            if st.checkbox("Dataset"):
                df=pd.read_csv("life_expectancy.csv")
                st.dataframe(df)


if __name__ =="__main__":
    main()
