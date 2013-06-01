#!/usr/bin/env python
#
#    Copyright 2012, Jose Ignacio Galarza <igalarzab@gmail.com>.
#
#    This file is part of avi2mkv.
#
#    avi2mkv is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    avi2mkv is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with avi2mkv.  If not, see <http://www.gnu.org/licenses/>.
#

import glob
import logging
import os
import subprocess
import sys
from optparse import OptionParser


# Global information
__uname__ = 'avi2mkv'
__long_name__ = 'Simple AVI/MP4 to MKV converter'
__version__ = '1.0'
__author__ = 'Jose Ignacio Galarza'
__email__ = 'igalarzab@gmail.com'
__url__ = 'http://github.com/igalarzab/avi2mkv'
__license__ = 'MIT'

# Colors (ANSI)
RED = '31'
GREEN = '32'


def show_authors(*args, **kwargs):
    'Show authors'
    print('%s v%s, %s' % (__uname__, __version__, __long_name__))
    print('%s <%s>' % (__author__, __email__))
    print(__license__)
    sys.exit(0)


def write_text(text, desc=sys.stdout, color=None):
    'Write the text with color, if tty'
    if color is not None and desc.isatty():
        desc.write('\x1b[%sm%s\x1b[0m' % (color, text))
    else:
        desc.write(text)

    desc.flush()


def shell_arguments():
    'Parse the arguments'
    usage = "usage: %prog [options] file1 file2 ..."
    parser = OptionParser(usage=usage, version="%prog " + __version__)

    # Print information
    parser.add_option('-d', '--debug',
                      action='store_true',
                      dest='debug',
                      help='be extra verbose',
                      default=False)

    parser.add_option('-a', '--authors',
                      action='callback',
                      callback=show_authors,
                      help='show authors')

    return parser


def check_mkvmerge():
    'Check if mkvmerge is installed'
    try:
        subprocess.check_call(['mkvmerge', '-V'], stdout=subprocess.PIPE)
    except OSError:
        return False

    return True


def analyze_path(obj):
    'Get all the videos of the obj (path or file)'
    ab_path = os.path.abspath(obj)

    # Check if the path exists
    if not os.path.exists(ab_path):
        write_text('[E]', color=RED)
        write_text(' The file "%s" doesn\'t exists\n' % obj)
        return False

    # If it's a file, convert it directly; otherwise, transverse the dir
    if os.path.isfile(ab_path):
        convert_video(ab_path)
    elif os.path.isdir(ab_path):
        for f in glob.glob(ab_path + r'/*.avi'):
            abs_f = os.path.join(ab_path, f)
            if os.path.isfile(abs_f):
                convert_video(abs_f)
        for f in glob.glob(ab_path + r'/*.mp4'):
            abs_f = os.path.join(ab_path, f)
            if os.path.isfile(abs_f):
                convert_video(abs_f)

    return True


def language_code(lang):
    'Get the language code'
    values = {
        'spanish': 'es',
        'english': 'en',
        'french': 'fr',
        'german': 'de',
    }

    return values.get(lang.lower(), None)


def find_subtitles(finput):
    'Find all the subtitles of the video'
    files = glob.glob(finput + '*.srt')
    languages = []

    for f in files:
        language = f[len(finput):-4].strip().strip('.')

        if language:
            languages.append([language_code(language), language, f])
            logging.info('Found a subtitle with the name "%s"', language)

    return languages


def create_command(iname, oname, subtitles):
    'Creathe the mkvmerge command'
    command = ['mkvmerge']

    # Append the output file
    command.append('-o')
    command.append(oname)

    # Append the input file
    command.append(iname)

    # Create the subtitles
    for subtitle in subtitles:
        if subtitle[0]:
            command.append('--language')
            command.append('0:%s' % subtitle[0])
        command.append('--track-name')
        command.append('0:%s' % subtitle[1])
        command.append(subtitle[2])

    logging.info(command)
    return command


def convert_video(finput):
    'Convert the found videos to matroska'
    logging.info('Trying to convert %s', finput)

    finput_without_ext = os.path.splitext(finput)[0]
    foutput = finput_without_ext + '.mkv'

    if os.path.exists(foutput):
        write_text('[E]', color=RED)
        write_text(' The destine "%s" already exists\n' % foutput)
        return False

    subs = find_subtitles(finput_without_ext)

    command = create_command(finput, foutput, subs)

    write_text('[ ] Converting %s' % finput)
    c = subprocess.call(command, stdout=subprocess.PIPE)

    if c == 0:
        write_text('\r[X]\n', sys.stdout, GREEN)
    else:
        write_text('\r[E]\n', sys.stdout, RED)

    return c == 0


def main():
    'Entry point'
    arg_parser = shell_arguments()
    (options, paths) = arg_parser.parse_args()

    if not paths:
        print('Try with -h to see the help')
        sys.exit(0)

    # Configure the logging module
    if options.debug:
        level = logging.INFO
    else:
        level = logging.WARNING

    logging.basicConfig(level=level,
                        format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    if not check_mkvmerge():
        print('mkvtoolnix is not installed in your system')
        print('You need the mkvmerge command to run this script')
        sys.exit(-1)

    for path in paths:
        logging.info('Looking for all the avi/mp4 files in %s', path)
        analyze_path(path)


if __name__ == '__main__':
    main()

# vim: ai ts=4 sts=4 et sw=4
