import yaml


def loads_json(filepath: str):
    """
    Load a json file using Yaml package to deal with possible trailing commas.
    :param config: dict
        Parameters to open the file (path, encoding)
    :return: data: json
        The deserialized file as python object according to JSONDecoder conversion table.
    """
    with open(filepath, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data
