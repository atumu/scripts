#! /bin/env python

import re
import subprocess
import sys
import os
import uuid

# Convert m4a to mp3.

# Annoying tmpnam warnings, this is a song converter.
def make_tempname():
    u = uuid.uuid4()
    return "/tmp/music-%s.wav" % u

# Make a directory if it doesn't exist (doesn't quite do the right
# thing with symlinks.
def safe_mkdir(name):
    if not os.path.isdir(name):
        os.mkdir(name)

class Convert():

    kw_re = re.compile(r'^([a-z]+): (.*)')
    decoding_re = re.compile(r'.*[Dd]ecoding.*')
    known_kw = frozenset(['title', 'artist', 'album', 'genre',
        'track', 'totaltracks', 'date'])

    def __init__(self, mp4):
        self._mp4 = mp4
        self._wave = make_tempname()
        print self._wave

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        try:
            os.unlink(self._wave)
        except OSError:
            pass

    def decode(self):
        devnull = open('/dev/null', 'r')
        self._fields = {}
        p = subprocess.Popen(['faad', '-o', self._wave, self._mp4],
                stderr=subprocess.PIPE, stdin=devnull)
        devnull.close()
        for line in p.stderr:
            line = line.rstrip('\n')
            m = Convert.kw_re.match(line)
            if m:
                key = m.group(1)
                value = m.group(2)
                if key in Convert.known_kw:
                    self._fields[key] = value
                    print "%s=%s" % (m.group(1), m.group(2))
            elif Convert.decoding_re.match(line):
                # Note that faad doesn't print the immediate status
                # unless it thinks it is talking to a terminal.
                print line
                sys.stdout.flush()
        result = p.wait()
        if result != 0:
            raise Exception("Failed to convert")

    def encode(self):
        artist = self._fields.get('artist', 'Unknown')
        album = self._fields.get('album', 'Unknown')
        title = self._fields.get('title', 'Unknown')
        track = int(self._fields.get('track', '0'))
        totaltracks = int(self._fields.get('track', '0'))
        safe_mkdir(artist)
        safe_mkdir(artist + '/' + album)
        self._mp3 = '%s/%s/%02d-%s.mp3' % (artist, album, track, title)
        subprocess.check_call(['lame', '--preset', '192', self._wave,
            self._mp3,
            '--tt', title,
            '--ta', artist,
            '--tl', album,
            '--ty', self._fields.get('date', '1900')[0:4],
            '--tg', self._fields.get('genre', 'Unknown'),
            '--tn', "%s/%s" % (track, totaltracks)])

def main(songs):
    for song in songs:
        with Convert(song) as conv:
            conv.decode()
            conv.encode()

if __name__ == '__main__':
    main(sys.argv[1:])