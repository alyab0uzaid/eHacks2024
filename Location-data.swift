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
