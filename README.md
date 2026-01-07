# 🚲 TFL BikePoint API Project

A Python project that uses with the Transport for London (TfL) Unified API to retrieve real-time BikePoint (Santander Cycles) data, exports the results to a JSON file, and maintains detailed execution logs.

## ✨ Features

* **Automated API Calls:** Fetches live data from the `/BikePoint` endpoint.
* **JSON Export:** Saves structured data including bike availability, dock status, and coordinates.
* **Robust Logging:** Implements the Python `logging` module to track successful runs, API timeouts, and errors.
* **Error Handling:** Gracefully handles connection issues or invalid API responses using `try-except` blocks.

---

## 🛠 Steps

### API Interaction

The script uses the url:

> `https://api.tfl.gov.uk/BikePoint`

Documentation found here: [TfL Swagger UI](https://api.tfl.gov.uk/swagger/ui/#!/BikePoint/BikePoint_GetAll)

The output is saved as a JSON file, example output:

```json
[
  {
    "id": "BikePoints_1",
    "commonName": "River Street, Clerkenwell",
    "lat": 51.529163,
    "lon": -0.10997,
    "additionalProperties": [
      { "key": "NbBikes", "value": "12" },
      { "key": "NbEmptyDocks", "value": "7" }
    ]
  }
]

```

### Logging Implementation

The project uses a standard logging configuration to track internal events:

* **INFO:** Records start times, successful data fetches, and file save locations.
* **ERROR:** Captures API timeouts or response codes/statuses.

### Error Handling

The script is built with a **Try-Except block** to ensure it doesnt attempt to output a JSON file if an error in calling the API has occured.

A **while loop** is also used to limit the number of attempts to call the API to 3, avoiding any unnessessary calls in case of a system error/outage. The script will wait 10s before attempting to try the API call again.


