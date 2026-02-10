# triage.py (en rama vision-model) 
import tensorflow as tf

def clasificar_imagen(img):
    # Proximamente: Modelo de Red Neuronal
    return "Lesion detectada"

# triage.py - Logica inicial
def evaluar_prioridad(sintomas):
    if "fiebre_alta" in sintomas and "disnea" in sintomas:
        return "PRIORIDAD 1 - Emergencia" 
    return "PRIORIDAD 3 - Estable"

print(evaluar_prioridad(["fiebre_alta", "disnea"]))