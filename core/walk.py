import os, sys, regex

from utils.colors import print_fatal

from core.path import Path

class Walk(object):
    def __init__(self, path:str):
        self.path = Path(path)

        self.preset = None

        self.dry_run = False
        self.recursive = False

        self.folder_regex = None
        self.file_regex = None

        self.discrimnate_extensions = []

        self.directory_count = 0
        self.file_count = 0

    def _match_regex(self, name:str, regex:str, full_match=False):
        if isinstance(regex, str):
            rgx = re.compile(regex)
            if full_match:
                match = rgx.match(name)
            else:
                match = rgx.search(name)

            if match:
                return True
            else:
                return False

    def _determine_extension(self, name:str):
        for e in self.discrimnate_extensions:
            if name.endswith(e):
                return True

        return False

    def scan_dirs(self):
        ret = []
        for root, directories, files in os.walk(self.path.get_path(), topdown=True):
            for name in directories:
                full_path = os.path.join(root, name)

                if self.folder_regex:
                    if _match_regex(name, self.folder_regex, True):
                        # self.scan_files(full_path)
                        ret.append(full_path)
                else:
                    ret.append(full_path)

        return ret

    def scan_files(self, path:str):
        ret = []
        if os.path.isdir(path):
            for root, directories, files in os.walk(path):
                for name in files:
                    full_path = os.path.join(root, name)
                    if _determine_extension(name):
                        pass
                    else:
                        if self.file_regex:
                            if _match_regex(name, self.file_regex):
                                # self.format(full_path)
                                ret.append(Path(full_path))
                        else:
                            ret.append(Path(full_path))

        return ret
        
    def format(self, path:str):
        if self.dry_run:
            pass
        else:
            pass
