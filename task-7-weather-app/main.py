import os
import sys
import json
import requests
from dotenv import load_dotenv

# Ensure the console outputs UTF-8 correctly (prevents crashes with special characters like ° on Windows)
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

def get_weather(city, api_key):
    """
    Fetches weather data for a given city using OpenWeatherMap API,
    processes the JSON response, and displays it.
    """
    # OpenWeatherMap current weather endpoint
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Query parameters
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Metric unit system ensures temperature is in Celsius
    }
    
    try:
        # Fetch the response from the API
        response = requests.get(url, params=params, timeout=10)
        
        # Check HTTP Status Codes
        if response.status_code == 200:
            # EXPLICITLY use the json library to parse the response text string
            data = json.loads(response.text)
            
            # Extract key details from the JSON structure
            city_name = data["name"]
            country = data["sys"]["country"]
            temperature = data["main"]["temp"]
            condition = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            
            # Display formatted output to the console
            print("\n" + "=" * 40)
            print(f"Weather in {city_name}, {country}:")
            print(f"  - Temperature: {temperature}°C")
            print(f"  - Condition:   {condition.capitalize()}")
            print(f"  - Humidity:    {humidity}%")
            print("=" * 40 + "\n")
            return True
            
        elif response.status_code == 401:
            print("\nError: Invalid API Key. Please verify your OpenWeatherMap API key.\n")
            return False
            
        elif response.status_code == 404:
            print(f"\nError: City '{city}' not found. Please check spelling.\n")
            return False
            
        else:
            print(f"\nError: API returned status code {response.status_code}.\n")
            return False
            
    except requests.exceptions.RequestException:
        # Catch connection timeouts, DNS resolution issues, and network failures
        print("\nError: Network failure. Please check your internet connection.\n")
        return False

def main():
    """
    Main function to run the interactive console weather app.
    """
    # Load environment variables from the .env file
    load_dotenv()
    
    # Retrieve the API key from environment variables
    api_key = os.getenv("OPENWEATHER_API_KEY")
    
    # Check if the API key is configured
    if not api_key or api_key == "your_api_key_here":
        print("\n" + "!" * 50)
        print("Error: Missing OpenWeatherMap API Key!")
        print("Please configure your key in a '.env' file:")
        print("  OPENWEATHER_API_KEY=your_actual_key_here")
        print("Register at https://openweathermap.org/ to get a free key.")
        print("!" * 50 + "\n")
        return

    print("========================================")
    print("           WEATHER APP (Task 7)         ")
    print("========================================")
    print("Type 'exit' to quit the application.\n")
    
    while True:
        try:
            # Prompt the user for city input
            city = input("Enter city name: ").strip()
            
            # Check if user wants to exit
            if city.lower() == "exit":
                print("Exiting application. Goodbye!")
                break
                
            # Handle empty input
            if not city:
                print("Error: City name cannot be empty. Please try again.\n")
                continue
            
            # Retrieve weather
            get_weather(city, api_key)
            
        except (KeyboardInterrupt, EOFError):
            print("\nExiting application. Goodbye!")
            break

if __name__ == "__main__":
    main()
