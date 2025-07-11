import tkinter as tk
from tkinter import messagebox
import requests

# Constants
API_KEY = "enter your api key"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

# Function to fetch and display weather
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    complete_url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        temperature = main["temp"]
        humidity = main["humidity"]
        weather_desc = data["weather"][0]["description"]

        result = f"City: {city}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nCondition: {weather_desc.title()}"
        result_label.config(text=result)
    else:
        result_label.config(text="City not found!")

# GUI Setup
root = tk.Tk()
root.title("Weather Prediction System")
root.geometry("400x300")
root.config(padx=20, pady=20)

# Widgets
title_label = tk.Label(root, text="Enter City Name", font=("Arial", 14))
title_label.pack()

city_entry = tk.Entry(root, font=("Arial", 12))
city_entry.pack(pady=10)

search_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12))
search_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=15)

# Run the app
root.mainloop()
