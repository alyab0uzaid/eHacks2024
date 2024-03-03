from fastapi import FastAPI , requests
from pydantic import BaseModel
import GoogleAPI 
from main import App

app = FastAPI()


@app.post("/receive_location/{lat}/{long}/{mode}") #receives binformatioon via post
async def receive_location(lat, long, mode): #def to get data in async
    print("Received DATA , ""LOCATION_DATA.dict()")
    print(lat, "  ", long, " ", mode)
    Location = GoogleAPI.get_nearby_places_with_distance(lat, long, 15)
   
                             #dict used to process data
    if mode == "Gym" and  GoogleAPI.places_info_list and GoogleAPI.places_info_list[0]['name'] == "Student Fitness Center":
        return{
            "Spotify URL" : "Here goes spotify URL",
            "Location:" : Location[0],
        }
    elif mode == "Chill":  
        return {
         "Spotpify URL" : "Here goes spotify URL",
        "Location:" : Location[0],
    }
    elif mode == "Library" and  GoogleAPI.places_info_list and GoogleAPI.places_info_list[0]['name'] == "Student Fitness Center":
        return {
        "Spotify URL" : "Here goes spotify URL",
        "Location:" : Location[0],
    }
    

@app.get("/")
async def root():
    return 

print("Running")

if __name__ == "__main__" : 
    import uvicorn  
    uvicorn.run(app,host="",port = 5000)
