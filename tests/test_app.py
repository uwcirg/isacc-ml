import unittest

from ml_services.app import create_app

class TestConfig:
    TESTING = True
    SERVER_NAME = 'fhir_server.local'
    SECRET_KEY = 'test_secret_key'
    TORCH_MODEL_PATH = '/path/to/invalid/model'

class TestIsaccMLServicesApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app(testing=True)
        self.app.config.from_object(TestConfig)
        self.client = self.app.test_client()

    def test_app_exists(self):
        self.assertIsNotNone(self.app)

    def test_blueprints_registered(self):
        self.assertIn('base', self.app.blueprints)

    def test_predict_score_route_invalid_input(self):
        response = self.client.post('/predict_score', json={'data': 'not_valid'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid input'})

    def test_predict_score_route_no_input(self):
        response = self.client.post('/predict_score', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid input'})

    def test_predict_score_route_model_path_not_set(self):
        # Remove the model path for this test
        self.app.config['TORCH_MODEL_PATH'] = None
        response = self.client.post('/predict_score', json={'message': 'test message'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Model path not set'})

    def test_predict_score_route_invalid_model_path(self):
        # Set an invalid model path for this test
        self.app.config['TORCH_MODEL_PATH'] = '/invalid/path/to/model'
        response = self.client.post('/predict_score', json={'message': 'test message'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Model path not found'})


if __name__ == '__main__':
    unittest.main()
