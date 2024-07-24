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
    data = request.get_json()
    if not data:
        return jsonify({'response': 'invalid input'}), 400
    message = data.get('message')
    #model_path = current_app.config.get('TORCH_MODEL_PATH')
    model_path = '/opt/app/config/models/model_for_isacc'
    if not message:
        return jsonify({'error': 'Invalid input'}), 400

    if not model_path:
        # If model path is not set and predict is called, return an error
        return jsonify({'error': 'Model path not set'}), 400

    if not os.path.exists(model_path):
        # If model path is set but not found, return an error
        return jsonify({'error': 'Model path not found'}), 400

    try:
        score = predict_score(message, model_path)
        return jsonify({'score': int(score)}), 200
    except Exception as e:
        logging.error(f"Error predicting score: {str(e)}")
        return jsonify({'error': str(e)}), 500


@base_blueprint.cli.command("test_connection")
def test_connection_cli():
    logging.info(f"Tested connection via command")
    result = test_connection()
    return result


@base_blueprint.route('/test_connection', methods=['GET'])
def test_connection_route():
    logging.info(f"Tested connection via route")
    result = test_connection()
    return result


def test_connection():
    return jsonify({'message': 'ok'}), 200
