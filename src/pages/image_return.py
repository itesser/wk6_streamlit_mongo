import streamlit as st
import requests
import os
import sys
from PIL import Image
from pathlib import Path
from io import BytesIO

# but we still need to import to_mongo
# create the filepath to the system where the main folder for the application lives

print(Path(__file__).parents)

# parents[0] = current folder
# parents[1] = one level hgher, ie: src directory

sys.path.insert(0, os.path.join(Path(__file__).parents[1]))
from to_mongo import ToMongo

# </header>
# <body>

st.title("image return page")

# create an instance of our Mongo class
c = ToMongo()

answer = st.text_input("enter a card name", value="Static Orb")

# transform it into a query
card = list(c.cards.find({"name": answer}))[0]["image_uris"]["normal"]
st.image(Image.open(BytesIO(requests.get(card).content)))
