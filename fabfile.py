from fabric.api import local


def test():
    local('flake8 *.py')
    local('python test_tictactoe.py')
