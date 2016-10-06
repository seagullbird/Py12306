import re
import requests
from pprint import pprint

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955'
r = requests.get(url, verify=False)
stations = re.findall(r'([A-Z]+)\|([a-z]+)', r.text)
stations = dict(stations)
# switch keys and values
stations = dict(zip(stations.values(), stations.keys()))
# indent: The amount of indentation
pprint(stations, indent=4)