import SwiftUI
import UIKit
import CoreLocation

class ViewController: UIViewController, CLLocationManagerDelegate {
    private var locationManager: CLLocationManager?
    private let latLngLabel: UILabel = {
        let label = UILabel()
        label.backgroundColor = .systemFill
        label.numberOfLines = 0
        label.textAlignment = .center
        label.font = .systemFont(ofSize: 26)
        return label
    }()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        latLngLabel.frame = CGRect(x: 20, y: view.bounds.height / 2 - 50, width: view.bounds.width - 40, height: 100)
        view.addSubview(latLngLabel)
        
        locationManager = CLLocationManager()
        locationManager?.requestAlwaysAuthorization()
        locationManager?.startUpdatingLocation()
        locationManager?.delegate = self
    }
    
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        if let location = locations.last {
            latLngLabel.text = "lat: \(location.coordinate.latitude) \nLng: \(location.coordinate.longitude)"
        }
    }
}

func sendLocationToServer(latitude: Double, longitude: Double) {
        // Create a URL with your FastAPI server endpoint
    guard let url = URL(string: "http://10.60.2.174:5000/receive_location/\(latitude)/\(longitude)")
    else{
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
        //request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        //request.setValue(apiKey, forHTTPHeaderField: "Authorization")
        //request.httpBody = jsonData

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
