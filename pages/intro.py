from dash import html, dcc
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
    "Academic Year": ["2019-20", "2020-21", "2021-22", "2022-23"],
    "Total Cost Savings ($)": [191196.90, 301354.38, 300769.68, 466356.72],
}
df11 = pd.DataFrame(data)

text_labels1 = [191196.90, 301354.38, 300769.68, 466356.72]

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=df11["Academic Year"],
        y=df11["Total Cost Savings ($)"],
        mode="lines+markers+text",
        marker=dict(
            size=12,
            color="#005CFE",
            symbol="circle",
        ),
        line=dict(color="darkgray", width=3),
        text=text_labels1,
        texttemplate="%{text:$,.2f}",
        textposition=["bottom right", "bottom right", "bottom right", "top left"],
        textfont=dict(
            color="#005CFE",
            size=13,
        ),
    ),
)
fig.update_layout(
    title="Total Cost Savings by Academic Year",
    plot_bgcolor="#F2F2F2",
    font_size=14,
)
fig.update_xaxes(title="Academic Year", gridcolor="lightgray")
fig.update_yaxes(
    range=[0, 600000],
    title="Cost Savings ($)",
    gridcolor="lightgray",
)
fig.add_annotation(
    x=2.5,
    y=400000,
    text="55% increase",
    arrowhead=1,
    font=dict(family="Balto, sans-serif", size=14, color="#005CFE"),
    ax=-75,
    ay=-15,
    arrowwidth=2,
    arrowcolor="#005CFE",
)

# ------------------ Number of Departments using OERs Graph ------------------ #
dept_data = {
    "Academic Year": ["2019-20", "2020-21", "2021-22", "2022-23"],
    "Number of Departments Using OERs": [15, 11, 19, 25],
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
            color="#005CFE",
            symbol="circle",
        ),
        line=dict(color="darkgray", width=3),
        textfont=dict(
            color="#005CFE",
            size=18,
        ),
    ),
)
fig2.update_layout(
    plot_bgcolor="#F2F2F2",
    font_size=14,
    title="Number of Departments reporting OER Usage",
    xaxis=dict(title="Academic Year", gridcolor="lightgray"),
    yaxis=dict(title="Number of Departments", gridcolor="lightgray", range=[0, 30]),
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
            src=("assets/Screenshot 2024-02-19 154257.png"),
            height=600,
            style={"width": "68vw"},
        ),
    ]
)
