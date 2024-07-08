from flask import Blueprint, request, jsonify, current_app
import logging
import os

from ml_services.api.ml_utils import predict_score

# Create a Blueprint
base_blueprint = Blueprint('base', __name__, cli_group=None)

@base_blueprint.route('/')
def root():
    return {'ok': True}

@base_blueprint.route('/predict_score', methods=['POST'])
def predict_score_route():
    logging.info("Received request to predict score")
    data = request.get_json()
    message = data.get('message')
    model_path = current_app.config.get('TORCH_MODEL_PATH')

    if not message:
        return jsonify({'error': 'Invalid input'}), 400

    if not model_path:
        # If model path is not set, return a benign response
        logging.info("Model path is not set, returning dummy success")
        return jsonify({'score': 'dummy_success'}), 200

    if not os.path.exists(model_path):
        # If model path is set but not found, return an error
        logging.error(f"Model path {model_path} not found")
        return jsonify({'error': 'Model path not found'}), 500

    try:
        score = predict_score(message, model_path)
        return jsonify({'score': score}), 200
    except Exception as e:
        logging.error(f"Error predicting score: {str(e)}")
        return jsonify({'error': str(e)}), 500

@base_blueprint.route('/test_connection', methods=['GET'])
def test_connection():
    return jsonify({'message': 'ok'}), 200
