#!/usr/bin/env python
#
# Copyright 2015 BMC Software, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from unittest import TestCase
import sys
from boundary.metric_list import MetricList
from io import TextIOWrapper, BytesIO
import json
import StringIO
from cli_test import CLITest
from cli_runner import CLIRunner


class MetricListTest(TestCase):

    def setUp(self):
        self.cli = MetricList()
        self.text = '''
        {
        "result": [ { "name": "BOUNDARY_MOCK_METRIC",
                     "defaultAggregate": "AVG",
                     "defaultResolutionMS": 1000,
                     "description": "BOUNDARY_MOCK_METRIC",
                     "displayName": "BOUNDARY_MOCK_METRIC",
                     "displayNameShort": "BOUNDARY_MOCK_METRIC",
                     "unit": "number",
                     "isDisabled": false,
                     "isBuiltin": false
                    }
                  ]
        }
        '''

        self.out = None
        self.json1 = None
        self.json2 = None
        # setup the environment
        self.old_stdout = sys.stdout
        sys.stdout = TextIOWrapper(BytesIO(), 'utf-8')
        sys.stdout = StringIO.StringIO()

    def tearDown(self):
        # restore stdout
        sys.stdout.close()
        sys.stdout = self.old_stdout
#        print("self.out: " + str(self.out))
#        print("self.json1: " + str(self.json1))
#        print("self.text: " + str(self.text))
#        print("self.json2: " + str(self.json2))

    def test_cli_description(self):
        CLITest.check_description(self, self.cli)

    def test_cli_help(self):
        CLITest.check_cli_help(self, self.cli)

    def test_create_curl(self):
        runner = CLIRunner(self.cli)

        enabled = True
        custom = True

        curl = runner.get_output(['-b', str(enabled).lower(),
                                  '-c', str(custom).lower(),
                                  '-z'])
        CLITest.check_curl(self, self.cli, curl)

    def test_list_metric(self):
        found = False
        runner_create = CLIRunner(MetricList())

        get = runner_create.get_output([])
        result_get = json.loads(get)
        metric_get = result_get['result']

        for metric in metric_get:
            if metric['name'] == 'CPU':
                found = True
                self.assertEqual('CPU Utilization', metric['displayName'])
                self.assertEqual('CPU', metric['displayNameShort'])
                self.assertTrue(metric['isBuiltin'])
                self.assertFalse(metric['isDisabled'])
                self.assertEqual('percent', metric['unit'])
                self.assertEqual('avg', metric['defaultAggregate'])
                self.assertEqual(1000, metric['defaultResolutionMS'])
                self.assertEqual('Overall CPU utilization', metric['description'])

        self.assertTrue(found)
