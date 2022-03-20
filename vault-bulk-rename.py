import os, sys, argparse

from core.cli import Cli

def usage():
    print("vault-bulk-rename - A powerful bulk renaming utility for media files")
    print("")
    print("Basic Operations")
    print("     -h --help : Print this page")
    print("     -i, --input : Input path")
    print("     -I, --info [path] : Get info on a directory or file")
    print("     -c, --check [path] : Check to see if a media file and/or directory is on VAULT")
    print("     -v, --verbose : Enable verbosity")
    print("Renaming: ")
    print("     -r, --rename : Rename a media file or directory")
    print("         --preset [preset_name] : Search for a preset to rename against")
    print("Auto Renaming: ")
    print("     -ar, --auto-rename [agent] : Auto Rename a media file or directory and match it to a Database")
    print("         --aired-order : Rename against aired order")
    print("         --dvd-order : Rename against DVD order")
    print("         --absolute-order : Rename against absolute order")
    print(" Walk Options: ")
    print("         --recursive : Walk files recursivly")
    print("         --top-down : Walk the directory top down")
    print("         --dry-run : Do everything except rename the file")
    print("         --extensions [ext] : Only rename files with certain extensions")
    print("         --folder-regex : Match folders against regex")
    print("         --file-regex : Match files against regex")
    print("         --folder-output : Folder renaming pattern")
    print("         --file-output : File renaming pattern")
    print("         --use-parsed : Use whatever is matched in file_regex to rename the file")
    print("         --embed-subtitles [.srt] : Embed a subtitles file into a media file (mp4, mkv)")
    print("         --find-subtitles : Find subtitles for the piece of media and embed them")
    print("         --reorder-audio-tracks : Reorder audio tracks to set english ones first")

def main():
    c = Cli()
    c.test()

if __name__ == '__main__':
    main()
