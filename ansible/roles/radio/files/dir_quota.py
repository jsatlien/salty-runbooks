#!/usr/bin/python

## TODO
# Write docstrings.
# Use getopt for arg handling.

import getopt, sys
import os
import subprocess

MAX_CACHE_SIZE = 18432
TARGET_CACHE_SIZE = 15360

def directory_size_in_mb(path):
    try:
        command = ['du', '-s', path]
        result = subprocess.check_output(command)
        kilobytes = int(result.split()[0])
    except OSError as e:
        print "Couldn't run command: {0}.\n\tError: {1}".format(command, e.strerror)
    except ValueError, IndexError:
        print "Didn't get a valid size from {0}".format(command)
    else:
        return kilobytes / 1024

def files_by_atime(path):
    files = [os.path.join(dir, file)
             for dir, dirs, files in os.walk(path)
             for file in files]
    return sorted(files, key=lambda x: os.stat(x).st_atime, reverse=True)

def delete_file(filename):
    size_in_mb = os.stat(filename).st_size / 1048756
    os.remove(filename)
    return size_in_mb

def remove_oldest_files(directory, space_to_free):
    lru_files = files_by_atime(directory)
    freed_space = 0
    while freed_space < space_to_free:
        freed_space += delete_file(lru_files.pop())

if __name__ == '__main__':
    cache_path = sys.argv[1]
    assert os.path.isdir(cache_path), "Invalid cache path supplied."
    cache_size = directory_size_in_mb(cache_path)
    if cache_size >= MAX_CACHE_SIZE:
        remove_oldest_files(cache_path, cache_size - TARGET_CACHE_SIZE)
