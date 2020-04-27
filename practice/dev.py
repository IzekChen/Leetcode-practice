#/bin/python

language = 'Python'
framework = 'Django'


def hello_world():
    print('Hey !!! welcome back')

class ModuleTest:
    def get_language(self):
        print('My favorite language is - {}'.format(language))

d = ModuleTest().get_language()
