import pytest
import connexion

flask_app = connexion.FlaskApp(__name__)
flask_app.add_api('../../../app/server/swagger.yml')


@pytest.fixture(scope='module')
def client():
    with flask_app.app.test_client() as c:
        yield c


def test_people_endpoint(client):
    response = client.get('/api/people')
    assert response.status_code == 200
