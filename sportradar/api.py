#!/usr/bin/env python
#
# Copyright 2018-2018, 2018 The Python-SportRadar Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A library that provides a Python interface to the SportRadar API"""

import json
import logging
import requests
import os

logger = logging.getLogger(__name__)

class Api(object):
    """A python interface into the SportRadar API"""

    def __init__(self,
        test_1=None,
        package='row',
        feed_package=None,
        access_level='xt',
        version='3',
        language_code='en',
        data_format='json',
        api_key=None):
        """Instantiate a new sportradar.Api object

        package: Defines the package you are accessing as US (us) or Rest of World (row)
        access_level: Defines the access level of your API key as Production (x) or Trial (xt)
        version: Version number of the API you are accessing (Current Version: 3)
        language_code: Supported Locales (en, de, fr, ru etc.) See https://developer.sportradar.com/files/locales.pdf
        format: xml or json
        api_key: Your API key."""

        self.base_url = 'https://api.sportradar.com'
        self.package = package
        self.access_level = access_level
        self.version = version
        self.language_code=language_code
        self.data_format = data_format

        if api_key is None:
            api_file_name = f'{feed_package}_api_key'
            with open(api_file_name) as f:
                print(api_file_name)
                self.api_key = f.readline().replace('\n', '')
                print(self.api_key)
