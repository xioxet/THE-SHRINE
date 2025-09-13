# wah see i use sys.argv
# so you know it's important

import os, sys

module_names = sys.argv[1:]
cwd = os.getcwd()

make_ignore = lambda dir_name: open(os.path.join(dir_name, '.init'), 'w').close()

for module_name in module_names:
    module_dir = os.path.join(cwd, module_name)
    if not os.path.isdir(module_dir):
        os.mkdir(module_dir)
        make_ignore(module_dir)
        for s in ['_lab', '_tut', '_notes']:
            subdir = os.path.join(module_dir, module_name+s)
            os.mkdir(subdir)
            make_ignore(subdir)

