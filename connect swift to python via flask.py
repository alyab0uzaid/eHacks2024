from flask import Flask, request

app = Flask(__name) # name must e name importing from?

@app.route('/receive_location', methods=['POST'])
def receive_location():
    if request.method == 'POST':
        location_data = request.get_json()  # Assuming location data is sent as JSON
        # Process the received location data here
        print("Received location data:", location_data)
        return "Location data received successfully", 200
    else:
        return "Invalid request method", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run the server on port 5000

