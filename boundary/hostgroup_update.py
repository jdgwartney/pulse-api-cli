#
# Copyright 2015 BMC Software, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from boundary import HostgroupModify


class HostgroupUpdate(HostgroupModify):
    def __init__(self):
        HostgroupModify.__init__(self, True)
        self.method = "PUT"
        self.hostGroupId = ""

    def add_arguments(self):
        HostgroupModify.add_arguments(self)
        self.parser.add_argument('-i', '--host-group-id', dest='hostGroupId', action='store',
                                 required=True, metavar='host_group_id', help='Host group id to update')

    def get_arguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        HostGroupModify.get_arguments(self)

        if self.args.hostGroupId is not None:
            self.hostGroupId = self.args.hostGroupId

        self.path = "v1/hostgroup/" + str(self.hostGroupId)

    def get_description(self):
        return 'Updates host group definition in a {0} account'.format(self.product_name)