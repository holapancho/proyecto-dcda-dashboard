from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from diagramas import Plots
from dash_bootstrap_templates import load_figure_template

load_figure_template('SLATE')
plots = Plots()

encuesta_string = ['EuroVision World', 'EuroJuly',
                   'My Eurovision Score', 'OGAE', 'WiwiBloggs']
encuesta_por_defecto = 'EuroVision World'
anios_string = ['2022', '2021', '2019', '2018', '2017', '2016']
anio_por_defecto = '2022'
paises_ganadores = plots.obtener_paises_ganadores_dict()

app = Dash(external_stylesheets=[dbc.themes.SLATE])

app.layout = dbc.Container(
    children=[
        # Primer Registro - cabecera
        dbc.Row([
            dbc.Col(children=[
                html.Div(html.Img(src='assets/dataset-cover.png',
                                  style={'height': '100px'})),
                html.Div(
                    html.H3("TOP 5 - Eurovision Song Contest Data Dashboard")),
                html.Div(html.P(
                    "El presente Dashboard muestra los datos del concurso Eurovision Song de los cuales...")),
                html.Div(html.H5("Año")),
                html.Div(dcc.Dropdown(options=anios_string,
                                      value=anio_por_defecto,
                                      clearable=False,
                                      id='anio-dropdown')),
                html.Div(html.H5("Encuesta")),
                html.Div(dcc.Dropdown(options=encuesta_string,
                                      value=encuesta_por_defecto,
                                      clearable=False,
                                      id='encuesta-dropdown'))
            ],
                md=2),
            dbc.Col(dcc.Graph(id='grafico-1'), md=4),  # Pie chart
            dbc.Col(dcc.Graph(id='grafico-5'), md=3),
            dbc.Col(dcc.Graph(id='grafico-3'), md=3)  # Mapa coropletico
        ]),


        # Segundo Registro
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='grafico-4'), md=6),  # serie de tiempo
                dbc.Col(dcc.Graph(id='grafico-2'), md=6)  # bar chart
            ]
        ),

    ],
    fluid=True
)

# documentacion https://dash.plotly.com/interactive-graphing
# The dcc.Graph component has four attributes that can change through user-interaction: hoverData, clickData, selectedData, relayoutData. These properties update when you hover over points, click on points, or select regions of points in a graph.


# Pie chart
@ app.callback(
    Output('grafico-1', 'figure'),
    Input('anio-dropdown', 'value')
)
def actualiza_pie_plot_por_anio(value):
    if value == 'None':
        value = anio_por_defecto
    return plots.obtener_pie_plot_por_anio(value)

# bar chart


@ app.callback(
    Output('grafico-2', 'figure'),
    Input('anio-dropdown', 'value'),
    Input(component_id='grafico-1', component_property='relayoutData')
)
def actualiza_bar_chart_resultados_finales_por_anio(value, relayoutData):
    hiddenlabels = []
    if value == 'None':
        value = anio_por_defecto

    if isinstance(relayoutData, dict):
        if 'hiddenlabels' in relayoutData:
            hiddenlabels = relayoutData['hiddenlabels']

    return plots.obtener_bar_chart_resultados_finales_por_anio(value, hiddenlabels)

# Mapa coropletico
@ app.callback(
    Output('grafico-3', 'figure'),
    Input('anio-dropdown', 'value')
)
def actualiza_mapa_resultados_finales_por_anio(value):
    if value == 'None':
        value = anio_por_defecto
    return plots.obtener_mapa_coropletico_resultados_finales_por_anio(value)

# grafico 4: serie de tiempo
@ app.callback(
    Output('grafico-4', 'figure'),
    Input('anio-dropdown', 'value'),
    Input('encuesta-dropdown', 'value')
)
def actualiza_serie_de_tiempo_por_anio_y_encuesta(anio, encuesta):
    return plots.obtener_serie_de_tiempo_por_anio(anio, encuesta)

# grafico 5: tabla
@ app.callback(
    Output('grafico-5', 'figure'),
    Input('anio-dropdown', 'value')
)
def actualizar_tabla_por_anio(anio):
    return plots.obtener_tabla_por_anio(anio) 

if __name__ == '__main__':
    app.run_server(debug=True)
