#Importamos las librerias necesarias
import pandas as pd
from fastapi import FastAPI

#Importamos la bases de datos a usar
datatotal = pd.read_csv("datasets/datatotal.csv")

app = FastAPI()

#para activar entorno virtual fastapi-env\Scripts\activate.bat

# uvicorn main:app --reload PARA LEVANTAR SERVIDOR

#Crear ruta para API
#  @ decorador, modifica la funcion que sigue, en este caso la registra

# http://127.0.0.1:8000/   /docs

@app.get('/') #Primera ruta
def get_bienvenida():
    return 'Saludos, aplicacion para hallar diferentes movies y series de plataformas amazon, disney, hulu y netflix. realiza tus busquedas'



#Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(year, platform, duration_type))

@app.get("/duracion/{year}/{platform}/{duration_type}")
def get_max_duration(year:int, platform, duration_type):
    lista=[]
    lista2=[]
    for ind,z in enumerate (datatotal["release_year"]):
        if (z == year):
            if (datatotal["duration_type"][ind] == duration_type):
                if datatotal["ID"][ind][0] == platform:
                     lista.append(int(datatotal["duration_int"][ind]))
                     lista2.append(ind)
                     b = max(lista)
                     c = lista.index(b)
                     d = lista2[c]
                
    return (datatotal["title"][d])


#Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year))
#Volvemos a la funcion
@app.get("/puntaje/{platform}/{scored}/{year}")
def get_score_count(platform, scored:float, year:int):
    lista=[]
    for ind,z in enumerate (datatotal["release_year"]):
        if (z == year):
            if datatotal["ID"][ind][0] == platform:
                if datatotal["score"][ind] > scored:
                     lista.append(float(datatotal["score"][ind]))
                
    return len(lista)

#Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform))
@app.get("/cantidad/{platform}")
def get_count_platform(platform):
    a=0
    for z in (datatotal["ID"]):
        if z[0] == platform:
            a += 1
    return a


#Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))
@app.get("/repeticion/{platform}/{year}")
def get_actor(platform, year:int):
    lista=[]
    lista4 =[]
    b=0
    if platform == "h":
        return("Hulu no tiene base de datos de actores")
    for ind,z in enumerate (datatotal["release_year"]):
        if (z == year):
            if datatotal["ID"][ind][0] == platform:
                lista.append(datatotal["cast"][ind])  #ARMO LISTA EN BASE A PLATAFORMA Y AÑO
    for indice, a in enumerate (lista): #SUBDIVIDO LA LISTA POR CADA NOMBRE
     if type(a)== str:
          lista[indice]= a.split(", ")

    for a in lista:
        if type(a)== list: # ARMO UNA LISTA APARTE SIN LOS NAN
            lista4.append(a)
    flatlist =[elemento for sublista in lista4 for elemento in sublista]  #FLAT
    for ind,a in enumerate(flatlist):  #CON COUNT BUSCO CUAL SE REPITE MAS Y LO RETORNO
        if flatlist.count(a) > b:
            b= flatlist.count(a)
            d= flatlist[ind]
    return(d)
