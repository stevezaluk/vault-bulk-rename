import os, sys

def usage():
    print("vault-bulk-rename - A powerful bulk renaming utility for media files")
    print("")
    print("Basic Operations")
    print("     -h --help : Print this page")
    print("     -i, --info [path] : Get info on a directory or file")
    print("     -c, --check [path] : Check to see if a media file and/or directory is on VAULT")
    print("Renaming: ")
    print("     -r, --rename : Rename a media file or directory")
    print("         --extensions [ext] : Only rename certain extensions")
    print("         --preset [preset_name] : Search for a preset to rename against")
    print("         --folder-regex : Match folders against regex")
    print("         --file-regex : Match files against regex")
    print("         --recursive : Walk files recursivly")
    print("         --encoder [encoder] : Only rename files with this encoder")
    print("         --dry-run : Do everything except rename the file")
    print("Auto Renaming: ")
    print("     -ar, --auto-rename : Auto Rename a media file or directory and match it to a Database")
    print("         --tv-db : Default. Match against shows and movies on TVdB")
    print("         --imdb : Match against shows and movies on IMDB")
    print("         --youtube : Match against videos on youtube")

def main():
    usage()

if __name__ == '__main__':
    main()
