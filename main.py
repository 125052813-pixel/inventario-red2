
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Dispositivo(BaseModel):
    nombre: str
    tipo: str
    ip: str
    activo: bool = True

inventario = []

def buscar(nombre: str):
    for dispositivo in inventario:
        if dispositivo.nombre == nombre:
            return dispositivo
    return None

@app.get("/")
async def inicio():
    return {"mensaje": "Sistema de redes funcionando"}

@app.get("/dispositivos")
async def listar():
    return inventario

@app.post("/dispositivos", status_code=201)
async def crear(nuevo: Dispositivo):
    if buscar(nuevo.nombre) is not None:
        raise HTTPException(
            status_code=409,
            detail=f"Ya existe el equipo {nuevo.nombre}"
        )

    inventario.append(nuevo)
    return nuevo
