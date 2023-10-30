import streamlit as st

# close out of python terminal with Ctrl-C

# streamlit run front_page.py

st.title("bonfire-129 mtg tracer application")
st.text(
    "my first application that utilizes pandas, streamlit, sklearn, spacy, mongodb, plotly and python to create a mtg recommendation system"
)

st.header("here are the different pages of my application")
st.subheader("image return")
st.text("")

st.subheader("summary page")
st.text(
    "summary page explaining the inner workings of my application and the why behind decisions we made"
)

st.subheader("query")
st.text(
    "a page that allows a user to enter a card name and qeries the database in mongo for all information matching that card name (card names must be exact)"
)

st.subheader("recommender")
st.text(
    "recommendation system that we will build that will allow users to se recommended cards"
)

st.subheader("Vis")
st.text("vis: ability to create visualizations using plotly")
