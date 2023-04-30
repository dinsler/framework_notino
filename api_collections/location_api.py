from data_objects.location_data import LocationData
from utilities.api.base_api import BaseAPI
from utilities.decorators import allure_step


@allure_step
class LocationAPI(BaseAPI):
    def __init__(self, env):
        super().__init__(env)
        self.__location_api = '/location'

    def get_location(self, location_id, headers=None):
        response = self.get(url=f'{self.__location_api}/{location_id}', headers=headers)
        return response

    def create_location(self, body=LocationData(), headers=None, **kwargs):
        body.update_data(**kwargs)
        response = self.post(f'{self.__location_api}/', body=body.get_json(), headers=headers)
        return response
