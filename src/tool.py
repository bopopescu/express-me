'''
Created on Sep 8, 2010

@author: Michael Liao
'''

from os import path
from Cheetah.Template import Template

def main():
    posts = [Post('New Post'), Post('How to install Python'), Post('Good day!')]
    model = {
            'title' : 'Compiled cheetah template',
            'posts' : posts
    }
    file = path.join(path.split(__file__)[0], 'view', 'main.html')
    print file
    t = Template(file=file, searchList=[model])
    print str(t)
    cc = Template.compile(source=None, file=file, returnAClass=False, moduleName='autogen.blog', className='CompiledTemplate')
    print cc
    target = path.join(path.split(__file__)[0], 'autogen', 'blog', 'main.py')
    f = open(target, 'w')
    f.write(cc)
    f.close()
    from autogen.blog.main import CompiledTemplate
    ct = CompiledTemplate(searchList=[model])
    print str(ct)

def compile(root_path):
    autogen_path = path.join(root_path, 'autogen')

def gen_init_py(package_path):
    file = open(path.join(package_path, '__init__.py'), 'w')
    file.write(r'''#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao (askxuefeng@gmail.com)'

# DO NOT modify because it was generated by 'compile_view'
''')
    file.close()

class Post(object):
    def __init__(self, title):
        self.title = title

if __name__ == '__main__':
    main()
