from dash import html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc


df = pd.read_csv("./Cleaned_Datasets/4fall_2021.csv")
df2 = pd.read_csv("./Cleaned_Datasets/4spring_2022.csv")
df3 = pd.concat([df, df2])
total = df3["Cost Savings ($)"].sum()

fig1 = px.histogram(
    df3,
    x="Department",
    y="Cost Savings ($)",
    title="2021-2022 Academic Year by Category",
)
fig1.update_xaxes(categoryorder="total descending")


layout = dbc.Container(
    [
        dbc.Row(
            [
                html.Div(
                    [
                        html.H3(
                            f"The University of Iowa saved students ${total:,.2f} in textbook costs in 21-22",
                            className="text-center fs-5",
                        ),
                        dcc.Graph(figure=fig1),
                        dcc.Dropdown(
                            id="category-dropdown21-22",
                            options=[
                                {"label": i, "value": i}
                                for i in df3["Department"].unique()
                            ],
                            value="Economics",
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        dcc.Graph(
                                            id="category-bar-graph21-22",
                                        )
                                    ]
                                )
                            ]
                        ),
                    ]
                ),
            ]
        ),
    ],
    style={"maxWidth": "75%"},
)


@callback(
    Output("category-bar-graph21-22", "figure"),
    Input("category-dropdown21-22", "value"),
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
    fig.update_xaxes(categoryorder="total descending")
    fig.update_traces(
        texttemplate="%{text:$,.0f}",
        textposition="outside",
    )
    fig.update_layout(autosize=True)
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False, showticklabels=False)
    return fig
