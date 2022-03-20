import os, sys
from utils.colors import print_fatal

class Path:
    def __init__(self, path):
        self._path = path
        self._validate()

        self._stat = os.stat(self._path)

        self._tokens = self._path.split("/")

        self.name = self._tokens[-1]
        self.root = ""

        self.type = "file"

    def get_path(self):
        return self._path

    def get_stat(self):
        return self._stat

    def _validate(self):
        if "~" in self._path:
            self._path = self._path.replace("~", os.getenv("HOME"))

        if os.path.exists(self._path):
            pass
        else:
            print_fatal("Path does not exist: ", self._path)

        if os.path.isdir(self._path):
            self.type = "dir"
        elif os.path.isfile(self._path):
            pass

class LocalSeason(Path):
    def __init__(self, path):
        super(LocalSeason, self).__init__(path)

        self.show_name = ""
        self.season_number = ""

        self.episodes = []


class LocalEpisode(Path):
    def __init__(self, path):
        super(LocalEpisode, self).__init__(path)

        self.season = ""
        self.episode_name = ""
        self.episode_prefix = ""
