import json
import csv
import os

class CorrelationMatrix:

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
                    matrix[row[0]] = {}
                    for column_index, value in enumerate(row):
                        if column_index:
                            matrix[row[0]][stations[column_index]] = value
        return matrix

    def find_correlations(self, base_station, time_frame):
        return self.matrix[time_frame][base_station]

    def get_station_keys(self, time):
        return [key for key in self.matrix[time]]
