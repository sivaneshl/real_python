import matplotlib.pyplot as plt
import pandas as pd
import requests

url = "https://api.midway.tomtom.com/ranking/live/IND_chennai"
req = requests.get(url)
json_obj = req.json()

# the json file is actually a dictionary called ‘data’, with a list of dictionaries contained within it
#  - “Time”, “TrafficIndexLive” and “TrafficIndexHistoric”, have to call the keys for each point we want to retrieve
i = 0
live_traffic = []
times = []
while i < len(json_obj['data']):
    current_data = json_obj["data"][i]
    live_traffic.append(current_data["TrafficIndexLive"])
    times.append(current_data["UpdateTime"])
    i += 1

# convert to df
df = pd.DataFrame({"Live Traffic": live_traffic}, index=times)
df.index = pd.to_datetime(df.index, unit="ms")
df.index.name = "Time"
print(df.head())

# plot graph
plt.style.use('seaborn')
ax = df.plot()
plt.title("Chennai traffic")
plt.show()

