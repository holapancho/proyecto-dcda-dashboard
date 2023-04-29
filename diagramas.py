
from fuentes import DatosConcurso
import pandas as pd
import plotly.express as px
import plotly.graph_objs as pg


class Plots:
    def __init__(self):
        self.datos_concurso = DatosConcurso()
        self.paises_ganadores = self.obtener_paises_ganadores_dict()

    def obtener_paises_ganadores_por_anio_arreglo(self, anio):
        song_data = self.datos_concurso.song_data
        song_data_filtrado = song_data[(song_data.year == anio) & (
            song_data.final_place > 0.0)]
        song_data_filtrado_top = song_data_filtrado.sort_values(
            by='final_place', ascending=True)
        return song_data_filtrado_top.head(5).country.tolist()

    def obtener_paises_ganadores_dict(self):
        paises_ganadores_por_anio = {}
        paises_ganadores_por_anio['2022'] = self.obtener_paises_ganadores_por_anio_arreglo(
            2022)
        paises_ganadores_por_anio['2021'] = self.obtener_paises_ganadores_por_anio_arreglo(
            2021)
        paises_ganadores_por_anio['2019'] = self.obtener_paises_ganadores_por_anio_arreglo(
            2019)
        paises_ganadores_por_anio['2018'] = self.obtener_paises_ganadores_por_anio_arreglo(
            2018)
        paises_ganadores_por_anio['2017'] = self.obtener_paises_ganadores_por_anio_arreglo(
            2017)
        paises_ganadores_por_anio['2016'] = self.obtener_paises_ganadores_por_anio_arreglo(
            2016)
        return paises_ganadores_por_anio

    def obtener_dataframe_res_finales_por_anio(self, anio_string):
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
        return df

    def obtener_pie_plot_por_anio(self, anio_string):
        song_data_filtrado_top = self.filtrar_dataset(anio_string)
        fig = px.pie(song_data_filtrado_top,
                     values='final_total_points',
                     names='country',
                     labels={'country': "País",
                             'final_total_points': 'Votos'},
                     title='Top 5 Paises de los Concursantes con mas votos en el año {}'.format(anio_string))
        fig.update_layout(legend = dict(font = dict( size = 18)))
        fig.update_layout(transition_duration=500)
        return fig

    def filtrar_dataset(self, anio_string):
        anio = int(anio_string)
        song_data = self.datos_concurso.song_data
        song_data_filtrado = song_data[(song_data.year == anio) & (
            song_data.final_place > 0.0) & song_data.country.isin(self.paises_ganadores[anio_string])]
        return song_data_filtrado.sort_values(by='final_place', ascending=True)

    def obtener_bar_chart_resultados_finales_por_anio(self, anio_string, excluded_countries):
        df = self.obtener_dataframe_res_finales_por_anio(anio_string)
        fig = px.bar(df.loc[~df['Contestant'].isin(excluded_countries) & df['Contestant'].isin(self.paises_ganadores[anio_string])],
                     x="Contestant",
                     y=["Jury score", "Televoting score"],
                     labels={'variable': "Tipo de Voto",
                             'final_total_points': 'Puntos Totales',
                             'Contestant': 'País',
                             'value':'Votos'},
                     title="Puntos por concursante en el año {}".format(anio_string))
        fig.update_layout(transition_duration=500)
        return fig

    def obtener_mapa_coropletico_resultados_finales_por_anio(self, anio_string, excluded_countries):
        df = self.obtener_dataframe_res_finales_por_anio(anio_string)
        df_mezclado = pd.merge(df, self.datos_concurso.country_data, how='left',
                               left_on='Contestant', right_on='country')[['Contestant', 'Total score', 'CODE']]
        df_mezclado = df_mezclado.loc[~df['Contestant'].isin(excluded_countries) & df['Contestant'].isin(self.paises_ganadores[anio_string])]
        data = dict(type='choropleth',
                    locations=df_mezclado['CODE'],
                    z=df_mezclado['Total score'],
                    text=df_mezclado['Contestant'])
        layout = dict(title='Mapa Coropletico de Votos Totales por Paises Concursantes',
                      geo=dict(projection=pg.layout.geo.Projection(type='albers'),
                               scope="europe",
                               showlakes=True))
        return pg.Figure(data=[data],
                         layout=layout)

    def obtener_df_por_encuesta(self, encuesta):
        df = None
        if encuesta == 'EuroJuly':
            df = self.datos_concurso.datos_encuestas.euro_july.eurojuly_total
        elif encuesta == 'EuroVision World':
            df = self.datos_concurso.datos_encuestas.eurovision_world.eurovisionworld_total
        elif encuesta == 'My Eurovision Score':
            df = self.datos_concurso.datos_encuestas.my_eurovision_score.myeurovisionscoreboard_total
        elif encuesta == 'OGAE':
            df = self.datos_concurso.datos_encuestas.ogae.ogae_results_total
        elif encuesta == 'WiwiBloggs':
            df = self.datos_concurso.datos_encuestas.wiwibloggs.wiwibloggs_results_total
        return df

    def obtener_serie_de_tiempo_por_anio(self, anio_string, encuesta):
        df = self.obtener_df_por_encuesta(encuesta)

        paises_top_5 = df.groupby(['Contestant']).sum(
        ).sort_values(by='Total')[-5:].index
        df = pd.pivot_table(df[['Año', 'Contestant', 'Total']],
                            index='Año', columns='Contestant', values='Total')
        df_top5 = df[list(paises_top_5)]

        fig = pg.Figure()

        for col in df_top5.columns:
            fig.add_trace(pg.Scatter(x=df_top5.index,
                          y=df_top5[col], name=col))

        fig.update_layout(
            title='Series de tiempo evolutiva del TOP 5 de Paises con mayor cantidad de votos',
            xaxis_title='Año',
            yaxis_title='Cantidad de Votos'
        )
        return fig

    def obtener_tabla_por_anio(self, anio_string, excluded_countries):
        song_data_table = self.filtrar_dataset(anio_string)
        song_data_table = song_data_table.loc[~song_data_table['country'].isin(
            excluded_countries)]
        fig = pg.Figure(data=[pg.Table(
            header=dict(values=['Posición', 'Pais', 'Artista', 'Canción', 'Votos'],
                        align='left',
                        fill_color='darkred',
                        font_color="white"),
            cells=dict(values=[song_data_table.final_place,
                               song_data_table.country,
                               song_data_table.artist_name,
                               song_data_table.song_name,
                               song_data_table.final_total_points],
                       align='left',
                        fill_color='grey',
                        font_color="white"))
        ])
        fig.update_layout(
            title='Top 5 Canciones ganadoras al año {}'.format(anio_string)
        )
        return fig
