import pandas as pd

class DatosConcurso:
  def __init__(self):
    self.contest_data = pd.read_csv("./csv_fuentes/contest_data.csv")
    self.country_data = pd.read_csv("./csv_fuentes/country_data.csv")
    self.song_data = pd.read_csv("./csv_fuentes/song_data.csv")
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

class DatosTelevotacion:
  def __init__(self):
    self.televote_results_2016 = pd.read_csv("./csv_fuentes/resultados_finales/televotacion/2016_televote_results.csv")
    self.televote_results_2017 = pd.read_csv("./csv_fuentes/resultados_finales/televotacion/2017_televote_results.csv")
    self.televote_results_2018 = pd.read_csv("./csv_fuentes/resultados_finales/televotacion/2018_televote_results.csv")
    self.televote_results_2019 = pd.read_csv("./csv_fuentes/resultados_finales/televotacion/2019_televote_results.csv")
    self.televote_results_2021 = pd.read_csv("./csv_fuentes/resultados_finales/televotacion/2021_televote_results.csv")
    self.televote_results_2022 = pd.read_csv("./csv_fuentes/resultados_finales/televotacion/2022_televote_results.csv")

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

class EurovisionWorld:
  def __init__(self):
    self.eurovisionworld_results_2016 = pd.read_csv("./csv_fuentes/encuestas/eurovision_world/2016_eurovisionworld_results.csv")
    self.eurovisionworld_results_2017 = pd.read_csv("./csv_fuentes/encuestas/eurovision_world/2017_eurovisionworld_results.csv")
    self.eurovisionworld_results_2018 = pd.read_csv("./csv_fuentes/encuestas/eurovision_world/2018_eurovisionworld_results.csv")
    self.eurovisionworld_results_2019 = pd.read_csv("./csv_fuentes/encuestas/eurovision_world/2019_eurovisionworld_results.csv")
    self.eurovisionworld_results_2021 = pd.read_csv("./csv_fuentes/encuestas/eurovision_world/2021_eurovisionworld_results.csv")
    self.eurovisionworld_results_2022 = pd.read_csv("./csv_fuentes/encuestas/eurovision_world/2022_eurovisionworld_results.csv")

class MyEurovisionScore:
  def __init__(self):
    self.myeurovisionscoreboard_results_2016 = pd.read_csv("./csv_fuentes/encuestas/my_eurovision_score/2016_myeurovisionscoreboard_results.csv")
    self.myeurovisionscoreboard_results_2017 = pd.read_csv("./csv_fuentes/encuestas/my_eurovision_score/2017_myeurovisionscoreboard_results.csv")
    self.myeurovisionscoreboard_results_2018 = pd.read_csv("./csv_fuentes/encuestas/my_eurovision_score/2018_myeurovisionscoreboard_results.csv")
    self.myeurovisionscoreboard_results_2019 = pd.read_csv("./csv_fuentes/encuestas/my_eurovision_score/2019_myeurovisionscoreboard_results.csv")
    self.myeurovisionscoreboard_results_2021 = pd.read_csv("./csv_fuentes/encuestas/my_eurovision_score/2021_myeurovisionscoreboard_results.csv")
    self.myeurovisionscoreboard_results_2022 = pd.read_csv("./csv_fuentes/encuestas/my_eurovision_score/2022_myeurovisionscoreboard_results.csv")

class OGAE:
  def __init__(self):
    self.ogae_results_2016 = pd.read_csv("./csv_fuentes/encuestas/ogae/2016_ogae_results.csv")
    self.ogae_results_2017 = pd.read_csv("./csv_fuentes/encuestas/ogae/2017_ogae_results.csv")
    self.ogae_results_2018 = pd.read_csv("./csv_fuentes/encuestas/ogae/2018_ogae_results.csv")
    self.ogae_results_2019 = pd.read_csv("./csv_fuentes/encuestas/ogae/2019_ogae_results.csv")
    self.ogae_results_2021 = pd.read_csv("./csv_fuentes/encuestas/ogae/2021_ogae_results.csv")
    self.ogae_results_2022 = pd.read_csv("./csv_fuentes/encuestas/ogae/2022_ogae_results.csv")

class Wiwibloggs:
  def __init__(self):
    self.wiwibloggs_results_2018 = pd.read_csv("./csv_fuentes/encuestas/wiwibloggs/2018_wiwibloggs_results.csv")
    self.wiwibloggs_results_2019 = pd.read_csv("./csv_fuentes/encuestas/wiwibloggs/2019_wiwibloggs_results.csv")
    self.wiwibloggs_results_2021 = pd.read_csv("./csv_fuentes/encuestas/wiwibloggs/2021_wiwibloggs_results.csv")
    self.wiwibloggs_results_2022 = pd.read_csv("./csv_fuentes/encuestas/wiwibloggs/2022_wiwibloggs_results.csv")
