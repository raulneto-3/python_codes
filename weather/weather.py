import tkinter as tk
from tkinter import messagebox
import requests

class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Weather App")
        self.geometry("400x200")
        self.configure(bg="white")

        self.label = tk.Label(self, text="Enter city name:", bg="white")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self, bg="white")
        self.entry.pack(pady=10)

        self.button = tk.Button(self, text="Get Weather", command=self.get_weather)
        self.button.pack(pady=10)

    def get_weather(self):
        city = self.entry.get()
        url = f"https://open-weather13.p.rapidapi.com/city/{city}/EN"
        headers = {
            "x-rapidapi-key": "your_api_key",
            "x-rapidapi-host": "open-weather13.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if 'weather' in data:
                weather_info = f"{data['weather'][0]['description']}, {data['weather'][0]['temperature']}°C"
                messagebox.showinfo("Weather Info", weather_info)
            else:
                messagebox.showerror("Error", "City not found")

        else:
            messagebox.showerror("Error", "Something went wrong")

if __name__ == '__main__':
    app = WeatherApp()
    app.mainloop()