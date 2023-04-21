
from fuentes import DatosConcurso
import pandas as pd
import plotly.express as px

class Plots:
    def __init__(self):
        self.datos_concurso = DatosConcurso()

    def obtener_plot_por_anio(self, anio_string):
        print(anio_string)
        anio = int(anio_string)
        song_data = self.datos_concurso.song_data
        song_data_2022 = song_data[(song_data.year == anio) & (song_data.final_place > 0.0)]
        song_data_2022_top = song_data_2022.sort_values(by='final_place',ascending=True)
        fig = px.pie(song_data_2022_top.head(), values='final_total_points', names='country', title='Paises de los artistas con mas votos el año {}'.format(anio))
        fig.update_layout(transition_duration=500)
        return fig