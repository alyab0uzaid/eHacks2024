from fastapi import FASTAPI , requests
from pydantic import BaseModel
app = FASTAPI()

class LocationData(BaseModel):
    lat: float
    long: float

@app.post("/recieve_location") #receives binformatioon via post
async def recieve_location(location_data: LocationData): #def to get data in async
    print("Received DATA , ""LOCATION_DATA.dict()")
                             #dict used to process data
    return{"message":"Location data recieved succesfully"}

if __name__ == "__main__" : 
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port = 5000)
    
          

