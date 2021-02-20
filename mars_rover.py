import requests
import json
import os

fif_fof_curry_sauce_chips_peas_neecey_birthday = '2018-06-09'

ask_nasa = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={fif_fof_curry_sauce_chips_peas_neecey_birthday}&api_key={os.environ['NASA_API_KEY']}"

response = requests.get(ask_nasa)

data = response.json()

for img in data['photos']:
    print(img['img_src'])