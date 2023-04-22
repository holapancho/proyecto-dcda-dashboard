from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from diagramas import Plots

plots = Plots()

anios_string = ['2022', '2021', '2019', '2018', '2017', '2016']
anio_por_defecto = '2022'

# temas disponibles en https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/#available-themes
app = Dash(external_stylesheets=[dbc.themes.SPACELAB])

app.layout = dbc.Container(
    children=[
        # Primer Registro - cabecera
        dbc.Row(
            [
                dbc.Col(html.Img(src='assets/dataset-cover.png',
                        style={'height': '100px'}), md=1),
                dbc.Col(md=9),
                dbc.Col(dcc.Dropdown(anios_string,
                                     anio_por_defecto,
                                     searchable=False,
                                     id='demo-dropdown'),
                        md=2)
            ]),
        # Primer Registro - cabecera
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='grafico-1'), md=6),
                dbc.Col(md=6)
            ]
        )
    ],
    fluid=True
)


@app.callback(
    Output('grafico-1', 'figure'),
    Input('demo-dropdown', 'value')
)
def actualiza_grafico_por_anio(value):
    if value == 'None':
        value = anio_por_defecto
    return plots.obtener_pie_plot_por_anio(value)


if __name__ == '__main__':
    app.run_server(debug=True)
