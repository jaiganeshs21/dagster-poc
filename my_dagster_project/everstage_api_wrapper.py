import os
import requests
from flask import session


class EverstageAPIWrapper:
    """
    Wrapper class for Everstage API calls
    """
    def _get_everstage_superset_api_client_secret(self):
        return "3cc937c3-6188-4800-875b-7327b0ca9bc3"

    def _get_everstage_bearer_token_for_request(self):
        return f"Bearer {self._get_everstage_superset_api_client_secret()}"

    def __init__(self):

        self.bearer_token = self._get_everstage_bearer_token_for_request()

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": self.bearer_token,
        }

        self.session = requests.Session()
        self.session.headers.update(headers)