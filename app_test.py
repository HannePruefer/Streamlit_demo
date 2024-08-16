
import streamlit as st
import pandas as pd

st.title("Welcome to my Streamlit test")

st.header("DATA", divider = True)

data = pd.read_csv("mushroom_competition.csv")
st.dataframe(data)

st.header("CHART", divider = True)
st.bar_chart (data, x = "bruises", y = "poisonous")

st.header("TEXT", divider = True)
st.write("are you interested in mushrooms?")
if st.button("yes"):
    st.write("Good choice")
