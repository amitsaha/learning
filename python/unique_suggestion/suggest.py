# Suggest unique names given a starting name which is already
# present in the repository.

from __future__ import unicode_literals
import random
import re

disk_hits = 0
max_unique = 3
max_disk_hit = 10

def is_unique(repository, name):
    if name not in repository:
        return True
    else:
        return False

def suggest(repository, name, max_length=25):
    # Empty string (one or more spaces)
    if not name or not name.strip():
        return []
    # Starting with a digit
    pat = re.compile('^\d+')
    if pat.match(name):
        return []
    # No non-alphanumeric character anywyere
    pat = re.compile('\w*\W+\w*')
    if pat.match(name):
        return []
    global disk_hits
    unique_suggestions = []
    while len(unique_suggestions) < max_unique and disk_hits < max_disk_hit:
        basename = name
        # Add a space, followed by a random number in the range 0-999
        # Ex. for 'Title' a suggestion would be 'Title - 123'
        # For Title and a maximum length of 5, valid suggestions would
        # be T - 1, T - 5, etc.
        unique_id = ' - %s' % random.randint(0, 999)
        while True:
            suggestion = basename + unique_id
            if len(suggestion) > max_length:
                basename = basename[:-1]
                num_digits = len(unique_id[unique_id.find('-') + 2:])
                # We want at least one digit, so if there
                # is only one we do not truncate it further
                # but truncate the basename
                if num_digits > 1:
                    unique_id = unique_id[:-1]
                else:
                    if len(basename) > 1:
                        basename = basename[:-1]
            else:
                break
        # Did we truncate the entire basename, hope not?
        assert len(basename) >= 1
        # Defensive
        assert len(suggestion) <= max_length
        # increment disk hit
        disk_hits += 1
        if is_unique(repository, suggestion):
            unique_suggestions.append(suggestion)
    return unique_suggestions
