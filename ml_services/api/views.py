from flask import Blueprint, request, jsonify, current_app
from ml_services.api.ml_utils import predict_score
import os

# Create a Blueprint
base_blueprint = Blueprint('base', __name__, cli_group=None)

@base_blueprint.route('/')
def root():
    return {'ok': True}

@base_blueprint.route('/predict_score', methods=['POST'])
def predict_score_route():
    print("Predicting the score")
    data = request.get_json()
    message = data.get('message')
    model_path = current_app.config.get('TORCH_MODEL_PATH')

    if not model_path or not message:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        score = predict_score(message, model_path)
        return jsonify({'score': score}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@base_blueprint.route('/test_connection', methods=['GET'])
def test_connection():
    return jsonify({'message': 'ok'}), 200
