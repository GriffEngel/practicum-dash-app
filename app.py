from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc


app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])

df = pd.read_csv("./Cleaned_Datasets/1fall_2019.csv")
df2 = pd.read_csv("./Cleaned_Datasets/1spring_2020.csv")
df3 = pd.concat([df, df2])
total = df3["Cost Savings ($)"].sum()

# ==============NavBar=================
NAV = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("2019-20", active=True, href="#")),
        dbc.NavItem(dbc.NavLink("2020-21", href="#")),
        dbc.NavItem(dbc.NavLink("2021-22", href="#")),
        dbc.NavItem(dbc.NavLink("2022-23", href="#")),
        dbc.NavItem(dbc.NavLink("2023-24", href="#")),
    ],
    class_name="d-flex justify-content-center fs-4",
)

NAVBAR_STYLE = {
    "position": "relative",
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

fig1 = px.histogram(
    df3,
    x="Department",
    y="Cost Savings ($)",
    title="2019-2020 Academic Year by Category",
)
fig1.update_xaxes(categoryorder="total descending")


app.layout = dbc.Container(
    [
        NAV,
        dbc.Row(
            [
                html.Div(
                    [
                        html.H3(
                            f"The University of Iowa saved students ${total:,.2f} in textbook costs in 19-20",
                            className="text-center fs-5",
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
