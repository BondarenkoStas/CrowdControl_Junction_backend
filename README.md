## Setup

if you use pip3, install requirements with
`cd backend`
`pip3 install -r requirements.txt`

if you have python3
`python3 main.py`

this will run it on localhost (default port 5000)
share it with ngrok
`ngrok http 127.0.0.1:5000`

## endpoints

`/correlation` returns correlation between every station on every timeentry

`/correlation?from=station_1&to=station_3` will return every timeentry correlation between station_1 and station_3 (one way relation)

`correlation?from=station_1&to=station_3&start=2019-11-16%2018:11:56&finish=2019-11-16%2023:00:00` will return timeentries between start and finish between station_1 and station_3. Time is in the format %Y-%m-%d %H:%M:%S.