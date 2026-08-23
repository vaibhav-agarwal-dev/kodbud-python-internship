# Task 7 — Weather App (Simplified)

A beginner-friendly console application written in Python that fetches and displays the current weather for a user-specified city. This project is structured specifically to make it easy to explain in internship demo/walkthrough videos.

---

## Features

- **API Requests**: Uses the `requests` library to fetch current weather details from the **OpenWeatherMap API**.
- **JSON Processing**: Explicitly uses Python's built-in `json` module to parse the response text string.
- **Environment Variables**: Secures the API key in a `.env` file loaded via the `python-dotenv` package.
- **Clean Console Output**: Displays the city name, country, temperature in Celsius, weather description, and humidity.
- **Robust Error Handling**:
  - Checks for a missing API key before startup.
  - Detects network/request failure.
  - Catches invalid API keys (HTTP 401).
  - Handles invalid city names (HTTP 404).

---

## Code Structure

Everything is contained in a single file: **[`main.py`](file:///d:/Kodbud-Python-Internship/task-7-weather-app/main.py)**.
- `get_weather(city, api_key)`: Sends the API request, handles exceptions, parses the response with `json.loads()`, and prints the weather details.
- `main()`: Loads environment variables, validates the API key, and runs the interactive input prompt loop.

---

## Installation & Setup

### 1. Register for an API Key
1. Go to [OpenWeatherMap](https://openweathermap.org/) and create a free account.
2. Navigate to your profile dashboard to locate your API Key.

### 2. Configure Environment variables
1. Create a file named `.env` in this directory:
   ```bash
   cd task-7-weather-app
   ```
2. Copy the contents of `.env.example` to `.env` or write:
   ```env
   OPENWEATHER_API_KEY=your_actual_api_key_here
   ```

### 3. Install Dependencies
Install the required packages using pip:
```bash
pip install -r requirements.txt
```

---

## Running the Application

Execute the application:
```bash
python main.py
```

### Example Usage:
```text
========================================
           WEATHER APP (Task 7)         
========================================
Type 'exit' to quit the application.

Enter city name: Paris

========================================
Weather in Paris, FR:
  - Temperature: 18.2°C
  - Condition:   Overcast clouds
  - Humidity:    78%
========================================
```
