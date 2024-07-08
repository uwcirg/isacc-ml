import unittest
from ml_services.app import create_app

class TestConfig:
    TESTING = True
    SERVER_NAME = 'fhir_server.local'
    SECRET_KEY = 'test_secret_key'
    PREFERRED_URL_SCHEME = 'http'
    TORCH_MODEL_PATH = '/path/to/test/model'

class TestIsaccMLServicesApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app(testing=True)
        self.app.config.from_object(TestConfig)
        self.client = self.app.test_client()

    def test_app_exists(self):
        self.assertIsNotNone(self.app)

    def test_blueprints_registered(self):
        self.assertIn('base', self.app.blueprints)

    def test_predict_score_route_success(self):
        response = self.client.post('/predict_score', json={'message': 'test message'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'score': 'success'})

    def test_predict_score_route_invalid_input(self):
        response = self.client.post('/predict_score', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid input'})

    def test_predict_score_route_missing_message(self):
        response = self.client.post('/predict_score', json={'model_path': '/path/to/test/model'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid input'})

if __name__ == '__main__':
    unittest.main()
