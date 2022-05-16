import app
import sys

def check_if_show_gui():
    args = sys.argv

    for arg in args:
        if arg == "-g":
            return True

    return False


def main():
    app.run(check_if_show_gui())


if __name__ == "__main__":
    main()