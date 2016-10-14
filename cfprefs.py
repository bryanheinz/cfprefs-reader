#!/usr/bin/python

import CoreFoundation

domain = 'com.apple.appstore'
key = 'restrict-store-require-admin-to-install'

key_value = CoreFoundation.CFPreferencesCopyAppValue(key, domain)
print 'Key Value = ', key_value

key_forced = CoreFoundation.CFPreferencesAppValueIsForced(key, domain) 
print 'Key Forced = ', key_forced
