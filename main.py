meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "PILOS": "Personas Inteligentes en colombia",
            "CAUSA": "Amigo en peru",
    "CHE": "Manera de llamar la atención",
    "COLEGA":"Una manera de llamar a alguien que te cae bien."
            }

print("estas son las palabras disponibles", meme_dict.keys())
palabra = input("Ingresa la palabra que deceas preguntar").upper

if palabra in meme_dict.keys():
    print("lo que significa es:", meme_dict[palabra])
else: 
    print("No esta palabra no esta disponible por el momento")
