from dash import html, dcc, callback, Output, Input, Dash
import dash_bootstrap_components as dbc
from app import app, server
from pages import intro, year19_20, year20_21, year21_22, year22_23, year23_24, appendix


app.layout = dbc.Nav(
    html.Div(
        [
            dcc.Location(id="url", refresh=False),
            html.Div(
                [
                    dcc.Link("Home", href="/"),
                    html.Br(),
                    dcc.Link("2019-20", href="/year19_20"),
                    html.Br(),
                    dcc.Link("2020-21", href="/year20_21"),
                    html.Br(),
                    dcc.Link("2021-22", href="/year21_22"),
                    html.Br(),
                    dcc.Link("2022-23", href="/year22_23"),
                    html.Br(),
                    dcc.Link("2023-24", href="/year23_24"),
                    html.Br(),
                    dcc.Link("Appendix", href="/appendix"),
                ],
                style={"padding": 10, "flex": 1},
                className="navbar d-flex justify-content-center gap-2 fs-4 link-offset-2",
            ),
            html.Div(id="page-content", style={"padding": 10}),
        ]
    ),
    class_name="nav justify-content-center",
)


@callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/":
        return intro.layout
    elif pathname == "/year19_20":
        return year19_20.layout
    elif pathname == "/year20_21":
        return year20_21.layout
    elif pathname == "/year21_22":
        return year21_22.layout
    elif pathname == "/year22_23":
        return year22_23.layout
    elif pathname == "/year23_24":
        return year23_24.layout
    elif pathname == "/appendix":
        return appendix.layout
    else:
        return "404 - page not found"


server = app.server
if __name__ == "__main__":
    app.run_server(debug=True)
