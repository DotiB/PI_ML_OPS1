from fastapi import FastAPI
import pandas as pd
import numpy as np

movies_df = pd.read_csv("movies_ETL.csv")
###http://127.0.0.1:8000
###uvicorn main:app --reload
app = FastAPI()

@app.get("/")
def read_root():
    return {"Message": "Help"}

@app.get("/language/{Idioma}")

def peliculas_idioma(Idioma: str):
    movie_q = len(movies_df.loc[movies_df["original_language"] == Idioma].index)
    return {"Idioma": Idioma, "Cantidad_Peliculas": movie_q}



