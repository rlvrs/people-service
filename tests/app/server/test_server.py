import pytest
import connexion

flask_app = connexion.FlaskApp(__name__)

project_root_path = "../../.."
project_server_path = "app/server"
openapi_filename = "swagger.yml"
openapi_path = "{0}/{1}/{2}".format(project_root_path, project_server_path, openapi_filename)
flask_app.add_api(openapi_path)


@pytest.fixture(scope='module')
def client():
    with flask_app.app.test_client() as c:
        yield c


def test_people_endpoint(client):
    response = client.get('/api/people')
    assert response.status_code == 200
