import requests
from datetime import datetime
import tkinter as tk

# Function to get weather data
def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()
    
    if weather_data["cod"] != "404":
        main = weather_data["main"]
        wind = weather_data["wind"]
        weather_desc = weather_data["weather"][0]["description"]
        
        temp = main["temp"]
        humidity = main["humidity"]
        wind_speed = wind["speed"]
        
        return f"Temperature: {temp}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s\nDescription: {weather_desc.capitalize()}"
    else:
        return "City Not Found"

# Function to update the weather, time, and date
def update_info():
    # Get current date and time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Get weather info (change 'YOUR_CITY' and 'YOUR_API_KEY')
    city = "YOUR_CITY"  # Replace with your city
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    weather_info = get_weather(city, api_key)
    
    # Update labels
    time_label.config(text=current_time)
    weather_label.config(text=weather_info)
    
    # Refresh every 60 seconds
    root.after(60000, update_info)

# Setup GUI
root = tk.Tk()
root.title("Weather, Date & Time")

# Labels for displaying time, date, and weather
time_label = tk.Label(root, font=("Helvetica", 18))
time_label.pack(pady=10)

weather_label = tk.Label(root, font=("Helvetica", 14), justify="left")
weather_label.pack(pady=10)

# Start updating the info
update_info()

# Run the GUI loop
root.mainloop()


#sudo apt-get update  bash line(Make sure your package list is up to date)
#sudo apt-get install python3-pip  bash line(This installs pip for Python 3, which allows to install third party Python libraries, such as requests)
#pip3 install requests   bash line(This command line uses pip to install requests library, which is neccessary for the program to interact with the OpenWeatherMap API.)
#python3 weather_display.py   bash line(This script allows  you to run it on the rasperryPi)

#Once you install the above libraries then replace using the placeholders listed below:
#Replace "YOUR_CITY" with the name of your city.
#Replace "YOUR_API_KEY" with your OpenWeatherMap API key.
#Run the script. Save the code in a file, e.g., weather_display.py, and run it on your Raspberry Pi. This will update the date, time and weather every 60 seconds.

