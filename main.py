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
    import sys
    print(sys.modules[__name__])


    source_folder = 'data/correlation'

    base_station = request.args.get('serial')
    time_frame = request.args.get('time')

    filenames = [f'{source_folder}/{file}' for file in os.listdir(source_folder)]

    correlation_matrix = CorrelationMatrix(filenames)
    station_keys = correlation_matrix.get_station_keys(time_frame)

    routes_matrix = RoutesMatrix()

    if base_station and time_frame:
        correlation_tuples = correlation_matrix.find_correlations(base_station, time_frame)
        routes_tuples = routes_matrix.find_routes(base_station, time_frame)

        keys_list = [key for key in correlation_tuples if key != base_station]

        return {
            'data': [{
                'serial': serial,
                'correlation': correlation_tuples[serial],
                'moveForward': routes_tuples[serial]['moveForward'],
                'moveBackwards': routes_tuples[serial]['moveBackward'],
                } for serial in keys_list],
            'base_station': base_station,
            'time_frame': time_frame
        }

if __name__ == "__main__":
    app.run(debug=True, host= '0.0.0.0')
