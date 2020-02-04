import socket
import fred
import logging

class New():
    def __init__(self):
        return
    def mymethod(self):
        """
        mymethod strings!!!
        """
        print('inside mymethod')

def moo():
    """
    docstrings for moo!!
    """
    print('hi world \n')
    c = New()
    c.mymethod()
    with open('fred.py') as fd:
        data = fd.read()
    print(data)
    print(c.mymethod())
    l = logging.Logger(__name__)
    l.log(1, data)
    l.


if __name__ == '__main__':
    moo()
