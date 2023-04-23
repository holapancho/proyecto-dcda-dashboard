# Metodos utilizarios para manipular columnas del dataframe

def convertirDataframeColumnaObjectAInt(df, nombre_columna):
    df[nombre_columna] = df[nombre_columna].astype(str).replace('-','0').replace('nan','0').astype(int)

def convertirDataframeColumnaObjectAFloat(df, nombre_columna):
    df[nombre_columna] = df[nombre_columna].astype(str).replace('-','0').replace('nan','0').astype(float)

def convertirDataframeColumnasObjectAFloat(df, nombre_columnas):
    for idx, nombre_columna in enumerate(nombre_columnas):
        df[nombre_columna] = df[nombre_columna].astype(str).replace('-','0').replace('nan','0').astype(float)

def convertirDataframeColumnaObjectAString(df, nombre_columna):
    df[nombre_columna] = df[nombre_columna].astype('string')

columna_2022 = ['Netherlands', 'San Marino', 'North Macedonia', 'Malta', 'Ukraine',
    'Albania', 'Estonia', 'Azerbaijan', 'Portugal', 'Germany', 'Belgium',
    'Norway', 'Israel', 'Poland', 'Greece', 'Moldova', 'Bulgaria', 'Serbia',
    'Iceland', 'Cyprus', 'Latvia', 'Spain', 'Switzerland', 'Denmark',
    'France', 'Armenia', 'Montenegro', 'Romania', 'Ireland', 'Slovenia',
    'Georgia', 'Croatia', 'Lithuania', 'Austria', 'Finland',
    'United Kingdom', 'Sweden', 'Australia', 'Czech Republic', 'Italy']
columna_2021 = ['Israel',
    'Poland', 'San Marino', 'Albania', 'Malta', 'Estonia',
    'North Macedonia', 'Azerbaijan', 'Norway', 'Spain', 'Austria',
    'United Kingdom', 'Italy', 'Slovenia', 'Greece', 'Latvia', 'Ireland',
    'Moldova', 'Serbia', 'Bulgaria', 'Cyprus', 'Belgium', 'Germany',
    'Australia', 'Finland', 'Portugal', 'Ukraine', 'Iceland', 'Romania',
    'Croatia', 'Czech Republic', 'Georgia', 'Lithuania', 'Denmark',
    'Russia', 'France', 'Sweden', 'Switzerland', 'Netherlands']
columna_2019 = [ 'Portugal', 'Azerbaijan', 'Malta', 'North Macedonia', 'San Marino',
    'Netherlands', 'Montenegro', 'Estonia', 'Poland', 'Norway', 'Spain',
    'Austria', 'United Kingdom', 'Italy', 'Albania', 'Hungary', 'Moldova',
    'Ireland', 'Belarus', 'Armenia', 'Romania', 'Cyprus', 'Australia',
    'Russia', 'Germany', 'Belgium', 'Sweden', 'Croatia', 'Lithuania',
    'Serbia', 'Iceland', 'Georgia', 'Greece', 'Latvia', 'Czech Republic',
    'Denmark', 'France', 'Finland', 'Switzerland', 'Slovenia', 'Israel']
columna_2018 = ['Ukraine', 'Azerbaijan', 'Belarus', 'San Marino', 'Netherlands',
    'Macedonia', 'Malta', 'Georgia', 'Spain', 'Austria', 'Denmark',
    'United Kingdom', 'Sweden', 'Latvia', 'Albania', 'Croatia', 'Ireland',
    'Romania', 'Czech Republic', 'Iceland', 'Moldova', 'Belgium', 'Norway',
    'France', 'Italy', 'Australia', 'Estonia', 'Serbia', 'Cyprus',
    'Armenia', 'Bulgaria', 'Greece', 'Hungary', 'Montenegro', 'Germany',
    'Finland', 'Russia', 'Switzerland', 'Israel', 'Poland', 'Lithuania',
    'Slovenia', 'Portugal']
columna_2017 = ['Sweden',
    'Azerbaijan', 'San Marino', 'Latvia', 'Israel', 'Montenegro', 'Albania',
    'Malta', 'Macedonia', 'Denmark', 'Austria', 'Norway', 'Spain',
    'Finland', 'France', 'Greece', 'Lithuania', 'Estonia', 'Moldova',
    'Armenia', 'Bulgaria', 'Iceland', 'Serbia', 'Australia', 'Italy',
    'Germany', 'Portugal', 'Switzerland', 'Netherlands', 'Ireland',
    'Georgia', 'Cyprus', 'Belarus', 'Romania', 'Hungary', 'Slovenia',
    'Belgium', 'Poland', 'United Kingdom', 'Croatia', 'Czech Republic',
    'Ukraine']
columna_2016 = ['Austria', 'Iceland', 'Azerbaijan', 'San Marino', 'Czech Republic',
    'Ireland', 'Georgia', 'Bosnia and Herzegovina', 'Malta', 'Spain',
    'Finland', 'Switzerland', 'Denmark', 'France', 'Moldova', 'Armenia',
    'Cyprus', 'Bulgaria', 'Netherlands', 'Latvia', 'Israel', 'Belarus',
    'Germany', 'Russia', 'Norway', 'Australia', 'Belgium', 'United Kingdom',
    'Croatia', 'Greece', 'Lithuania', 'Serbia', 'Macedonia', 'Albania',
    'Estonia', 'Ukraine', 'Italy', 'Poland', 'Slovenia', 'Hungary',
    'Montenegro', 'Sweden']