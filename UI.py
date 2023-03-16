def printDataFrame (dataFrame):
    dataFrame.rename(columns = {"departamento_nom": "Departamento"}, inplace = True)
    dataFrame.rename(columns = {"ciudad_municipio_nom": "Municipio"}, inplace = True)
    dataFrame.rename(columns = {"edad": "Edad"}, inplace = True)
    dataFrame.rename(columns = {"fuente_tipo_contagio": "Tipo de contagio"}, inplace = True)
    dataFrame.rename(columns = {"estado": "Estado"}, inplace = True)
    if 'pais_viajo_1_nom' not in dataFrame:
        dataFrame ['Pais'] = ""
    else:
        dataFrame.rename(columns={"'pais_viajo_1_nom'": "Pais"}, inplace=True)
    dataFrame = dataFrame [["Departamento", "Municipio", "Edad", "Tipo de contagio", "Estado", "Pais"]]
    print(dataFrame.to_string(index = False))