import pandas as pd
from sodapy import Socrata

def consultar (nombreDepartamento, limiteRegistros):
    client = Socrata("www.datos.gov.co", None)
    results = client.get("gt2j-8ykr", limit = limiteRegistros, departamento_nom = nombreDepartamento)
    return (pd.DataFrame.from_records(results))