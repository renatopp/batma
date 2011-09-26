# -*- coding:utf-8 -*-
# Copyright (c) 2011 Renato de Pontes Pereira, renato.ppontes at gmail dot com
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.

'''
First version of robi scaffolding
'''

import sys, os

game = '''
import batma

class MyGame(batma.Game):
    def initialize(self):
        batma.add_resource_path('resources')
    
    def load_content(self):
        pass

    def update(self, tick):
        pass

    def draw(self):
        pass

game = MyGame()
batma.run()
'''

cwd = os.getcwd()

def robi():
    if len(sys.argv) > 1:
        project_name = sys.argv[1].replace(' ', '')
    else:
        project_name = raw_input('Project name: ').replace(' ', '')
    
    project_dir = os.path.join(cwd, project_name)
    resource_dir = os.path.join(project_dir, 'resources')
    game_file = os.path.join(project_dir, project_name+'.py')

    os.mkdir(project_dir)
    os.mkdir(resource_dir)
    f = open(game_file, 'w')
    f.write(game)
    f.close()
