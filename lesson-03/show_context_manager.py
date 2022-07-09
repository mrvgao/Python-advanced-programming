"""
Context Manager
E.g :
    open  a file
    connect a dataset
    process images or some big files

    => Manage the resource
"""

"""
file = open('show_context_manager.py', 'a')
# or we connect the dataset

try:
    file.write('\n#newline')
finally:
    file.close()
"""

from contextlib import contextmanager


@contextmanager
def connect_database(url):
    obj = open(url, 'r')
    try:
        print('enter the obj')
        yield obj
    finally:
        print('exit the obj')
        obj.close()


class Processer:
    def __init__(self, filename):
        self.file = filename

    def __enter__(self):
        try:
            print(f'initialize {self.file}')
            self.fileobj = open(self.file)
            return self.file
        except FileNotFoundError as e:
            self.fileobj = None
            print('file not exists')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.fileobj:
            self.file.close()


with Processer('show_context_manager.pyui') as file:
    pass

# with open('show_context_manager.py') as file:
#     file.write('\n#newline')


with connect_database('show_context_manager.py') as c:
    print(c.read())