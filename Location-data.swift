import HealthKit

class HealthDataCollector {
    
    let healthStore = HKHealthStore()

     // requestAuthorization function requests permission to read heart rate and step count data.
    func requestAuthorization() {
        if HKHealthStore.isHealthDataAvailable() {
            let readTypes: Set<HKObjectType> = [
                HKObjectType.quantityType(forIdentifier: .heartRate)!,
                HKObjectType.quantityType(forIdentifier: .stepCount)!,
                // Add more types as we need
            ]

            healthStore.requestAuthorization(toShare: nil, read: readTypes) { (success, error) in
                if success {
                    self.collectHealthData()
                } else {
                    print("Authorization failed with error: \(String(describing: error))")
                }
            }
        }
    }

    //the saveDataToFile function takes a string data and saves it to 
    //a text file named "health_data.txt" in the app's document directory.
    func saveDataToFile(data: String) {
        let fileName = "health_data.txt"

        if let documentDirectory = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first {
            let fileURL = documentDirectory.appendingPathComponent(fileName)

            do {
                try data.write(to: fileURL, atomically: true, encoding: .utf8)
                print("Data saved to file: \(fileURL.path)")
            } catch {
                print("Error saving data to file: \(error)")
            }
        }

    //  collectHealthData function initiates the collection process, 
    // calling queryHealthData for each specified health metric.

    func collectHealthData() {
        // Query heart rate data
        let heartRateType = HKObjectType.quantityType(forIdentifier: .heartRate)!
        queryHealthData(sampleType: heartRateType)

        // Query step count data
        let stepCountType = HKObjectType.quantityType(forIdentifier: .stepCount)!
        queryHealthData(sampleType: stepCountType)

        // Add more queries for other health metrics as we will need
    }

    func queryHealthData(sampleType: HKSampleType) {
        let query = HKSampleQuery(
            sampleType: sampleType,
            predicate: nil,
            limit: HKObjectQueryNoLimit,
            sortDescriptors: nil
        ) { (query, results, error) in
            if let samples = results as? [HKQuantitySample] {
                for sample in samples {
                    let quantity = sample.quantity
                    let unit = HKUnit.count()
                    let value = quantity.doubleValue(for: unit)
                    
                    // Handle the collected data as needed
                    print("Type: \(sampleType.identifier), Value: \(value)")
                }
            }
        }

        healthStore.execute(query)
    }
}
}

// Example usage
let healthDataCollector = HealthDataCollector()
healthDataCollector.requestAuthorization()

