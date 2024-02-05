from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc


app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])

df = pd.read_csv("./Cleaned_Datasets/1fall_2019.csv")
df2 = pd.read_csv("./Cleaned_Datasets/1spring_2020.csv")
df3 = pd.concat([df, df2])
total = df3["Cost Savings ($)"].sum()

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "10%",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.Hr(),
        html.P("A simple sidebar layout with navigation links", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Page 1", href="/page-1", active="exact"),
                dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

fig1 = px.histogram(
    df3,
    x="Department",
    y="Cost Savings ($)",
    title="2019-2020 Academic Year by Category",
)
fig1.update_xaxes(categoryorder="total descending")


app.layout = dbc.Container(
    [
        html.Div([dcc.Location(id="url"), sidebar, content]),
        dbc.Row(
            [
                html.Div(
                    [
                        html.H3(
                            f"The University of Iowa has saved students ${total:,.2f} in textbook costs in 19-20",
                            className="text-center",
                        ),
                        dcc.Graph(figure=fig1),
                        dcc.Dropdown(
                            id="category-dropdown",
                            options=[
                                {"label": i, "value": i}
                                for i in df3["Department"].unique()
                            ],
                            value="Education",
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col([html.Div([dcc.Graph(id="category-bar-graph")])]),
                    ]
                ),
            ]
        ),
    ],
    style={"maxWidth": "75%"},
)


@callback(Output("category-bar-graph", "figure"), Input("category-dropdown", "value"))
def update_graph(selected_category):
    filtered_df = df3[df3["Department"] == selected_category]
    fig = px.bar(
        filtered_df, x="Course #", y="Cost Savings ($)", text="Cost Savings ($)"
    )
    fig.update_xaxes(categoryorder="total descending")
    fig.update_traces(texttemplate="%{text:$,.0f}", textposition="outside")
    return fig


if __name__ == "__main__":
    app.run(debug=True)
