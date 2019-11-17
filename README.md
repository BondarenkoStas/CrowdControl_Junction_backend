https://github.com/MoritzLange/Junction2019 is the initial repository where the work was started. Backend was moved here to be able to deploy it to heroku (it should be in the root of the repository)

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

WARNING: datasets for routes are not full. Evening and Night are present.