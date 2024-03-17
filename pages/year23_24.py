from dash import html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc


df = pd.read_csv("./Cleaned_Datasets/6fall_2023.csv")
df2 = pd.read_csv("./Cleaned_Datasets/6Spring_2024.csv")
df3 = pd.concat([df, df2])
total = df3["Cost Savings ($)"].sum()

aggregated_df = df3.groupby("Department")["Cost Savings ($)"].sum().reset_index()
# options_list = {"label": i, "value": i} for i in df3["Department "].unique()

fig1 = go.Figure()

fig1.add_trace(
    go.Bar(
        x=aggregated_df["Department"],
        y=aggregated_df["Cost Savings ($)"],
    )
)

fig1.update_layout(
    title="Cost Savings by Department",
    template="plotly",
    font_size=13,
    xaxis=dict(title="Department", categoryorder="total descending", showgrid=False),
    yaxis=dict(title="Cost Savings", tickprefix="$", tickformat=",.0f"),
)


layout = dbc.Container(
    [
        dbc.Row(
            [
                # ! Extra Div needs to be here in order for dcc.graph style to work
                html.Div(
                    [
                        html.H3(
                            f"The University of Iowa saved students ${total:,.2f} in textbook costs in 2023-24",
                            className="text-center fs-5",
                        ),
                        dcc.Graph(figure=fig1, style={"width": "80vw"}),
                        dcc.Dropdown(
                            id="category-dropdown23-24",
                            options=[
                                {"label": i, "value": i}
                                for i in df3["Department"].unique()
                            ],
                            value="Management",
                            clearable=False,
                            className="shadow-sm p-3 mb-2 mt-2 rounded border border-info border-1",
                        ),
                    ],
                ),
                dbc.Row(
                    [
                        dcc.Graph(
                            id="category-bar-graph23-24",
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
    Output("category-bar-graph23-24", "figure"),
    Input("category-dropdown23-24", "value"),
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
        template="plotly",
        font_size=13,
        xaxis=dict(categoryorder="total descending", showgrid=False),
        yaxis=dict(showgrid=False, showticklabels=False),
    )
    fig.update_traces(
        texttemplate="%{text:$,.0f}",
        textposition="outside",
    )
    return fig
