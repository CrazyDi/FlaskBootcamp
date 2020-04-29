x = 'THIS IS GLOBAL LEVEL'


def enclosing():
    x = 'Enclosing Level'

    def inside():
        x = 'local'
        print(x)

    inside()


enclosing()
