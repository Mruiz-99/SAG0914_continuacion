import pytest
#from src.app import create_app
from routes.usuario import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({'TESTING': True})
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
