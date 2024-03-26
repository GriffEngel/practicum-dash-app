from dash import html, dash_table
import pandas as pd
import dash_bootstrap_components as dbc
from src.app import app

df = pd.read_csv("./Cleaned_Datasets/1fall_2019.csv")
df2 = pd.read_csv("./Cleaned_Datasets/1spring_2020.csv")
df3 = pd.read_csv("./Cleaned_Datasets/3fall_2020.csv")
df4 = pd.read_csv("./Cleaned_Datasets/3spring_2021.csv")
df5 = pd.read_csv("./Cleaned_Datasets/4fall_2021.csv")
df6 = pd.read_csv("./Cleaned_Datasets/4spring_2022.csv")
df7 = pd.read_csv("./Cleaned_Datasets/5fall_2022.csv")
df8 = pd.read_csv("./Cleaned_Datasets/5spring_2023.csv")
df9 = pd.read_csv("Cleaned_Datasets/6fall_2023.csv")
df10 = pd.read_csv("Cleaned_Datasets/6spring_2024.csv")
df19_20 = pd.concat([df, df2])
df20_21 = pd.concat([df3, df4])
df21_22 = pd.concat([df5, df6])
df22_23 = pd.concat([df7, df8])
df23_24 = pd.concat([df9, df10])
# df10 = pd.concat([df,df2,df3,df4,df5,df6,df7,df8,df9])

page_size = 10

app.layout = dbc.Container(
    [
        dbc.Col(
            [
                html.H1(
                    "Appendix",
                    className="fs-1 shadow-sm p-3 mb-2 bg-body-secondary rounded text-center",
                ),
                html.P(
                    "Raw data used to make this dashboard",
                    className="text-center text-primary",
                ),
                html.Br(),
                html.H3("2019-20 Academic Year"),
                dash_table.DataTable(
                    df19_20.to_dict("records"),
                    [{"name": i, "id": i} for i in df19_20.columns],
                    style_table={"overflowX": "scroll"},
                    page_size=page_size,
                ),
                html.H3("2020-21 Academic Year"),
                dash_table.DataTable(
                    df20_21.to_dict("records"),
                    [{"name": i, "id": i} for i in df20_21.columns],
                    style_table={"overflowX": "scroll"},
                    page_size=page_size,
                ),
                html.H3("2021-22 Academic Year"),
                dash_table.DataTable(
                    df21_22.to_dict("records"),
                    [{"name": i, "id": i} for i in df21_22.columns],
                    style_table={"overflowX": "scroll"},
                    page_size=page_size,
                ),
                html.H3("2022-23 Academic Year"),
                dash_table.DataTable(
                    df22_23.to_dict("records"),
                    [{"name": i, "id": i} for i in df22_23.columns],
                    style_table={"overflowX": "scroll"},
                    page_size=page_size,
                ),
                html.H3("2023-24 Academic Year"),
                dash_table.DataTable(
                    df23_24.to_dict("records"),
                    [{"name": i, "id": i} for i in df23_24.columns],
                    style_table={"overflowX": "scroll"},
                    page_size=page_size,
                ),
            ]
        )
    ],
    class_name="flex flex-column justify-content-center max-vw-75",
)
