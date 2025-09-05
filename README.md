# Wordle

This is a Wordle game written in Python with a simple command-line interface.  It is meant to emulate the 
New York Times version of the game, except for the [dictionary](#dictionary).

## Installation

There are Windows and Linux 64 bit zip files that contain the Wordle
executable and the words dictionary (`words.txt`).  Unzip into any
folder your wish and run the executable (`wordle.exe` for Windows and 
`wordle` for Linux).  Windows users can double-click in the Files app.
There is no macOS version because I don't have access to a Mac, but
try the Execution instructions below.  If the installation files don't work for you,
you can try the instructions below too.

## Execution with Python

You will need to download and install [Python](https://www.python.org/downloads/) to your system.  Also download the source files by clicking the green Code button and selection Download ZIP.  Or you can clone the repository with `git`.

This project uses [termcolor](https://pypi.org/project/termcolor/) to do the coloring of the display letters.  You
will need to install this package once to run Wordle program.  The easiest way to do that is to type the following at the
command line:

    pip install termcolor

After that, type this to run the program in the directory you downloaded to:

    python wordle.py

## Colors

Being red/green colorblind, I am sensitive to the choice of colors.  The NYTimes version of Wordle uses orange and
green, which are very hard for me to tell apart.  So I made the letters that are in the right place white, but on a green background.  This makes it easy for me to distinguish the two, but is still the color scheme that most people are used to.
Letters in the wrong place but in the word are light red because orange is not available.

## Dictionary

The dictionary is just a text file called `words.txt` with one word per line.
You can build your own dictionary if you wish.  If your system has a text dictionary with one word per line, like
`/usr/share/dict/words`, there is a program called `build_words.py` that will create the
file from scratch.

One thing that is not easy to do is filter out plurals, so they are left in.  They are not legal in the NYTimes
version of Wordle, so be aware of that.

The word list is somewhat curated.  It contains no offensive words or racial slurs that I can think of, but some may
have gotten past me.

## Related Projects

* <https://github.com/ksnortum/find-words-web>
* <https://github.com/ksnortum/find-words-java>
* <https://github.com/ksnortum/find-words-python>
* <https://github.com/ksnortum/wordle-kotlin>
* <https://github.com/ksnortum/wordle-python> (this site)
