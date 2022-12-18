import os, json, requests
import pandas as pd

locations = [(28.645, 77.245) , (28.64 , 77.29) , (28.614 , 77.2089) , (28.676314 , 77.224977) , (28.6936 , 77.3073) , (28.6964 , 77.1271) , (28.5549 , 77.1919) , (28.5531 , 77.2599) , (28.60955 , 77.1367) , (28.6608 , 77.1008)]

output = r""
base_url = r"https://power.larc.nasa.gov/api/temporal/daily/point?parameters=ALLSKY_SFC_LW_DWN,WS50M&community=RE&longitude={longitude}&latitude={latitude}&start=20200101&end=20201231&format=CSV"

for latitude, longitude in locations:
    api_request_url = base_url.format(longitude=longitude, latitude=latitude)

    response = requests.get(url=api_request_url, verify=True, timeout=30.00)

    filename = response.headers['content-disposition'].split('filename=')[1]
    filename += '.csv'
    with open(filename , 'w+') as f:
        f.write(response.text)

    



        
        