import pandas as pd

class DatosConcurso:
  def __init__(self):
    self.contest_data = pd.read_csv("./csv_fuentes/contest_data.csv")
    self.country_data = pd.read_csv("./csv_fuentes/country_data.csv")
    self.song_data = pd.read_csv("./csv_fuentes/song_data.csv")
    self.datos_resultados_finales = DatosResultadosFinales()

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

class DatosTelevotacion:
  def __init__(self):
    self.televote_results_2016 = pd.read_csv("./csv_fuentes/resultados_finales/televotacion/2016_televote_results.csv")
    self.televote_results_2017 = pd.read_csv("./csv_fuentes/resultados_finales/televotacion/2017_televote_results.csv")
    self.televote_results_2018 = pd.read_csv("./csv_fuentes/resultados_finales/televotacion/2018_televote_results.csv")
    self.televote_results_2019 = pd.read_csv("./csv_fuentes/resultados_finales/televotacion/2019_televote_results.csv")
    self.televote_results_2021 = pd.read_csv("./csv_fuentes/resultados_finales/televotacion/2021_televote_results.csv")
    self.televote_results_2022 = pd.read_csv("./csv_fuentes/resultados_finales/televotacion/2022_televote_results.csv")