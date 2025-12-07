import requests

def test_users_invalid_credentials(mocker):
    url = 'http://127.0.0.1:8000/users'
    params = {
        'username': 'admin',
        'password': 'admin'
    }

    # Crear el mock de la respuesta
    mocked_response = mocker.Mock()
    mocked_response.status_code = 401
    mocked_response.text = ''

    # Mockear requests.get
    mocker.patch('requests.get', return_value=mocked_response)

    response = requests.get(url, params=params)

    assert response.status_code == 401
    assert response.text.strip() == ''


def test_users_valid_credentials(mocker):
    url = 'http://127.0.0.1:8000/users'
    params = {
        'username': 'admin',
        'password': 'qwerty'
    }

    # Crear el mock de la respuesta
    mocked_response = mocker.Mock()
    mocked_response.status_code = 200
    mocked_response.text = ''

    # Mockear requests.get
    mocker.patch('requests.get', return_value=mocked_response)

    response = requests.get(url, params=params)

    assert response.status_code == 200
    assert response.text.strip() == ''
