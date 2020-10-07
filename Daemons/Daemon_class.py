from daemon import runner
from time import ctime, sleep


class Daemon:
    def __init__(self):
        pass


def do_something():
    with open("/tmp/some_file.txt", "w") as f:
        f.write("The time is now" + ctime())


def run():
    while True:
        sleep(300)
        do_something()


if __name__ == '__main__':
    run()
