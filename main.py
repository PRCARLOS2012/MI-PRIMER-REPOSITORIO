#DICCIONARIO

meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "Es cuando algo es muy random",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación o decepcion",
            "CREEPY": "aterrador, siniestro y terrorifico",
            "AGGRO": "ponerse agresivo/enojado",
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("La palabra no se encuentra, recuerda poner las letras en mayuscula.")
