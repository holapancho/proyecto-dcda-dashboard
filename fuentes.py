import pandas as pd
from utilitarios import columna_2022, columna_2021, columna_2019, columna_2018, columna_2017, columna_2016, convertirDataframeColumnaObjectAFloat, convertirDataframeColumnaObjectAInt, convertirDataframeColumnaObjectAString, convertirDataframeColumnasObjectAFloat

class DatosConcurso:
  def __init__(self):
    self.contest_data = pd.read_csv("./csv_fuentes/contest_data.csv")
    self.country_data = pd.read_csv("./csv_fuentes/country_data.csv")
    self.song_data = pd.read_csv("./csv_fuentes/song_data.csv")

    #sanitiza song_data
    convertirDataframeColumnaObjectAInt(self.song_data, 'final_draw_position')
    convertirDataframeColumnaObjectAInt(self.song_data, 'semi_draw_position')
    convertirDataframeColumnaObjectAString(self.song_data, 'country')
    convertirDataframeColumnaObjectAString(self.song_data, 'artist_name')
    convertirDataframeColumnaObjectAString(self.song_data, 'song_name')
    convertirDataframeColumnaObjectAString(self.song_data, 'language')
    convertirDataframeColumnaObjectAString(self.song_data, 'style')
    convertirDataframeColumnaObjectAString(self.song_data, 'race')
    convertirDataframeColumnaObjectAInt(self.song_data, 'energy')
    convertirDataframeColumnaObjectAInt(self.song_data, 'danceability')
    convertirDataframeColumnaObjectAInt(self.song_data, 'happiness')
    convertirDataframeColumnaObjectAString(self.song_data, 'loudness')
    convertirDataframeColumnaObjectAInt(self.song_data, 'acousticness')
    convertirDataframeColumnaObjectAInt(self.song_data, 'instrumentalness')
    convertirDataframeColumnaObjectAInt(self.song_data, 'liveness')
    convertirDataframeColumnaObjectAString(self.song_data, 'speechiness')
    convertirDataframeColumnaObjectAInt(self.song_data, 'BPM')
    convertirDataframeColumnaObjectAFloat(self.song_data, 'final_jury_votes')
    convertirDataframeColumnaObjectAFloat(self.song_data, 'final_televote_points')
    convertirDataframeColumnaObjectAFloat(self.song_data, 'final_jury_points')
    convertirDataframeColumnaObjectAFloat(self.song_data, 'final_televote_votes')
    convertirDataframeColumnaObjectAFloat(self.song_data, 'final_place')
    convertirDataframeColumnaObjectAFloat(self.song_data, 'final_total_points')
    convertirDataframeColumnaObjectAFloat(self.song_data, 'semi_place')
    convertirDataframeColumnaObjectAFloat(self.song_data, 'semi_televote_points')
    convertirDataframeColumnaObjectAFloat(self.song_data, 'semi_jury_points')
    convertirDataframeColumnaObjectAFloat(self.song_data, 'semi_total_points')
    self.song_data.drop(['gender','age','selection'], axis=1,  inplace=True)

    #Sub dataframes
    self.datos_resultados_finales = DatosResultadosFinales()
    self.datos_encuestas = DatosEncuestas()

class DatosResultadosFinales:
  def __init__(self):
    self.datos_jurado = DatosJurado()
    self.datos_televotacion = DatosTelevotacion()

class DatosJurado:
  def __init__(self):
    self.jury_results_2016 = pd.read_csv("./csv_fuentes/resultados_finales/jurado/2016_jury_results.csv")
    self.jury_results_2017 = pd.read_csv("./csv_fuentes/resultados_finales/jurado/2017_jury_results.csv")
    self.jury_results_2018 = pd.read_csv("./csv_fuentes/resultados_finales/jurado/2018_jury_results.csv")
    self.jury_results_2019 = pd.read_csv("./csv_fuentes/resultados_finales/jurado/2019_jury_results.csv")
    self.jury_results_2021 = pd.read_csv("./csv_fuentes/resultados_finales/jurado/2021_jury_results.csv")
    self.jury_results_2022 = pd.read_csv("./csv_fuentes/resultados_finales/jurado/2022_jury_results.csv")

    convertirDataframeColumnasObjectAFloat(self.jury_results_2022, columna_2022)
    convertirDataframeColumnasObjectAFloat(self.jury_results_2021, columna_2021)
    convertirDataframeColumnasObjectAFloat(self.jury_results_2019, columna_2019)
    convertirDataframeColumnasObjectAFloat(self.jury_results_2018, columna_2018)
    convertirDataframeColumnasObjectAFloat(self.jury_results_2017, columna_2017)
    convertirDataframeColumnasObjectAFloat(self.jury_results_2016, columna_2016)

