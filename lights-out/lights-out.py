#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Copyright 2008 Juha Autero
#
# Copyright 2008 Juha Autero <jautero@gmail.com>
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

project="Lights Out"
version="1.0"
author="Juha Autero <jautero@gmail.com>"
copyright="Copyright 2008 Juha Autero <jautero@gmail.com>"
application="lights-out"
import wsgiref.handlers
import os

from google.appengine.ext.webapp import template
from google.appengine.ext import webapp

class LightsOut(webapp.RequestHandler):

  def get(self):
    template_values=globals()
    path = os.path.join(os.path.dirname(__file__), 'index.html')
    self.response.out.write(template.render(path, template_values))

def main():
  application = webapp.WSGIApplication([('/', LightsOut)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
