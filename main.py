#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
import webapp2
from caesar import encrypt
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Formation</title>
    </style>
</head>
<body>
"""
page_footer = """
</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        encryption = self.request.get("encryption")
        text_form = """
        <form method="post">
            <label for="numbers"> Enter rotation amount.</label>
            <input type="text" name="numbers" value="0">
            <br>
            <label for="text"> Enter your text.</label>
            <textarea name="text">{}</textarea>
            <input type="submit">
        </form>
        """.format(encryption)
        self.response.write(page_header+text_form+page_footer)
        #a = encryption
        #"%s" % a
    def post(self):
        numbers=self.request.get("numbers")
        text=self.request.get("text")
        encryption=encrypt(text, numbers)
        text_form = """
        <form method="get">
            <label for="numbers"> Enter rotation amount.</label>
            <input type="text" name="numbers" value="0">
            <br>
            <label for="text"> Enter your text.</label>
            <textarea name="text">{}</textarea>
            <input type="submit" name="button">
        </form>
        """.format(encryption)

        self.response.write(page_header+text_form+page_footer)
        # self.redirect('/?encryption={}'.format(encryption))
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