class DatosTelevotacion:
  def __init__(self):
    self.televote_results_2016 = pd.read_csv("./csv_fuentes/resultados_finales/televotacion/2016_televote_results.csv")
    self.televote_results_2017 = pd.read_csv("./csv_fuentes/resultados_finales/televotacion/2017_televote_results.csv")
    self.televote_results_2018 = pd.read_csv("./csv_fuentes/resultados_finales/televotacion/2018_televote_results.csv")
    self.televote_results_2019 = pd.read_csv("./csv_fuentes/resultados_finales/televotacion/2019_televote_results.csv")
    self.televote_results_2021 = pd.read_csv("./csv_fuentes/resultados_finales/televotacion/2021_televote_results.csv")
    self.televote_results_2022 = pd.read_csv("./csv_fuentes/resultados_finales/televotacion/2022_televote_results.csv")

    convertirDataframeColumnasObjectAFloat(self.televote_results_2022, columna_2022)
    convertirDataframeColumnasObjectAFloat(self.televote_results_2021, columna_2021)
    convertirDataframeColumnasObjectAFloat(self.televote_results_2019, columna_2019)
    convertirDataframeColumnasObjectAFloat(self.televote_results_2018, columna_2018)
    convertirDataframeColumnasObjectAFloat(self.televote_results_2017, columna_2017)
    convertirDataframeColumnasObjectAFloat(self.televote_results_2016, columna_2016)

class DatosEncuestas:
  def __init__(self) -> None:
    self.euro_july = EuroJuly()
    self.eurovision_world = EurovisionWorld()
    self.my_eurovision_score = MyEurovisionScore()
    self.ogae = OGAE()
    self.wiwibloggs = Wiwibloggs()
    
class EuroJuly:
  def __init__(self):
    self.eurojury_results_2016 = pd.read_csv("./csv_fuentes/encuestas/euro_july/2016_eurojury_results.csv")
    self.eurojury_results_2017 = pd.read_csv("./csv_fuentes/encuestas/euro_july/2017_eurojury_results.csv")
    self.eurojury_results_2018 = pd.read_csv("./csv_fuentes/encuestas/euro_july/2018_eurojury_results.csv")
    self.eurojury_results_2019 = pd.read_csv("./csv_fuentes/encuestas/euro_july/2019_eurojury_results.csv")
    self.eurojury_results_2021 = pd.read_csv("./csv_fuentes/encuestas/euro_july/2021_eurojury_results.csv")
    self.eurojury_results_2022 = pd.read_csv("./csv_fuentes/encuestas/euro_july/2022_eurojury_results.csv")

    #asignacion temporal para iteracion
    concurso_2016 = self.eurojury_results_2016
    concurso_2017 = self.eurojury_results_2017
    concurso_2018 = self.eurojury_results_2018
    concurso_2019 = self.eurojury_results_2019
    concurso_2021 = self.eurojury_results_2021
    concurso_2022 = self.eurojury_results_2022

    anios = [2016, 2017, 2018, 2019, 2021, 2022]
    eurojuly_total = pd.DataFrame()
    for anio in anios:
        df_seleccionado = locals()['concurso_'+str(anio)]
        df_seleccionado['Total'] = df_seleccionado['Online Points'] + df_seleccionado['Jury Points']
        df_seleccionado['Año'] = anio
        eurojuly_total = pd.concat([df_seleccionado, eurojuly_total])
    self.eurojuly_total = eurojuly_total

class EurovisionWorld:
  def __init__(self):
    self.eurovisionworld_results_2016 = pd.read_csv("./csv_fuentes/encuestas/eurovision_world/2016_eurovisionworld_results.csv")
    self.eurovisionworld_results_2017 = pd.read_csv("./csv_fuentes/encuestas/eurovision_world/2017_eurovisionworld_results.csv")
    self.eurovisionworld_results_2018 = pd.read_csv("./csv_fuentes/encuestas/eurovision_world/2018_eurovisionworld_results.csv")
    self.eurovisionworld_results_2019 = pd.read_csv("./csv_fuentes/encuestas/eurovision_world/2019_eurovisionworld_results.csv")
    self.eurovisionworld_results_2021 = pd.read_csv("./csv_fuentes/encuestas/eurovision_world/2021_eurovisionworld_results.csv")
    self.eurovisionworld_results_2022 = pd.read_csv("./csv_fuentes/encuestas/eurovision_world/2022_eurovisionworld_results.csv")

    #asignacion temporal para iteracion
    concurso_2016 = self.eurovisionworld_results_2016
    concurso_2017 = self.eurovisionworld_results_2017
    concurso_2018 = self.eurovisionworld_results_2018
    concurso_2019 = self.eurovisionworld_results_2019
    concurso_2021 = self.eurovisionworld_results_2021
    concurso_2022 = self.eurovisionworld_results_2022

    eurovisionworld_total = pd.DataFrame()
    anios = [2016, 2017, 2018, 2019, 2021, 2022]
    for anio in anios:
      df_seleccionado = locals()['concurso_'+str(anio)]
      df_seleccionado['Año'] = anio
      df_seleccionado['Total'] = df_seleccionado['Votes']
      eurovisionworld_total = pd.concat([df_seleccionado, eurovisionworld_total])
    self.eurovisionworld_total = eurovisionworld_total

