import streamlit as st
import pandas as pd


st.header("Welcome to the Online Digitalvb Demo")
st.subheader("Daroda Toll Satff Details")
st.write("You can use this demo to explore the features of DigitalVB.") 

dataset = pd.read_excel("List_for_LOGIN_IDs.xlsx")

st.dataframe(dataset)