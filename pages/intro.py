from dash import html, dcc, callback, Output, Input
import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

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
    ),
    yaxis=dict(
        range=[0, 600000],
        title="Cost Savings ($)",
    ),
)
fig.add_annotation(
    x=2.5,
    y=400000,
    text="55% increase",
    arrowhead=1,
    font=dict(size=12),
    ax=-75,
    ay=-15,
    arrowwidth=2,
)

fig.add_annotation(
    x=3.85,
    y=400000,
    text="143% increase since <br> the 2019-20 academic year",
    font=dict(size=12),
    arrowhead=1,
    arrowwidth=2,
    ax=-50,
    ay=100,
)

fig.add_annotation(
    x=1,
    y=165000,
    arrowhead=1,
    arrowwidth=2,
    ax=85,
    ay=2,
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
            size=14,
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
                html.H1(
                    "University of Iowa OER Report",
                    className="fs-1 shadow-sm p-3 mb-2 bg-body-secondary rounded text-center",
                ),
                html.P(
                    "Please select the appropriate link to access the cost savings data for each academic year.",
                    className="text-center text-primary",
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
            src=("assets/image.png"),
            height=600,
            style={"width": "68vw", "display": "block", "margin": "auto"},
            className="mb-4 mx-auto",
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
                        "University of Iowa OER Report © 2024 by Griffin Engel is licensed under CC BY-NC 4.0"
                    ],
                    className="text-center my-2",
                )
            ]
        ),
    ],
)