class MyEurovisionScore:
  def __init__(self):
    self.myeurovisionscoreboard_results_2016 = pd.read_csv("./csv_fuentes/encuestas/my_eurovision_score/2016_myeurovisionscoreboard_results.csv")
    self.myeurovisionscoreboard_results_2017 = pd.read_csv("./csv_fuentes/encuestas/my_eurovision_score/2017_myeurovisionscoreboard_results.csv")
    self.myeurovisionscoreboard_results_2018 = pd.read_csv("./csv_fuentes/encuestas/my_eurovision_score/2018_myeurovisionscoreboard_results.csv")
    self.myeurovisionscoreboard_results_2019 = pd.read_csv("./csv_fuentes/encuestas/my_eurovision_score/2019_myeurovisionscoreboard_results.csv")
    self.myeurovisionscoreboard_results_2021 = pd.read_csv("./csv_fuentes/encuestas/my_eurovision_score/2021_myeurovisionscoreboard_results.csv")
    self.myeurovisionscoreboard_results_2022 = pd.read_csv("./csv_fuentes/encuestas/my_eurovision_score/2022_myeurovisionscoreboard_results.csv")

    #asignacion temporal para iteracion
    concurso_2016 = self.myeurovisionscoreboard_results_2016
    concurso_2017 = self.myeurovisionscoreboard_results_2017
    concurso_2018 = self.myeurovisionscoreboard_results_2018
    concurso_2019 = self.myeurovisionscoreboard_results_2019
    concurso_2021 = self.myeurovisionscoreboard_results_2021
    concurso_2022 = self.myeurovisionscoreboard_results_2022

    myeurovisionscoreboard_total = pd.DataFrame()
    anios = [2016, 2017, 2018, 2019, 2021, 2022]
    for anio in anios:
      df_seleccionado = locals()['concurso_'+str(anio)]
      df_seleccionado['Año'] = anio
      df_seleccionado['Total'] = df_seleccionado['Points']
      myeurovisionscoreboard_total = pd.concat([df_seleccionado, myeurovisionscoreboard_total])
    self.myeurovisionscoreboard_total = myeurovisionscoreboard_total

class OGAE:
  def __init__(self):
    self.ogae_results_2016 = pd.read_csv("./csv_fuentes/encuestas/ogae/2016_ogae_results.csv")
    self.ogae_results_2017 = pd.read_csv("./csv_fuentes/encuestas/ogae/2017_ogae_results.csv")
    self.ogae_results_2018 = pd.read_csv("./csv_fuentes/encuestas/ogae/2018_ogae_results.csv")
    self.ogae_results_2019 = pd.read_csv("./csv_fuentes/encuestas/ogae/2019_ogae_results.csv")
    self.ogae_results_2021 = pd.read_csv("./csv_fuentes/encuestas/ogae/2021_ogae_results.csv")
    self.ogae_results_2022 = pd.read_csv("./csv_fuentes/encuestas/ogae/2022_ogae_results.csv")

    #asignacion temporal para iteracion
    concurso_2016 = self.ogae_results_2016
    concurso_2017 = self.ogae_results_2017
    concurso_2018 = self.ogae_results_2018
    concurso_2019 = self.ogae_results_2019
    concurso_2021 = self.ogae_results_2021
    concurso_2022 = self.ogae_results_2022

    ogae_results_total = pd.DataFrame()
    anios = [2016, 2017, 2018, 2019, 2021, 2022]
    for anio in anios:
      df_seleccionado = locals()['concurso_'+str(anio)]
      df_seleccionado['Año'] = anio
      df_seleccionado['Total'] = df_seleccionado['Points']
      ogae_results_total = pd.concat([df_seleccionado, ogae_results_total])
    self.ogae_results_total = ogae_results_total


class Wiwibloggs:
  def __init__(self):
    self.wiwibloggs_results_2018 = pd.read_csv("./csv_fuentes/encuestas/wiwibloggs/2018_wiwibloggs_results.csv")
    self.wiwibloggs_results_2019 = pd.read_csv("./csv_fuentes/encuestas/wiwibloggs/2019_wiwibloggs_results.csv")
    self.wiwibloggs_results_2021 = pd.read_csv("./csv_fuentes/encuestas/wiwibloggs/2021_wiwibloggs_results.csv")
    self.wiwibloggs_results_2022 = pd.read_csv("./csv_fuentes/encuestas/wiwibloggs/2022_wiwibloggs_results.csv")

    #asignacion temporal para iteracion
    concurso_2018 = self.wiwibloggs_results_2018
    concurso_2019 = self.wiwibloggs_results_2019
    concurso_2021 = self.wiwibloggs_results_2021
    concurso_2022 = self.wiwibloggs_results_2022

    wiwibloggs_results_total = pd.DataFrame()
    anios = [2018, 2019, 2021, 2022]
    for anio in anios:
      df_seleccionado = locals()['concurso_'+str(anio)]
      df_seleccionado['Año'] = anio
      df_seleccionado['Total'] = df_seleccionado['Votes']
      wiwibloggs_results_total = pd.concat([df_seleccionado, wiwibloggs_results_total])
    self.wiwibloggs_results_total = wiwibloggs_results_total
