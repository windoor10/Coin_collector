from pydantic import BaseModel, Field
from typing import List
from pathlib import Path

class Vec2(BaseModel):
    x: int
    y: int

class Coin(BaseModel):
    x: int
    y: int
    r: int = Field(ge=3, le=30)

class Wall(BaseModel):
    x: int
    y: int
    w: int = Field(gt=0)
    h: int = Field(gt=0)

class Level(BaseModel):
    width: int = Field(default=800, ge=320, le=1920)
    height: int = Field(default=600, ge=240, le=1080)
    player_start: Vec2 = Field(default_factory=lambda: Vec2(x=50, y=50))
    coins: List[Coin]
    walls: List[Wall] = []

def load_level(path: str) -> Level:
    import json
    # Normalisiere den Pfad zu einem absoluten Pfad
    path_obj = Path(path).resolve()
    
    if not path_obj.exists():
        raise FileNotFoundError(f"Level-Datei nicht gefunden: {path_obj}\n(Eingabe: {path})")
    
    with open(path_obj, "r", encoding="utf-8") as f:
        data = json.load(f)
    return Level.model_validate(data)