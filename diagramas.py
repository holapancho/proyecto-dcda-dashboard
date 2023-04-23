
from fuentes import DatosConcurso
import pandas as pd
import plotly.express as px

class Plots:
    def __init__(self):
        self.datos_concurso = DatosConcurso()

    def obtener_pie_plot_por_anio(self, anio_string):
        anio = int(anio_string)
        song_data = self.datos_concurso.song_data
        song_data_2022 = song_data[(song_data.year == anio) & (song_data.final_place > 0.0)]
        song_data_2022_top = song_data_2022.sort_values(by='final_place',ascending=True)
        fig = px.pie(song_data_2022_top, values='final_total_points', names='country', title='Paises de los artistas con mas votos el año {}'.format(anio))
        fig.update_layout(transition_duration=500)
        return fig
    
    def obtener_bar_chart_resultados_finales_por_anio(self, anio_string, excluded_countries):
        df = None
        if anio_string == '2022':
            df = self.datos_concurso.datos_resultados_finales.datos_televotacion.televote_results_2022
        elif anio_string == '2021':
            df = self.datos_concurso.datos_resultados_finales.datos_televotacion.televote_results_2021
        elif anio_string == '2019':
            df = self.datos_concurso.datos_resultados_finales.datos_televotacion.televote_results_2019
        elif anio_string == '2018':
            df = self.datos_concurso.datos_resultados_finales.datos_televotacion.televote_results_2018
        elif anio_string == '2017':
            df = self.datos_concurso.datos_resultados_finales.datos_televotacion.televote_results_2017
        elif anio_string == '2016':
            df = self.datos_concurso.datos_resultados_finales.datos_televotacion.televote_results_2016

        fig = px.bar(df.loc[~df['Contestant'].isin(excluded_countries)], x="Contestant", y=["Jury score", "Televoting score"], title="Puntos por concursante en el año {}".format(anio_string))
        fig.update_layout(transition_duration=500)
        return fig