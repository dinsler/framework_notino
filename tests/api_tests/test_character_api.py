from http import HTTPStatus

import pytest

from api_collections.character_api import CharacterAPI
from data_objects.character_data import CharacterData


@pytest.mark.smoke
def test_get_character(env, character_mock):
    expected_character = character_mock
    response = CharacterAPI(env).get_character(2)
    response_data = response.json()
    actual_character = CharacterData.from_json(**response_data)
    assert response.status_code == HTTPStatus.OK, 'Status code is not as expected'
    assert actual_character == expected_character, 'Character Data is not as expected'


@pytest.mark.smoke
def test_get_non_existent_character(env):
    response = CharacterAPI(env).get_character(1534)
    assert response.status_code == HTTPStatus.NOT_FOUND, 'Status code is not as expected'
    assert response.json().get('error') == 'Character not found'
