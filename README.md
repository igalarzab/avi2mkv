# avi2mkv [![Project Status](http://stillmaintained.com/igalarzab/avi2mkv.png)](http://stillmaintained.com/igalarzab/avi2mkv)

## What it does.

Simple (stupid) script to transform an AVI video to matroska MKV.

It's simple because you don't need to provide any arguments to work.

It's powerful because this script will do these things for you:

* Convert all the video and audio tracks of the AVI.
* Look for all the SRT subtitles and append it to the MKV file.
* Generate a MKV file with the same name than the AVI (and in the same place).
* If you provide a directory, ``avi2mkv`` will convert all the AVI videos of the dir.


## What I need.

To use ``avi2mkv``, you need at least:

* Python (>=2.6)
* mkvtools


## How to install it.

First, install the required dependences.

Use your favourite package manager to accomplish this task.

* MacOS (with [HomeBrew](http://mxcl.github.com/homebrew/))

```sh
$ brew install mkvtoolnix
```

* Linux (with apt-get)::

```sh
$ sudo apt-get install mkvtoolnix
```

Then, you can install the last version of ``avi2mkv`` in two ways.

* You can use ``easy_install``::

```sh
$ sudo easy_install avi2mkv
```

* Or, if it's installed in your system, you can use ``pip``::

```sh
$ sudo pip install avi2mkv
```


## How to use

To run, you only need to execute the installed command::

```sh
$ avi2mkv --help
```

To convert a video (or a list of videos) you only need to provide the filename.

The output video will be placed in the same directory of the original one, and
with the same name (ended with .mkv)::

```sh
$ avi2mkv My_Video.avi My_Video2.avi
```

If you provide a directory, ``avi2mkv`` will transform all the .avi videos that are
in the directory::

```sh
$ avi2mkv My_Videos/
```


Finally, ``avi2mkv`` will take all the SRT subtitles of the video. To do this, the
script will search all the files with the **same prefix** that the .avi video
(without the extension) that ends with a .srt extension.

To take the language of the subtitles, ``avi2mkv`` will take the part that differs of
the filename of both files (the avi and the srt), stripped.

For example, in the following scenario::

```sh
$ ls
  "My_Video1.avi" "My_Video1    Spanish.srt" "My_Video1 Englishhh.srt"
$ avi2mkv My_Video1.avi
```

``avi2mkv`` will take the two subtitles files, and the name of the languages will be *Spanish*
and *Englishhh*.

## Author

* [Jose Ignacio Galarza (igalarzab)](http://github.com/igalarzab)
