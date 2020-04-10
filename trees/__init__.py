#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Copyright 2020 Abdelkrime Aries <kariminfo0@gmail.com>
#
#  ---- AUTHORS ----
# 2020	Abdelkrime Aries <kariminfo0@gmail.com>
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
#

from collections import OrderedDict

version = "0.1"
release = "0.1.0"

class NodeProcessor(object):

    def root_init(self):
        pass

    def root_final(self):
        pass

    def child_pre_process(self, node, child_key):
        print("pre_processing " + str(node.children[child_key].label))
        return False

    def child_post_process(self, node, child_key):
        print("post_processing " + str(node.children[child_key].label))
        return False

    def pre_process(self, node):
        print("begin processing " + str(node.label))
        return node.children.keys()

    def post_process(self, node):
        print("end processing " + str(node.label))

    def result(self):
        pass

    def process(self, node):
        children_keys = self.pre_process(node)
        for child_key in children_keys:
            if self.child_pre_process(node, child_key):
                break
            if self.process(node.children[child_key]):
                break
            if self.child_post_process(node, child_key):
                break
        self.post_process(node)

def_processor = NodeProcessor()

class Node(object):
    def __init__(self, value=0, label=""):
        self.label = label
        self.value = value
        self.children = OrderedDict()

    def append_child(self, label, node):
        self.children[label] = node
        return self


class Tree(object):

    def __init__(self, value=0, label=""):
        self.root = Node(value, label)

    def get_root(self):
        return self.root

    def process(self, processor=def_processor):
        processor.root_init()
        processor.process(self.root)
        processor.root_final()
        return processor.result()
