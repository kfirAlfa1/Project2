from datetime import datetime, timedelta
from easygui import enterbox, buttonbox
import sys
import api  

current_date = datetime.now()
date_list = []

# Populate date list with next 6 days
for i in range(6):  
    date_list.append(current_date.strftime('%Y-%m-%d'))
    current_date += timedelta(days=1)

title = "Forecast for the next 5 days"
message_for_input_box = "Hi and welcome to Kfir's forecast project.\nPlease enter a name of a city in Israel where you'd like to know the weather:"
city_name = enterbox(message_for_input_box, title)
if city_name is None:
    sys.exit()

api.get_lon_and_lat(city_name)

forecast_data_for_five_days = api.get_data_for_5_days(api.lat, api.lon)
button_list = date_list[1:]

message_for_main_window = f"Thank you for your choice!\nHere is the forecast for today in: {city_name}\n\n"
message_for_main_window += api.get_forecast_for_now(api.lat, api.lon) + "\n "
user_choice = buttonbox(message_for_main_window, title, button_list)

# Loop until user choose to exit
while True:
    forecast = api.get_forecast_for_specific_date(forecast_data_for_five_days, user_choice)
    forecast_to_show = f"The weather for: {user_choice} in {city_name}\n"
    forecast_to_show += api.get_max_temperature(forecast) + '\n' 
    forecast_to_show += api.get_min_temperature(forecast) + '\n'
    forecast_to_show += api.get_average_humidity(forecast) + '\n'
    forecast_to_show += api.get_weather_description(forecast)
    user_choice = buttonbox(forecast_to_show, title, button_list)

    if user_choice is None:
       break
