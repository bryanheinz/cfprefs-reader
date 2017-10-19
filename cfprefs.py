#!/usr/bin/python

# Script forked and tweaked from https://github.com/dataJAR/jnuc2016

import CoreFoundation
from sys import argv

if '-h' in argv or len(argv) == 1:
    print("")
    print("python prefs.py <com.domain.name> <key>")
    print("")
    exit(0)

script, domain, key = argv

key_value = CoreFoundation.CFPreferencesCopyAppValue(key, domain)
print 'Key Value = ', key_value

key_forced = CoreFoundation.CFPreferencesAppValueIsForced(key, domain) 
print 'Key Forced = ', key_forced
