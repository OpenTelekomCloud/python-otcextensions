#!/usr/bin/env python3
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
"""
Find CCE Node Pool by name or ID
"""
import openstack

openstack.enable_logging(True)
conn = openstack.connect(cloud='otc')


cluster = 'name_or_id'
node_pool = 'name_or_id'
cluster = conn.cce.find_cluster(cluster)
pool = conn.cce.find_node_pool(cluster=cluster, node_pool=node_pool)
print(pool)
