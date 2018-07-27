# -*- coding: utf-8 -*-
import json
import pytest

from marshmallow import ValidationError

from lib.config import get_config

from api.github import GithubApi
from schemas.message import UnauthorizedSchema

class TestUnauthorizedUser(object):

    def setup(self):
        self.config = get_config()
        base_url = "{}://{}".format(
            self.config['enviroment']['prod']['protocol'],
            self.config['enviroment']['prod']['base_url'],
        )
        api = GithubApi(base_url)
        self.response = r = api.get_user()

    def test_status_code_401(self):
        assert self.response.status_code == 401

    def test_received_validate_schema(self):
        errors = UnauthorizedSchema().validate(self.response.json())
        assert {} == errors

    def test_validate_requires_authentication_message(self):
        message = self.response.json().get('message', None)
        assert message == 'Requires authentication'
