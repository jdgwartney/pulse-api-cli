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

import json
from unittest import TestCase

from boundary import ActionInstalled
from cli_runner import CLIRunner
from cli_test import CLITest


class ActionInstalledTest(TestCase):

    def setUp(self):
        self.cli = ActionInstalled()

    def test_cli_description(self):
        CLITest.check_description(self, self.cli)

    def test_cli_curl(self):
        runner = CLIRunner(self.cli)
        curl = runner.get_output(['-z'])
        CLITest.check_curl(self, self.cli, curl)

    def test_cli_help(self):
        CLITest.check_cli_help(self, self.cli)

    def test_get_actions_installed(self):
        runner = CLIRunner(ActionInstalled())

        result = runner.get_output([])
        actions_result = json.loads(result)
        actions = actions_result['result']

        self.assertGreaterEqual(len(actions), 1)

