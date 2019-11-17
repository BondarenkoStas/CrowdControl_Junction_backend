## Setup

if you use pip3, install requirements with
`cd backend`
`pip3 install -r requirements.txt`

if you have python3
`python3 main.py`

this will run it on localhost (default port 5000)
share it with ngrok, localtunnel or deploy to heroku to make accesible over internet

## endpoints

`/correlation` returns correlation between every station on every timeentry

`/correlation?serial=serial&time=time_frame` will return every correlation and routes for the station with given timeframe

optional parameter is `routes` to define the number of routes to return.