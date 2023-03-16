import API
import UI

respuesta = "S"
while respuesta.upper() != "N":
    if respuesta.upper() == "S":
        while (True):
            try:
                limiteRegistros = int (input ("Ingrese la cantidad maxima de registros a mostrar: "))
                if limiteRegistros < 1000:
                    break
                print ("El limite de registros debe ser menor a 1000")
            except:
                print ("ERROR, como limite de registros solo puede ingresar un numero entero positivo")

        nombreDepartamento = input ("Ingrese el departamento al que corresponden los registros: ")
        try:
            dataFrame = API.consultar (nombreDepartamento.upper(), limiteRegistros)
            UI.printDataFrame(dataFrame)
        except:
            print ("ERROR, el departamento ingresado no existe o fue mal digitado (no debe tener tildes ni otros caracteres especiales)")
    else:
        print ("Respuesta invalida")
    respuesta = input ("Desea hacer otra consulta? (S/N) ")