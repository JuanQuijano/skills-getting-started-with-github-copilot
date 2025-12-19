"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

# FastAPI: framework web para crear APIs en Python
from fastapi import FastAPI, HTTPException

# StaticFiles: sirve archivos estáticos (HTML/CSS/JS) desde una carpeta
from fastapi.staticfiles import StaticFiles

# RedirectResponse: permite redirigir (por ejemplo, "/" -> "/static/index.html")
from fastapi.responses import RedirectResponse

import os
from pathlib import Path

# Instancia principal de la aplicación FastAPI.
# Uvicorn (el servidor ASGI) carga este objeto para exponer las rutas.
app = FastAPI(
    title="Mergington High School API",
    description="API for viewing and signing up for extracurricular activities",
)

# -----------------------------
# Archivos estáticos (frontend)
# -----------------------------
# Directorio donde vive este archivo (src/app.py)
current_dir = Path(__file__).parent

# Monta la carpeta "static" para servirla bajo la URL "/static".
# Ejemplo: /static/index.html -> src/static/index.html
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(current_dir, "static")),
    name="static",
)

# -----------------------------
# "Base de datos" en memoria
# -----------------------------
# Estructura:
# activities[activity_name] = {
#   "description": str,
#   "schedule": str,
#   "max_participants": int,
#   "participants": list[str]
# }
# Nota: al ser en memoria, se pierde al reiniciar el proceso.
activities = {
    # Definimos "activities" como un diccionario que almacena todas las actividades extracurriculares.
    # Cada clave es el nombre de la actividad, y el valor es un diccionario con sus detalles.
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"],
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"],
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"],
    },
    "Soccer Practice": {
        "description": "Team drills, conditioning, and scrimmages",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 22,
        "participants": [],
    },
    "Track & Field": {
        "description": "Sprint, distance, and field event training",
        "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 28,
        "participants": [],
    },
    "Drama Club": {
        "description": "Acting workshops and preparing stage performances",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": [],
    },
    "Art Studio": {
        "description": "Drawing, painting, and mixed-media projects",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 16,
        "participants": [],
    },
    "Debate Team": {
        "description": "Practice structured debates and public speaking",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 14,
        "participants": [],
    },
    "Math Olympiad": {
        "description": "Problem-solving sessions and competition prep",
        "schedule": "Tuesdays, 3:30 PM - 4:45 PM",
        "max_participants": 20,
        "participants": [],
    },
}

# -----------------------------
# Rutas (endpoints)
# -----------------------------
@app.get("/")
def root():
    """Redirige la raíz al frontend estático."""
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    """Devuelve todas las actividades disponibles (con sus participantes)."""
    return activities





@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Apunta a un estudiante (email) a una actividad."""
    
    # 1) Validar que la actividad existe
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # 2) Obtener la actividad concreta
    activity = activities[activity_name]

    # 3) Evitar registros duplicados
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student is already signed up")

    # 4) Validar capacidad máxima antes de añadir
    if len(activity["participants"]) >= activity["max_participants"]:
        raise HTTPException(status_code=400, detail="Activity is full")

    # 5) Añadir el email a la lista de participantes
    activity["participants"].append(email)
    
    return {"message": f"Signed up {email} for {activity_name}"}


# -----------------------------
# Arranque local (opcional)
# -----------------------------
if __name__ == "__main__":
    # Permite ejecutar el servidor con: python3 src/app.py
    # Alternativa típica: uvicorn src.app:app --reload
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)