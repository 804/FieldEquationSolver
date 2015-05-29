__author__ = '804'

from Application import App
import sys

if __name__ == "__main__":
    app = App(sys.argv)
    sys.exit(app.exec_())
