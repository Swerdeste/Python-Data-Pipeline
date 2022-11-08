import json


class Loader:
    """
    Loader class is used to load the data

    """

    def __init__(self, files):
        self.files = files
        self.out = {}

    def load(self, drugs):
        for drug in drugs:
            self.out[drug] = {}
            for file in self.files:
                if drug in file.keys():
                    for key in file[drug].keys():
                        if key in self.out[drug].keys():
                            self.out[drug][key].extend(file[drug][key])
                        else:
                            self.out[drug][key] = file[drug][key]

    def to_json(self, path):
        with open(path, 'w') as f:
            json.dump(self.out, f)