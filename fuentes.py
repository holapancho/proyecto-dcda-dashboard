import pandas as pd

class DatosConcurso:
  def __init__(self):
    self.contest_data = pd.read_csv("./csv_fuentes/contest_data.csv") 