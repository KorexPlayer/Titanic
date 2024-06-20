def leer_archivos(archivo):
    ent = open(archivo, 'r', encoding="UTF-8")
    seres = []
    for lines in ent:
        line = lines.rstrip("\n").split(",")
        seres.append(line)
    seres.pop(-1)
    ent.close()
    return seres
def cantidad_sobrevivientes(personas):
    i = 0
    viva = 0
    while i < len(personas):
        if personas[i][1] == "1":
            viva += 1
        i += 1
    return viva
def cantidad_mujeres(personas):
    i = 0
    mujeres = 0
    while i < len(personas):
        if personas[i][3] == "female":
            mujeres += 1
        i += 1
    return mujeres
def cantidad_hombres(personas):
    i = 0
    hombres = 0
    while i < len(personas):
        if personas[i][3] == "male":
            hombres += 1
        i += 1
    return hombres
def cant_pasajeros_prim_class(personas):
    i = 0
    prim_class = 0
    while i < len(personas):
        if personas[i][0] == "1":
            prim_class += 1
        i += 1
    return prim_class
def cant_pasajeros_segu_class(personas):
    i = 0
    segu_class = 0
    while i < len(personas):
        if personas[i][0] == "2":
            segu_class += 1
        i += 1
    return segu_class
def cant_pasajeros_terc_class(personas):
    i = 0
    terc_class = 0
    while i < len(personas):
        if personas[i][0] == "3":
            terc_class += 1
        i += 1
    return terc_class
def cant_pasajeros_emb_cherb(personas):
    i = 0
    emb_cherb = 0
    while i < len(personas):
        if personas[i][10] == "C":
            emb_cherb += 1
        i += 1
    return emb_cherb
def cant_pasajeros_emb_queen(personas):
    i = 0
    emb_queen = 0
    while i < len(personas):
        if personas[i][10] == "Q":
            emb_queen += 1
        i += 1
    return emb_queen
def cant_pasajeros_emb_south(personas):
    i = 0
    emb_south = 0
    while i < len(personas):
        if personas[i][10] == "S":
            emb_south += 1
        i += 1
    return emb_south
if __name__ == "__main__":
    personas = leer_archivos("titanic3_nuevo.txt")
    sobrevivio = cantidad_sobrevivientes(personas)
    mujer = cantidad_mujeres(personas)
    hombre = cantidad_hombres(personas)
    primera_clase = cant_pasajeros_prim_class(personas)
    segunda_clase = cant_pasajeros_segu_class(personas)
    tercera_clase = cant_pasajeros_terc_class(personas)
    cherburgo = cant_pasajeros_emb_cherb(personas)
    queenstown = cant_pasajeros_emb_queen(personas)
    southampton = cant_pasajeros_emb_south(personas)
    print(f"""Cantidad de personas a bordo: {len(personas)}
              Cantidad de sobrevivientes: {sobrevivio}
              Cantidad de mujeres: {mujer}
              Cantidad de hombres: {hombre}
              Cantidad de personas en primera clase: {primera_clase}
              Cantidad de personas en segunda clase: {segunda_clase}
              Cantidad de personas en tercera clase: {tercera_clase}
              Cantidad de personas que embarcaron en Cherburgo: {cherburgo}
              Cantidad de personas que embarcaron en Queenstown: {queenstown}
              Cantidad de personas que embarcaron en Southampton: {southampton}""")