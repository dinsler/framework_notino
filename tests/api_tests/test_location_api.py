from http import HTTPStatus

import pytest

from api_collections.location_api import LocationAPI
from data_objects.location_data import LocationData


@pytest.mark.smoke
def test_get_location(env, location_mock):
    expected_location = location_mock
    response = LocationAPI(env).get_location(1)
    response_data = response.json()
    actual_location = LocationData.from_json(**response_data)
    assert response.status_code == HTTPStatus.OK, 'Status code is not as expected'
    assert actual_location == expected_location, 'Location Data is not as expected'


@pytest.mark.smoke
def test_get_non_existent_location(env):
    response = LocationAPI(env).get_location(1123)
    assert response.status_code == HTTPStatus.NOT_FOUND, 'Status code is not as expected'
    assert response.json().get('error') == 'Location not found'
