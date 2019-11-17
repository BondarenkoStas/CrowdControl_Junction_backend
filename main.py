import os
from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
from utils.correlation_matrix import CorrelationMatrix
from utils.routes_matrix import RoutesMatrix

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app)

@app.route("/correlation_and_routes")
@cross_origin(origin='*',headers=['access-control-allow-origin','Content-Type'])
def correlation():
    correlation_source_folder = 'data/correlation'
    routes_source_folder = 'data/routes'
    CONST_ROUTES = 5

    base_station = request.args.get('serial')
    time_frame = request.args.get('time')
    number_of_routes = request.args.get('routes', CONST_ROUTES)

    filenames_correlation = [f'{correlation_source_folder}/{file}' for file in os.listdir(correlation_source_folder)]
    filenames_routes = [f'{routes_source_folder}/{file}' for file in os.listdir(routes_source_folder)]

    correlation_matrix = CorrelationMatrix(filenames_correlation)
    station_keys = correlation_matrix.get_station_keys(time_frame)

    routes_matrix = RoutesMatrix(filenames_correlation)

    print(routes_matrix.matrix)

    if base_station and time_frame:
        correlation_tuples = correlation_matrix.find_correlations(base_station, time_frame)
        routes_tuples = routes_matrix.find_routes(base_station, time_frame)

        keys_list = [key for key in correlation_tuples if key != base_station]
        
        summed_routes = {}
        for key in routes_tuples:
            summed_routes[key] = float(routes_tuples[key]['moveForward']) + float(routes_tuples[key]['moveBackward'])
        routes_to_discard = sorted(summed_routes, key=summed_routes.get, reverse=True)[number_of_routes+1:]

        for serial in routes_to_discard:
            routes_tuples[serial] = {}

        return {
            'data': [{
                'serial': serial,
                'correlation': correlation_tuples.get(serial),
                'moveForward': routes_tuples.get(serial, {}).get('moveForward'),
                'moveBackwards': routes_tuples.get(serial, {}).get('moveBackward'),
                } for serial in keys_list],
            'base_station': base_station,
            'time_frame': time_frame
        }

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
