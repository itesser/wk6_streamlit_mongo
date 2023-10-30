import pandas as pd
from pathlib import Path
from base import Base
from to_mongo import ToMongo
import re
import spacy

# pip install scikit-learn
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

import pickle  # used to save trained pipeline


# set folder directory
folder_dir = f"{Path(__file__).parents[0]}\\data"

# making sure we have the freshest dataset
Base().df.to_csv(f"{folder_dir}\\oracle_cards.csv", index=False)
print("saved new card data to csv file")


# update the database:
# ToMongo().drop_collection()
# print("Succesfully dropped all items in collection")

# ToMongo().upload_one_by_one()
# print("succesfully updated collection with new data")

# read in the dataframe from the csv

df = pd.read_csv(f"{folder_dir}\\oracle_cards.csv", low_memory=False)
print("created the DataFrame object")

## starting LLM

# drop null values and any empty strings

df.dropna(subset=["oracle_text"], axis=0, inplace=True)
df.drop(df.index[df["oracle_text"] == ""], inplace=True)
print("dropped all values that were either null or empty")

# use regex to remove all non-alpha-numeric values from the column:
df["oracle_text"] = [re.sub("[^0-9a-zA-Z]+", " ", i) for i in df.oracle_text]
print("regex process was successful")

# bringin in spaCy
# spaCy install for virtal env https://spacy.io/usage
nlp = spacy.load("en_core_web_md")
lemmas = []
for doc in df["oracle_text"]:
    lemmas.append(
        [
            token.lemma_.lower().strip()
            for token in nlp(str(doc))
            if (token.is_stop != True)
            and (token.is_punct != True)
            and (token.is_space != True)
            and (len(token) > 2)
        ]
    )

df["lemmas"] = lemmas

print("succesfully created lemma column in a dataframe object")

# save back over the csv with lemma included

df.to_csv(f"{folder_dir}\\oracle_cards.csv", index=False)

# #lemmmas does not like lists of lists, so we need to break up the column... unless we're doing a pipeline?
# def dummy_fun(doc):
#     return doc

pipe = make_pipeline(
    TfidfVectorizer(), NearestNeighbors(n_neighbors=12)  # default is 5
)

pipe.fit(df["lemmas"].astype(str))

pickle.dump(pipe, open(f"{folder_dir}\\pipe.pk", "wb"))

print("pickle file complete")
