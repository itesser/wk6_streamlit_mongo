import plotly.express as plt
import streamlit as st
import os
import sys
from pathlib import Path
import pandas as pd

filepath = os.path.join(Path(__file__).parents[1], "data/oracle_cards.csv")
df = pd.read_csv(filepath, low_memory=False)

vis_to_use = ["scatterplot", "histogram", "bar chart"]
type_vis = st.selectbox(
    "select the type of visualization you would like to see", options=vis_to_use
)

if type_vis == "scatterplot":
    answer_x = st.selectbox(
        "select a column to visualize on the x axis", options=sorted(list(df.columns))
    )
    answer_y = st.selectbox(
        "select a column to visualize on the y axis", options=sorted(list(df.columns))
    )
    if answer_x and answer_y:
        try:
            st.plotly_chart(
                plt.scatter(df, x=answer_x, y=answer_y, hover_data=["name"]),
                use_container_width=True,
            )
        except BaseException:
            print("error visualizing that combination of columns")

elif type_vis == "bar chart":
    answer_x = st.selectbox(
        "select a column to visualize on the x axis", options=sorted(list(df.columns))
    )
    answer_y = st.selectbox(
        "select a column to visualize on the y axis", options=sorted(list(df.columns))
    )
    if answer_x and answer_y:
        try:
            st.plotly_chart(
                plt.bar(df, x=answer_x, y=answer_y, hover_data=["name"]),
                use_container_width=True,
            )
        except BaseException:
            print("error visualizing that combination of columns")

elif type_vis == "histogram":
    answer = st.selectbox(
        "select a column to visualize", options=sorted(list(df.columns))
    )
    if answer:
        try:
            st.plotly_chart(
                plt.bar(df, x=answer, hover_data=["name"]), use_container_width=True
            )
        except BaseException:
            print("error visualizing that combination of columns")
