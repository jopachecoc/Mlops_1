# funcion # diagnosticos.py
# esta funcionn  realia todo el proceso de una manera elelgante y dinamica
# esto se realiza para quititamos eso y lo hacemos de nuevo
# y de nuevo lo amos hacer para que vuelva a aparecer el comentario

def enfermedad1(Presion_sistolica, Presion_diastolica, Pulso, Temperatura):
    categoria = 'SIN CATEGORIA'

    if Presion_sistolica is None:
        Presion_sistolica = 100
    if Presion_diastolica is None:
        Presion_diastolica = 70
    if Pulso is None:
        Pulso = 80
    if Temperatura is None:
        Temperatura = 37

    Presion_sistolica = float(Presion_sistolica)
    Presion_diastolica = float(Presion_diastolica)
    Pulso = float(Pulso)
    Temperatura = float(Temperatura)

    if ((Presion_sistolica < 120 and Presion_diastolica < 80 and Pulso < 100) and (Temperatura < 37.3 or Temperatura <= 36.5)):
        categoria = 'NO ENFERMO'
    if (Presion_sistolica < 120 and Presion_diastolica < 80 and Pulso < 100 and Temperatura >= 37.3):
        categoria = 'ENFERMEDAD LEVE'
    elif (Presion_sistolica < 120 and Presion_diastolica < 80 and Pulso >= 100):
        categoria = 'ENFERMEDAD AGUDA'
    elif (Presion_sistolica >= 120 or Presion_diastolica >= 80):
        categoria = 'ENFERMEDAD CRÓNICA'

    return categoria
## va a correr con exito de una vez ahora si a testea dios mio salvalme
