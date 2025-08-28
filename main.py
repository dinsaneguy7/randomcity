from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Allow all origins (for local testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows any domain to access the API
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

cities = [
    { "city": "Kathmandu", "lat": 27.7172, "lon": 85.3240 },
    { "city": "Pokhara", "lat": 28.2096, "lon": 83.9856 },
    # Add more cities as needed...
]

@app.get("/random-city")
def get_random_city():
    random_city = random.choice(cities)
    return random_city
