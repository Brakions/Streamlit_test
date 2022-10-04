import streamlit as st
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from client import lifexp

def main():
    menu = ["Life Expectancy","Dataset"]
    choice = st.sidebar.selectbox("Menu",menu)

    st.title("Test")

    if choice == "Life Expectancy":
            st.subheader("Life Expectancy")
            if st.checkbox("Life Expectancy"):
                st.write(lifexp())
    else :
            
            st.subheader("Dataset")
            if st.checkbox("Dataset"):
                df=pd.read_csv("life_expectancy.csv")
                st.dataframe(df)


if __name__ =="__main__":
    main()
