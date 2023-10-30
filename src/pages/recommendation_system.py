import streamlit as st
import requests
import os
import sys
from PIL import Image
from pathlib import Path
from io import BytesIO


print(Path(__file__).parents)

sys.path.insert(0, os.path.join(Path(__file__).parents[1]))
from model import Model

m = Model()

st.title("recommender page")
card_name = st.text_input(
    "please enter the full name of the card you wish to see a recommendation for:"
)

if st.button("submit card"):
    try:
        st.image(m.image_return(card_name))
        img_list = m.recommended_cards(card_name)
        st.write(
            f"here is the {len(img_list)} cards that would be recommended  \n for a deck with {card_name} in it"
        )
        col1, col2, col3 = st.columns(3)
        col1.image(img_list[0:3])
        col2.image(img_list[3:6])
        col3.image(img_list[6:])
    except BaseException:
        st.error(" card name not accepted")
