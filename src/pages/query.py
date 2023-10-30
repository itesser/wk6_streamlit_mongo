from pathlib import Path
import streamlit as st
import sys
import os

sys.path.insert(0, os.path.join(Path(__file__).parents[1]))

from to_mongo import ToMongo

c = ToMongo()

st.header("query page")
st.write(
    """
         this page will search our database for any card name! 
         
         spelling and capitalization must be exact!
         """
)
# now we query the database
# and display the information gathered in a usable format

# how can i use this in the future?
# when a user wants to search for information, we don't have to reference a local file anymore, we can pnp a database instead and let the user query that database

try:
    answer = st.text_input("Enter a card", value="Saproling Burst")
    st.write(list(c.cards.find({"name": answer})))
except:
    st.error("invalid card name, please try again")
