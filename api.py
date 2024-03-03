from fastapi import FastAPI , requests
from pydantic import BaseModel
import GoogleAPI
app = FastAPI()

class LocationData(BaseModel):
    lat: float
    long: float

@app.post("/receive_location/{lat}/{long}") #receives binformatioon via post
async def receive_location(lat, long): #def to get data in async
    print("Received DATA , ""LOCATION_DATA.dict()")
    print(lat, "  ", long)
    Location = GoogleAPI.get_nearby_places(lat, long, 15)

                             #dict used to process data
    return {
        "message":"Location data recieved succesfully",
        "playlistID": "an ID",
        "Location:" : Location,
    }

@app.get("/")
async def root():
    return 

print("Running")

if __name__ == "__main__" : 
    import uvicorn  
    uvicorn.run(app,host="",port = 5000)



    # Return python dictionary with JSON.