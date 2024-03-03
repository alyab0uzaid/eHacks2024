//In the Swift file where you want to access location data, import Core Location:
import CoreLocation

// Create a CLLocationManager instance and set its delegate to receive location updates. 
//We typically do this in a view controller:


class ViewController: UIViewController, CLLocationManagerDelegate {
    let locationManager = CLLocationManager()

    override func viewDidLoad() {
        super.viewDidLoad()

        locationManager.delegate = self
        locationManager.desiredAccuracy = kCLLocationAccuracyBest
    }
}

//Request permission from the user to access their location:

func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
    guard let location = locations.last else { return }
    
    let speed = location.speed // Speed in meters per second

    if speed >= 0 {
        // Speed is a positive value indicating the device is moving
        print("Current speed: \(speed) m/s")
    } else {
        
        // Speed is an invalid value (-1) indicating it could not be determined
        print("Speed could not be determined")
    }
}

override func viewDidAppear(_ animated: Bool) {
    super.viewDidAppear(animated)

    if CLLocationManager.locationServicesEnabled() {
        switch CLLocationManager.authorizationStatus() {
        case .notDetermined:
            locationManager.requestWhenInUseAuthorization() // or requestAlwaysAuthorization()
        case .restricted, .denied:
            // Handle restriction or denial
        case .authorizedWhenInUse, .authorizedAlways:
            // Permission granted
            locationManager.startUpdatingLocation()
        @unknown default:
            fatalError()
        }
    } else {
        // Location services are not enabled
    }
}
func sendLocationToServer(latitude: Double, longitude: Double) {
        // Create a URL with your FastAPI server endpoint
        guard let url = URL(string: "http://0.0.0.0:5000/receive_location") else { # url must be changed here to uvicorn link
            print("Invalid URL")
            return
        }

        // Create a JSON payload with latitude and longitude
        let locationData: [String: Any] = ["lat": latitude, "long": longitude]

        // Convert JSON to Data
        guard let jsonData = try? JSONSerialization.data(withJSONObject: locationData) else {
            print("Failed to serialize JSON data")
            return
        }

        // Create a POST request
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.httpBody = jsonData

        // Send the request
        URLSession.shared.dataTask(with: request) { data, response, error in
            if let error = error {
                print("Error: \(error)")
            } else if let data = data {
                if let responseString = String(data: data, encoding: .utf8) {
                    print("Response: \(responseString)")
                }
            }
        }.resume()
    }
// Implement the CLLocationManagerDelegate methods to handle location updates:
func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
    if let location = locations.last {
        let latitude = location.coordinate.latitude
        let longitude = location.coordinate.longitude
        // Use latitude and longitude
    }
}

func locationManager(_ manager: CLLocationManager, didFailWithError error: Error) {
    // Handle failure to get location
}

//To conserve battery, start and stop location updates as needed:
locationManager.startUpdatingLocation()

//When you no longer need to receive location updates, call:
locationManager.startUpdatingLocation() 
