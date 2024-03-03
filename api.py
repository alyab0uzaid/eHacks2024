from fastapi import FastAPI , requests
from pydantic import BaseModel
app = FastAPI()

class LocationData(BaseModel):
    lat: float
    long: float

@app.post("/recieve_location") #receives binformatioon via post
async def recieve_location(location_data: LocationData): #def to get data in async
    print("Received DATA , ""LOCATION_DATA.dict()")
                             #dict used to process data
    return {"message":"Location data recieved succesfully"}

@app.get("/")
async def root():
    return 

print("Running")

if __name__ == "__main__" : 
    import uvicorn
    uvicorn.run(app,host="",port = 5000)



    # Return python dictionary with JSON.