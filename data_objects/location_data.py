import json


class LocationData:
    def __init__(self, **kwargs):
        self.name = 'Earth (C-137)' if 'name' not in kwargs.keys() else kwargs['name']
        self.type = 'Planet' if 'type' not in kwargs.keys() else kwargs['type']
        self.dimension = 'Dimension C-137' if 'dimension' not in kwargs.keys() else kwargs['dimension']

    @classmethod
    def from_json(cls, **kwargs):
        return cls(**kwargs)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def get_json(self):
        return json.dumps(self.__dict__)

    def update_data(self, **kwargs):
        self.__dict__.update(**kwargs)

    def get_dict(self):
        return self.__dict__
