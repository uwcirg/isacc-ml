# ML ISACC Service

This repository contains a Flask-based microservice that provides machine learning utilities for the ISACC service. The primary function of this service is to handle text classification tasks using a pre-trained BERT model. The service exposes an endpoint to predict scores for given input text messages.

## Installation

```bash
git clone https://github.com/uwcirg/isacc-ml
cd isacc-ml
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Usage
```bash
FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
The service will be available at http://0.0.0.0:8000.

## Endpoint
```POST <ISACC_ML_HOST>/predict_score```
Predicts the score for a given text message.

### Request:
```bash
ISACC_ML_HOST=<ISACC ML address here>
curl -X POST $ISACC_ML_HOST/predict_score \
-H "Content-Type: application/json" \
      -d '{
           "message": "Your input message here"
         }'
```

### Response:
- Status: 200 OK
- Body:
```json
{
    "score": <predicted_score>
}
```

## Configuration
Modify isacc-ml/config.py for configuration settings.
