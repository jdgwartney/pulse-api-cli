#!/usr/bin/env python
#
# Copyright 2014-2015 Boundary, Inc.
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
from boundary import API


class ApiTest(TestCase):

    def setUp(self):
        self.api = API()

    def test_get_metric(self):
        metric_definitions = self.api.metric_get()
        self.assertIsNotNone(metric_definitions)

    def test_metrics_count(self):
        metric_definitions = self.api.metric_get()
        self.assertGreaterEqual(1, len(metric_definitions))

    def test_metrics_iter(self):
        metric_definitions = self.api.metric_get()
        print(metric_definitions)
        for metric in metric_definitions:
            print(metric)

