import json
from pathlib import Path
from typing import List

from fastapi import APIRouter, HTTPException

from app.models import City

router = APIRouter(prefix="/api/cities", tags=["cities"])

data_path = Path(__file__).resolve().parent.parent / "data" / "cities.json"

with open(data_path, "r", encoding="utf-8") as f:
    cities_data: List[City] = [City(**c) for c in json.load(f)]


@router.get("", response_model=List[City])
async def get_cities():
    return cities_data


@router.get("/{city_id}", response_model=City)
async def get_city(city_id: int):
    for city in cities_data:
        if city.id == city_id:
            return city
    raise HTTPException(status_code=404, detail="City not found")