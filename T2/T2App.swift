import SwiftUI
import UIKit
import CoreLocation

struct ViewControllerWrapper: UIViewControllerRepresentable {
    func makeUIViewController(context: Context) -> ViewController {
        sendLocationToServer(latitude: 37.785834, longitude: -122.406417)
        return ViewController()
    }
    
    func updateUIViewController(_ uiViewController: ViewController, context: Context) {
        // Update the view controller if needed
    }
}

@main
struct T2App: App {
    var body: some Scene {
        WindowGroup {
            ViewControllerWrapper()
        }
    }
}
