# Copyright 2020 JD.com, Inc. Galileo Authors. All Rights Reserved.
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
# ==============================================================================

from galileo.platform.export import export
from galileo.platform.default_values import DefaultValues


@export()
def create_client(zk_server=DefaultValues.ZK_SERVER,
                  zk_path=DefaultValues.ZK_PATH):
    from galileo.framework.pywrap import py_client as client
    conf = client.DGraphConfig()
    conf.zk_addr = zk_server
    conf.zk_path = zk_path
    if not client.CreateDGraph(conf):
        raise RuntimeError("Failed to create graph client")