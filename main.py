from fastapi import FastAPI
import uvicorn
from models.cars import Cars
from routers.sell_car import router as routerSell
from routers.cars import router as routerCar
from routers.financial import router as routerFinancial
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://automororesirigoyen-website.vercel.app",
    "https://automotoresyrigoyen.com",
    "automotoresyrigoyen.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def read_root():
    return {"message": "Automotores Yrigoyen API by iWeb Techonology. All rights reserved"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

app.include_router(routerCar)
app.include_router(routerSell)
app.include_router(routerFinancial)