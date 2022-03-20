import os, sys
from argparse import ArgumentParser

from core.walk import Walk

class Cli(ArgumentParser):
    def __init__(self):
        super(Cli, self).__init__()
        self._build_args()
        self.args = self.parse_args()

    def _build_args(self):
        self.add_argument("-t", "--test", dest="test", action="store_true")

    def test(self):
        if self.args.test:
            w = Walk("~/flabba")

            del w
