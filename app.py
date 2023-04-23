from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from diagramas import Plots
from dash_bootstrap_templates import load_figure_template

load_figure_template('SLATE')
plots = Plots()

anios_string = ['2022', '2021', '2019', '2018', '2017', '2016']
anio_por_defecto = '2022'

# temas disponibles en https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/#available-themes
app = Dash(external_stylesheets=[dbc.themes.SLATE])

app.layout = dbc.Container(
    children=[
        # Primer Registro - cabecera
        dbc.Row(
            [
                dbc.Col(html.Img(src='assets/dataset-cover.png',
                        style={'height': '100px'}), md=1),
                dbc.Col(md=9),
                dbc.Col(dcc.Dropdown(options=anios_string,
                                     value=anio_por_defecto,
                                     clearable=False,
                                     id='demo-dropdown'),
                        md=2)
            ]),
        # Segundo Registro 
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='grafico-1'), md=12)
            ]
        ),
         # Tercer Registro 
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='grafico-2'), md=12)
            ]
        ),
        # Cuarto Registro 
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='grafico-3'), md=12)
            ]
        )
    ],
    fluid=True
)

#documentacion https://dash.plotly.com/interactive-graphing
#The dcc.Graph component has four attributes that can change through user-interaction: hoverData, clickData, selectedData, relayoutData. These properties update when you hover over points, click on points, or select regions of points in a graph.


@app.callback(
    Output('grafico-1', 'figure'),
    Input('demo-dropdown', 'value')
)
def actualiza_pie_plot_por_anio(value):
    if value == 'None':
        value = anio_por_defecto
    return plots.obtener_pie_plot_por_anio(value)

@app.callback(
    Output('grafico-2', 'figure'),
    Input('demo-dropdown', 'value'),
    Input(component_id='grafico-1', component_property='relayoutData') 
)
def actualiza_bar_chart_resultados_finales_por_anio(value,relayoutData):
    hiddenlabels = []
    if value == 'None':
        value = anio_por_defecto

    if isinstance(relayoutData, dict):
        if 'hiddenlabels' in relayoutData:
            hiddenlabels = relayoutData['hiddenlabels']
    return plots.obtener_bar_chart_resultados_finales_por_anio(value,hiddenlabels)

@app.callback(
    Output('grafico-3', 'figure'),
    Input('demo-dropdown', 'value')
)
def actualiza_mapa_resultados_finales_por_anio(value):
    if value == 'None':
        value = anio_por_defecto
    return plots.obtener_mapa_coropletico_resultados_finales_por_anio(value)

if __name__ == '__main__':
    app.run_server(debug=True)
