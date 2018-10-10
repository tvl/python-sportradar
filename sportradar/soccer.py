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

class Soccer(Api):
    """A python interface into the SportRadar Soccer API"""

    def __init__(self, league_group='eu', *args, **kwargs):
        """Instantiate a new sportradar.Soccer object

        access_level: Defines the access level of your API key as Production (x) or Trial (xt)
        version: Version number of the API you are accessing (Current Version: 3)
        league_group: League group in one of the following formats: Top Europe (eu),
            Top Americas (am), Top Asia (as), Top International (intl), Other (other), or Global (global)

        format: xml or json
        api_key: Your API key."""

        self.league_group = league_group
        super().__init__(self, access_level = 'xt', version = '3', feed_package='soccer', *args, **kwargs)

    def daily_schedule(self):
        """This endpoint retrieves the Daily Schedule"""
        url = f'{self.base_url}/soccer-{self.access_level}{self.version}/{self.league_group}/{self.language_code}/schedules/2018-10-11/schedule.{self.data_format}'
        payload = {'api_key': self.api_key}
        r = requests.get(url, params=payload)
        print(r.url)
        pprint(r.json())



