from dash import html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc


df = pd.read_csv("./Cleaned_Datasets/3fall_2020.csv")
df2 = pd.read_csv("./Cleaned_Datasets/3spring_2021.csv")
df3 = pd.concat([df, df2])
total = df3["Cost Savings ($)"].sum()

fig1 = px.histogram(
    df3,
    x="Department",
    y="Cost Savings ($)",
)
fig1.update_layout(autosize=True)
fig1.update_xaxes(categoryorder="total descending")


layout = dbc.Container(
    [
        dbc.Row(
            [
                # ! Extra Div needs to be here in order for dcc.Graph style to work
                html.Div(
                    [
                        html.H3(
                            f"The University of Iowa saved students ${total:,.2f} in textbook costs in 20-21",
                            className="text-center fs-5",
                        ),
                        dcc.Graph(figure=fig1, style={"width": "72vw"}),
                        dcc.Dropdown(
                            id="category-dropdown20-21",
                            options=[
                                {"label": i, "value": i}
                                for i in df3["Department"].unique()
                            ],
                            value="Economics",
                            clearable=False,
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dcc.Graph(
                            id="category-bar-graph20-21",
                            style={"height": "63vh"},
                        )
                    ]
                ),
            ]
        ),
    ],
    style={"maxWidth": "75%"},
)


@callback(
    Output("category-bar-graph20-21", "figure"),
    Input("category-dropdown20-21", "value"),
)
def update_graph(selected_category):
    filtered_df = df3[df3["Department"] == selected_category]
    fig = px.bar(
        filtered_df,
        x="Course #",
        y="Cost Savings ($)",
        text="Cost Savings ($)",
        title="Breakdown by Individual Course",
        height=500,
    )
    fig.update_layout(
        autosize=True,
        plot_bgcolor="#F2F2F2",
    )
    fig.update_xaxes(categoryorder="total descending")
    fig.update_traces(
        texttemplate="%{text:$,.0f}",
        textposition="outside",
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False, showticklabels=False)
    return fig
