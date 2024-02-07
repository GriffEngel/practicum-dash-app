from dash import html
import pandas as pd
import plotly.express as px

df = pd.read_csv("./Cleaned_Datasets/1fall_2019.csv")
df2 = pd.read_csv("./Cleaned_Datasets/1spring_2020.csv")
df3 = pd.read_csv("./Cleaned_Datasets/2summer_2020.csv")
df4 = pd.read_csv("./Cleaned_Datasets/3fall_2020.csv")
df5 = pd.read_csv("./Cleaned_Datasets/3spring_2021.csv")
df6 = pd.read_csv("./Cleaned_Datasets/4fall_2021.csv")


layout = (
    html.Div(
        [
            html.H1("OpenHawks OER Report", className="fs-1"),
            html.P(
                "Click on the corresponding link to see cost savings data for each academic year"
            ),
        ],
        className="text-center min-vw-100",
    ),
)
html.Div([])
