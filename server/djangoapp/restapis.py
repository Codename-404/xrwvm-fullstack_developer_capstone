# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv
from typing import Any, Dict, Optional

load_dotenv()

backend_url: str = os.getenv('backend_url', default='http://localhost:3030')
sentiment_analyzer_url: str = os.getenv(
    'sentiment_analyzer_url', default='http://localhost:5050/')


def get_request(endpoint: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
    """Make a GET request to the backend"""
    params = ''
    if kwargs:
        for key, value in kwargs.items():
            params += f'{key}={value}&'

    request_url = f'{backend_url}{endpoint}?{params}'

    print(f'GET from {request_url}')
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f'Unexpected {err=}, {type(err)=}')
        print('Network exception occurred')
        return None


def analyze_review_sentiments(text: str) -> Optional[Dict[str, Any]]:
    """Make a GET request to the sentiment analyzer"""
    request_url = f'{sentiment_analyzer_url}analyze/{text}'
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f'Unexpected {err=}, {type(err)=}')
        print('Network exception occurred')
        return None


def post_review(data_dict: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Make a POST request to the backend"""
    request_url = f'{backend_url}insert_review'
    try:
        response = requests.post(request_url, json=data_dict)
        response.raise_for_status()
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f'Unexpected {err=}, {type(err)=}')
        print('Network exception occurred')
        return None

