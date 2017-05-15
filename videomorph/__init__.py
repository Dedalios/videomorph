#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File name: __init__.py
#
#   VideoMorph - A PyQt5 frontend to ffmpeg and avconv.
#   Copyright 2015-2016 VideoMorph Development Team

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at

#       http://www.apache.org/licenses/LICENSE-2.0

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""This module defines the videomorph package and the needed constants."""


from collections import namedtuple
from os import cpu_count

APPNAME = 'VideoMorph'
VERSION = '1.0'
CODENAME = 'traveler'
PACKAGE_NAME = APPNAME.lower()
MAINTAINER = APPNAME + ' ' + 'Development Team'

ConversionLib = namedtuple('ConversionLib', 'ffmpeg avconv')
CONV_LIB = ConversionLib('ffmpeg', 'avconv')

Prober = namedtuple('Prober', 'ffprobe avprobe')
PROBER = Prober('ffprobe', 'avprobe')

MediaFileStatus = namedtuple('MediaFileStatus', 'todo done stopped')
STATUS = MediaFileStatus('To convert', 'Done!', 'Stopped!')


CPU_CORES = (cpu_count() - 1 if
             cpu_count() is not None
             else 0)

LINUX_PATHS = {'apps': '/usr/share/applications',
               'icons': '/usr/share/icons',
               'i18n': '/usr/share/videomorph/translations',
               'profiles': '/usr/share/videomorph/stdprofiles',
               'doc': '/usr/share/doc/videomorph'}

VM_PATHS = {'apps': 'share/applications',
            'icons': 'share/icons',
            'i18n': 'share/videomorph/translations',
            'profiles': 'share/videomorph/stdprofiles',
            'doc': 'share/doc/videomorph',
            'bin': 'bin'}
