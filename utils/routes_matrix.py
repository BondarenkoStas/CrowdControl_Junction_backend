import json
import csv
import os

class RoutesMatrix:

    def __init__(self, filepaths):
        self.matrix = {}
        for filepath in filepaths:
            filename = os.path.basename(filepath)
            time = filename.rsplit('.', 1)[0]
            self.matrix[time] = self._create_matrix(filepath)

    def _create_matrix(self, file_name):
        matrix = {}

        with open(file_name, mode='r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            stations = []
            for row_index, row in enumerate(reader):
                if not row_index:
                    stations = row
                else:
                    print(row)
                    matrix[row[0]] = {}
                    for column_index, value in enumerate(row):
                        if column_index:
                            matrix[row[0]][stations[column_index]] = value
        return matrix

    def find_routes(self, base_station, time_frame):
        response = {}
        needed_table = self.matrix.get(time_frame, {})
        for key in needed_table:
            response[key] = {}
            response[key]['moveForward'] = needed_table.get(base_station, {}).get(key)
            response[key]['moveBackward'] = needed_table.get(key, {}).get(base_station)
        return response
        
        

    def get_station_keys(self, time):
        return [key for key in self.matrix[time]]
