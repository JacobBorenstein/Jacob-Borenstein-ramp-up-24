from fastapi import FastAPI

api = FastAPI()

@api.get('/{name}')
async def root(name:str):
    return f"Hello {name}"
