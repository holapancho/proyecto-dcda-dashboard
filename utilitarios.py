# Metodos utilizarios para manipular columnas del dataframe

def convertirDataframeColumnaObjectAInt(df, nombre_columna):
    df[nombre_columna] = df[nombre_columna].astype(str).replace('-','0').replace('nan','0').astype(int)

def convertirDataframeColumnaObjectAFloat(df, nombre_columna):
    df[nombre_columna] = df[nombre_columna].astype(str).replace('-','0').replace('nan','0').astype(float)

def convertirDataframeColumnaObjectAString(df, nombre_columna):
    df[nombre_columna] = df[nombre_columna].astype('string')