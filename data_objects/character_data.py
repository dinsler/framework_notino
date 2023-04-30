import json


class CharacterData:
    def __init__(self, **kwargs):
        self.name = 'Morty Smith' if 'name' not in kwargs.keys() else kwargs['name']
        self.status = 'Alive' if 'status' not in kwargs.keys() else kwargs['status']
        self.species = 'Human' if 'species' not in kwargs.keys() else kwargs['species']
        self.gender = 'Male' if 'gender' not in kwargs.keys() else kwargs['gender']

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
    