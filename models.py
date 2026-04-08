from pydantic import BaseModel

class Observation(BaseModel):
    query: str

class Action(BaseModel):
    response: str

class Reward(BaseModel):
    score: float