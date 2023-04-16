from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from fuentes import DatosConcurso

concurso = DatosConcurso()

# temas disponibles en https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/#available-themes
app = Dash(external_stylesheets=[dbc.themes.DARKLY])

app.layout = dbc.Container(
    children=[
        # Primer Registro - cabecera
        dbc.Row(
            [
                dbc.Col(html.Img(src='assets/dataset-cover.png',
                        style={'height': '25%'}), md=1)
            ])
    ],
    fluid=True
)

if __name__ == '__main__':
    app.run_server(debug=True)
