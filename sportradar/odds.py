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
import requests
from pprint import pprint
from api import Api

class Odds(Api):
    """A python interface into the SportRadar Odds API"""

    def __init__(self, odds_format='eu', *args, **kwargs):
        """Instantiate a new sportradar.Odds object

        package: Defines the package you are accessing as US (us) or Rest of World (row)
        access_level: Defines the access level of your API key as Production (x) or Trial (xt)
        version: Version number of the API you are accessing (Current Version: 3)
        language_code: Supported Locales (en, de, fr, ru etc.) See https://developer.sportradar.com/files/locales.pdf
        format: xml or json
        api_key: Your API key
        odds_format: Odds type in 2 letter format: American (us), Fractional (uk), or Decimal (eu)."""

        self.odds_format  = odds_format
        super().__init__(self, access_level = 't', version = '1', feed_package='odds', *args, **kwargs)

    def sports(self):
        """This endpoint retrieves the list of Sports."""
        url = f'{self.base_url}/oddscomparison-{self.package}{self.access_level}{self.version}/{self.language_code}/{self.odds_format}/sports.{self.data_format}'
        print(url)
        pass
        payload = {'api_key': self.api_key}
        r = requests.get(url, params=payload)
        print(r.url)
        pprint(r.json())

    def books(self):
        """This endpoint retrieves the list of Bookmakers."""
        url = f'{self.base_url}/oddscomparison-{self.package}{self.access_level}{self.version}/{self.language_code}/{self.odds_format}/books.{self.data_format}'
        payload = {'api_key': self.api_key}
        r = requests.get(url, params=payload)
        print(r.url)
        pprint(r.json())

    def daily_sport_schedule(self):
        """This endpoint retrieves the Daily Sport Schedule."""
        url = f'{self.base_url}/oddscomparison-{self.package}{self.access_level}{self.version}/{self.language_code}/{self.odds_format}/sports/sr:sport:1/2018-10-10/schedule.{self.data_format}'
        payload = {'api_key': self.api_key}
        r = requests.get(url, params=payload)
        print(r.url)
        pprint(r.json())



