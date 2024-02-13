from dash import html, dcc, callback, Output, Input
import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc


df = pd.read_csv("./Cleaned_Datasets/1fall_2019.csv")
df2 = pd.read_csv("./Cleaned_Datasets/1spring_2020.csv")
df3 = pd.concat([df, df2])
total = df3["Cost Savings ($)"].sum()

aggregated_df = df3.groupby("Department")["Cost Savings ($)"].sum().reset_index()

# Create the bar chart
fig1 = go.Figure()

fig1.add_trace(
    go.Bar(
        x=aggregated_df["Department"],
        y=aggregated_df["Cost Savings ($)"],
        marker=dict(color="blue"),
    )
)

fig1.update_layout(
    title="Cost Savings by Department",
    xaxis_title="Department",
    yaxis_title="Cost Savings",
    yaxis_tickprefix="$",
    yaxis_tickformat=",.0f",
    plot_bgcolor="#F2F2F2",
)
fig1.update_xaxes(categoryorder="total descending", showgrid=False)
fig1.update_yaxes(gridcolor="lightgray")


# fig1 = px.histogram(
#     df3,
#     x="Department",
#     y="Cost Savings ($)",
#     title="2019-2020 Academic Year by Category",
# )
# fig1.update_xaxes(categoryorder="total descending")


layout = dbc.Container(
    [
        dbc.Row(
            [
                html.Div(
                    [
                        html.H3(
                            f"The University of Iowa saved students ${total:,.2f} in textbook costs in 19-20",
                            className="text-center fs-5",
                        ),
                        dcc.Graph(figure=fig1, style={"width": "68vw"}),
                        dcc.Dropdown(
                            id="category-dropdown19-20",
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
                                            id="category-bar-graph19-20",
                                            style={"height": "63vh"},
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
    style={"maxWidth": "65%"},
)


@callback(
    Output("category-bar-graph19-20", "figure"),
    Input("category-dropdown19-20", "value"),
)
def update_graph(selected_category):
    filtered_df = df3[df3["Department"] == selected_category]
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=filtered_df["Course #"],
            y=filtered_df["Cost Savings ($)"],
            text=filtered_df["Cost Savings ($)"],
            marker=dict(color="#005CFE"),
        )
    )

    fig.update_layout(
        title="Breakdown by Individual Course",
        height=550,
        xaxis=dict(categoryorder="total descending", showgrid=False),
        yaxis=dict(showgrid=False, showticklabels=False),
    )
    fig.update_traces(
        texttemplate="%{text:$,.0f}",
        textposition="outside",
    )

    return fig
