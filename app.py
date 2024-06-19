import tkinter as tk
import requests
import time

def getWeather(event=None):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=d1ddbb5255263aa771bbc8ea21aede95"
    
    try:
        json_data = requests.get(api).json()

        # Debug: print the JSON response to inspect its structure
        print(json_data)

        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
        sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

        final_info = f"{condition}\n{temp}°C"
        final_data = (
            f"\nMin Temp: {min_temp}°C\nMax Temp: {max_temp}°C\nPressure: {pressure}"
            f"\nHumidity: {humidity}\nWind Speed: {wind}\nSunrise: {sunrise}\nSunset: {sunset}"
        )
        label1.config(text=final_info)
        label2.config(text=final_data)
    except KeyError as e:
        label1.config(text="Error: Invalid response from the API")
        label2.config(text=f"Details: {str(e)}")
    except Exception as e:
        label1.config(text="Error: Unable to fetch data")
        label2.config(text=f"Details: {str(e)}")

# Tkinter setup
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width=20, font=t)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

get_weather_button = tk.Button(canvas, text="Get Weather", command=getWeather)
get_weather_button.pack()

canvas.mainloop()
