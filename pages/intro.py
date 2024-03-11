from dash import html, dcc, callback, Output, Input, State
import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc


# *========== Keep for Later if Needed ============
# df = pd.read_csv("./Cleaned_Datasets/1fall_2019.csv")
# df2 = pd.read_csv("./Cleaned_Datasets/1spring_2020.csv")
# df3 = pd.read_csv("./Cleaned_Datasets/2summer_2020.csv")
# df4 = pd.read_csv("./Cleaned_Datasets/3fall_2020.csv")
# df5 = pd.read_csv("./Cleaned_Datasets/3spring_2021.csv")
# df6 = pd.read_csv("./Cleaned_Datasets/4fall_2021.csv")
# df7 = pd.read_csv("./Cleaned_Datasets/4spring_2022.csv")
# df8 = pd.read_csv("./Cleaned_Datasets/5fall_2022.csv")
# df9 = pd.read_csv("./Cleaned_Datasets/5spring_2023.csv")
# df10 = pd.concat([df,df2,df3,df4,df5,df6,df7,df8,df9])

# ---------------------------------------------------------------------------- #
#                                    Graphs                                    #
# ---------------------------------------------------------------------------- #
# ------------------------- Total Cost Savings graph ------------------------- #
data = {
    "Academic Year": ["2019-20", "2020-21", "2021-22", "2022-23", "2023-24"],
    "Total Cost Savings ($)": [191197, 301354, 300770, 466357, 464603],
}
df11 = pd.DataFrame(data)

text_labels1 = [191197, 301354, 300770, 466357, 464603]

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=df11["Academic Year"],
        y=df11["Total Cost Savings ($)"],
        mode="lines+markers+text",
        marker=dict(
            size=14,
            symbol="circle",
        ),
        line=dict(width=3),
        text=text_labels1,
        texttemplate="%{text:$,}",
        textposition=[
            "bottom right",
            "top left",
            "bottom right",
            "top left",
            "bottom center",
        ],
        textfont=dict(
            size=10,
        ),
    ),
)
fig.update_layout(
    title="Total Cost Savings by Academic Year",
    font_size=14,
    template="plotly",
    xaxis=dict(
        title="Academic Year",
        tickmode="auto",
        dtick=1,
        ticklen=10,
        tickwidth=2,
        tickcolor="#000000",
    ),
    yaxis=dict(
        range=[0, 600000],
        title="Cost Savings ($)",
        tickmode="auto",
        dtick=1,
        ticklen=10,
        tickwidth=2,
        tickcolor="#000000",
    ),
)
fig.add_annotation(
    x=2.5,
    y=400000,
    text="55% increase",
    arrowhead=1,
    font=dict(size=14),
    ax=-75,
    ay=-15,
    arrowwidth=2,
)

# ------------------ Number of Departments using OERs Graph ------------------ #
dept_data = {
    "Academic Year": ["2019-20", "2020-21", "2021-22", "2022-23", "2023-24"],
    "Number of Departments Using OERs": [15, 11, 19, 25, 26],
}
df12 = pd.DataFrame(dept_data)

fig2 = go.Figure()

fig2.add_trace(
    go.Scatter(
        x=df12["Academic Year"],
        y=df12["Number of Departments Using OERs"],
        mode="lines+markers+text",
        marker=dict(
            size=12,
            symbol="circle",
        ),
        line=dict(width=3),
        textfont=dict(
            size=18,
        ),
    ),
)
fig2.update_layout(
    font_size=14,
    template="plotly",
    title="Number of Departments reporting OER Usage",
    xaxis=dict(
        title="Academic Year",
    ),
    yaxis=dict(
        title="Number of Departments",
        range=[0, 30],
    ),
)

# ---------------------------------------------------------------------------- #
#                                    Layout                                    #
# ---------------------------------------------------------------------------- #
layout = dbc.Container(
    [
        html.Div(
            [
                html.H1("University of Iowa OER Report", className="fs-1 text-center"),
                html.P(
                    "Click on the corresponding link to see cost savings data for each academic year",
                    className="text-center",
                ),
            ],
        ),
        dbc.Row(
            [
                dbc.Col([html.Div([dcc.Graph(figure=fig)])]),
                dbc.Col([html.Div([dcc.Graph(figure=fig2)])]),
            ]
        ),
        html.Img(
            src=("assets/Screenshot 2024-02-26 163212.png"),
            height=600,
            style={"width": "68vw"},
            className="mb-2",
        ),
        dbc.Container(
            [
                html.H5("Dashboard created by Griffin Engel"),
                html.A(
                    "LinkedIn",
                    href="https://www.linkedin.com/in/griffin-engel-066b12224/",
                    className="mx-3",
                ),
                html.A(
                    "Full Portfolio",
                    href="https://www.datascienceportfol.io/griffinengel",
                ),
            ],
            className="flex text-center",
        ),
        dbc.Container(
            [
                html.Div(
                    [
                        "University of Iowa OER Report © 2024 by Griffin Engel is licensed under CC BY-NC-ND 4.0"
                    ],
                    className="text-center my-2",
                )
            ]
        ),
    ]
)
