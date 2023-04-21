from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from diagramas import Plots

plots = Plots()

# temas disponibles en https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/#available-themes
app = Dash(external_stylesheets=[dbc.themes.SPACELAB])

app.layout = dbc.Container(
    children=[
        # Primer Registro - cabecera
        dbc.Row(
            [
                dbc.Col(html.Img(src='assets/dataset-cover.png',
                        style={'height': '25%'}), md=1),
                dbc.Col(md=9),
                dbc.Col(dcc.Dropdown(['2022', '2021', '2020'],
                                     '2022',
                                     searchable=False,
                                     id='demo-dropdown'),
                        md=2)
            ]),
        # Primer Registro - cabecera
        dbc.Row(
            dcc.Graph(id='grafico-1'))
    ],
    fluid=True
)


@app.callback(
    Output('grafico-1', 'figure'),
    Input('demo-dropdown', 'value')
)
def actualiza_grafico_por_anio(value):
    if value == 'None':
        value = '2022'
    return plots.obtener_plot_por_anio(value)


if __name__ == '__main__':
    app.run_server(debug=True)
