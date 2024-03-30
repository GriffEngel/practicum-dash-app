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

# ----------------------------- Total Enrollment ----------------------------- #
enrollment_data = {
    "Academic Year": ["2019-20", "2020-21", "2021-22", "2022-23", "2023-24"],
    "Total Enrollment": [1635, 2577, 2572, 3988, 3973],
}
df13 = pd.DataFrame(enrollment_data)

fig3 = go.Figure()

fig3.add_trace(
    go.Scatter(
        x=df13['Academic Year'],
        y=df13['Total Enrollment'],
        mode="lines+markers+text",
        marker=dict(
            size=14,
            symbol="circle",
        ),
        line=dict(width=3),
        textfont=dict(
            size=18,
        )
    )
)

fig3.update_layout(
    template='plotly',
    font_size=14,
    title="Total Students Using OERs",
    xaxis=dict(
        title="Academic Year"
    ),
    yaxis=dict(
        title="Number of Students"
    )
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
                dbc.Col(html.Div(dcc.Graph(figure=fig)), xs=12, sm=12, md=12, lg=6),
                dbc.Col(html.Div(dcc.Graph(figure=fig2)), xs=12, sm=12, md=12, lg=6),
            ],
        ),
        dbc.Row(
            [
                dbc.Col(html.Div(dcc.Graph(figure=fig3)), width=12),
            ]
        ),
        dbc.Row(
            [
                html.H5("Dashboard created by Griffin Engel"),
                dbc.Col([
                    html.A(
                    "GitHub",
                    href="https://github.com/GriffEngel"),
                ], width="auto"),
                dbc.Col([
                    html.A(
                    "Kaggle",
                    href="https://www.kaggle.com/griffinengel/code"),
                ], width="auto"),
                dbc.Col([
                    html.A(
                    "LinkedIn",
                    href="https://www.linkedin.com/in/griffin-engel-066b12224/"
                ),
                ], width="auto"),
                dbc.Col([
                    html.A(
                    "Full Portfolio",
                    href="https://griffengel.github.io/"
                ), 
                ], width="auto"),
                dbc.Col([
                    html.A(
                    "Tableau",
                    href="https://public.tableau.com/app/profile/griffin.engel/vizzes"
                ), 
                ], width="auto"),
                dbc.Col([
                    html.A(
                    "X/Twitter",
                    href="https://twitter.com/DataVizGriff"
                ), 
                ], width="auto"),
                
            ],
            className="flex text-center justify-content-center",
        ),
        dbc.Row(
            [
                html.Div(
                    [
                        "University of Iowa OER Report © 2024 by Griffin Engel is licensed under CC BY NC 4.0"
                    ],
                    className="text-center my-2",
                )
            ]
        ),
    ], 
    style={"width": "100vw"}
)
