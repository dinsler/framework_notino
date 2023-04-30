from data_objects.character_data import CharacterData
from utilities.api.base_api import BaseAPI
from utilities.decorators import allure_step


@allure_step
class CharacterAPI(BaseAPI):
    def __init__(self, env):
        super().__init__(env)
        self.__character_api = '/character'

    def get_character(self, character_id, headers=None):
        response = self.get(url=f'{self.__character_api}/{character_id}', headers=headers)
        return response

    def create_character(self, body=CharacterData(), headers=None, **kwargs):
        body.update_data(**kwargs)
        response = self.post(f'{self.__character_api}/', body=body.get_json(), headers=headers)
        return response
