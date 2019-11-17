import json
from random import seed, random
from datetime import datetime, timedelta

class RoutesMatrix:

    def __init__(self):
        seed(1)
        self.time_keys = self.get_time_keys()
        self.station_keys = self.get_station_keys()
        self.matrix = self._create_matrix()

    def _create_matrix(self):
        data = {}
        for time_key in self.time_keys:
            data[time_key] = {}
            for i in self.station_keys:
                data[time_key][i] = {}
                for j in self.station_keys:
                    data[time_key][i][j] = {
                        'moveForward': random(),
                        'moveBackward': random()
                    }
        return data

    def find_routes(self, base_station, time_frame):
        return self.matrix[time_frame][base_station]

# change for real data
    def get_time_keys(self):
        return ['m', 'n', 'e', 'd']

# change for real data
    def get_station_keys(self):
        stations = {'0000000006dd41f6': 'Hernesaari LHC',
                    '000000000f4919c9': 'Amos Rex',
                    '0000000019fb59c4': 'Lansiterminaali 1',
                    '00000000342570c2': 'Sibelius Monumentti',
                    '0000000038bf9618': 'Kaivopuiston ranta',
                    '0000000038d83d41': 'Pakkahuoneenlaituri',
                    '000000004ef3150d': 'Lansiterminaali 2',
                    '0000000053c6c2be': 'Katajanokan laituri 2',
                    '00000000675d5200': 'Hakaniemen kauppahalli 1',
                    '000000006b087f40': 'Ateneum',
                    '000000006b44cce7': 'Kauppatori',
                    '0000000074f765a7': 'Oodi',
                    '000000007b5207b6': 'Hakaniemen kauppahalli 2',
                    '0000000096918cfa': 'Temppeliaukion kirkko',
                    '00000000a53ed894': 'Hernesaari LHD',
                    '00000000aa852af1': 'Senaatintori lantinen',
                    '00000000afef4555': 'Stockmann',
                    '00000000b33a8357': 'Kamppi',
                    '00000000cd16b8ef': 'Senaatintori itainen',
                    '00000000d747f075': 'Katajanokan terminaali',
                    '00000000e8a064a4': 'Hernesaari LHB',
                    '00000000f1124bca': 'Olympiaterminaali',
                    '00000000fb7600be': 'Katajanokan laituri',
                    '00000000fdda10fe': 'Dianapuisto',
                    '00000000fffb8cf0': 'Suomenlinna'
        }
        return [key for key in stations]
