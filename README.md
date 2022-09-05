# Unix File Organization


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![Testing-Library](https://img.shields.io/badge/-TestingLibrary-%23E33332?style=for-the-badge&logo=testing-library&logoColor=white)
![Debian](https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white)


![Production Workflow](https://github.com/rod608/fileorg_oop_docker/actions/workflows/prod.yml/badge.svg)

## Description:
This is the base for a file organization app with the purpose of moving files within the root of a "starting" directory to a "final" directory; 
whether it be the "final" directory's root or to automatically created sub-folders within it. The two declared directories can be the same due to this.

The process starts with the program searching for potential files to move. Whether a file is considered to be "movable" depends on its format type 
(i.e audio), which is determined by its extension (i.e mp3, wav, etc.) If any movable files are found, the program creates folders on the 
"final" directory's root if they were supplied by the user. The files are then moved either into the "final" directory's root or a sub-folder 
within that directory if it is tied to the file's format type (there may be a folder specifically for audios). Once the process is complete, 
all empty folders within the "final" directory are deleted and one is left with their files successfully organized.

### Steps:
1) Search the "starting" directory for potential files to move. Stop if none are found.
2) Create folders on the "final" directory's root, if supplied.
3) Move files. Depending on their format type, they may be moved to either the "final" directory's root or a sub-folder tied to it by said format type.
4) Delete all empty folders on the "final" directory.

## existing features:
- Organize files based on user defined file types and associated file extensions.
- Files will either move directly into the target directory 
- Organize (move) files from one directory to another based on file types and their extensions.

## features to add:

## Process
### formats.py
- used to refresh myself on OOP in Python. I added methods that I believed would be useful to the class.
- getters, settings, toString, equals, compareTo, etc.