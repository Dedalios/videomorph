#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File name: test_profiles.py
#
#   VideoMorph - A PyQt5 frontend to ffmpeg.
#   Copyright 2016-2018 VideoMorph Development Team

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at

#       http://www.apache.org/licenses/LICENSE-2.0

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""This module provides tests for profile.py module."""

from collections import OrderedDict

import nose

from videomorph.converter.profile import ConversionProfile
from videomorph.converter.conversionlib import ConversionLib


profile = None
conv = ConversionLib()


def setup():
    """Function to setup the test."""
    global profile
    profile = ConversionProfile(prober=conv.prober_path)
    profile.update(new_quality='MP4 Fullscreen (4:3)')


def test_get_xml_profile_attr():
    """Test get_xml_profile_attr."""
    attr = profile.get_xml_profile_attr(target_quality='MP4 Fullscreen (4:3)',
                                        attr_name='preset_params')

    assert attr == '-f mp4 -r 29.97 -vcodec libx264 -s 640x480 -b:v 1000k ' \
                   '-aspect 4:3 -flags +loop -cmp +chroma -deblockalpha 0 ' \
                   '-deblockbeta 0 -maxrate 1500k -bufsize 4M -bt 256k ' \
                   '-refs 1 -bf 3 -coder 1 -me_method umh -me_range 16 ' \
                   '-subq 7 -partitions +parti4x4+parti8x8+partp8x8+partb8x8 '\
                   '-g 250 -keyint_min 25 -level 30 -qmin 10 -qmax 51 ' \
                   '-qcomp 0.6 -sc_threshold 40 -i_qfactor 0.71 -acodec aac ' \
                   '-b:a 112k -ar 48000 -ac 2 -strict -2'


def test_get_xml_profile_qualities_en():
    """Test get_xml_profile_qualities -> english."""
    qualities = profile.get_xml_profile_qualities('en_US')
    assert qualities == OrderedDict([('AVI', ['MS Compatible 640x480', 'MS Compatible 720x480', 'XVID Fullscreen 640x480 (4:3)', 'XVID Widescreen 704x384 (16:9)']), ('DVD', ['DVD Fullscreen 352x480 (4:3)', 'DVD Widescreen 352x480 (16:9)', 'DVD Fullscreen 720x480 (4:3) High Quality', 'DVD Widescreen 720x480 (16:9) High Quality', 'DVD Low Quality 720x480']), ('FLV', ['FLV Fullscreen 320x240 (4:3)', 'FLV Widescreen 320x180 (16:9)']), ('MOV', ['MOV Generic', 'Quicktime MOV Auto', 'QuickTime H.264 High quality', 'QuickTime H.264 Very High Quality']), ('MP4', ['MP4 High Quality', 'MP4 Very High Quality', 'MP4 Super High Quality', 'MP4 Fullscreen (4:3)', 'MP4 Widescreen (16:9)']), ('VCD', ['NTSC VCD High Quality', 'PAL VCD High Quality']), ('WEBM', ['WEBM Fullscreen (4:3)', 'WEBM Widescreen (16:9)']), ('WMV', ['WMV Generic']), ('MP3', ['Extract Audio mp3', 'MP3 Good Quality (160 kb)', 'MP3 High Quality (192 kb)'])])


def test_get_xml_profile_qualities_es():
    """Test get_xml_profile_qualities -> spanish."""
    qualities = profile.get_xml_profile_qualities('es_ES')
    assert qualities == OrderedDict([('AVI', ['Compatible MS 640x480', 'Compatible MS 720x480', 'XVID Pantalla Completa 640x480 (4:3)', 'XVID Pantalla Panorámica 704x384 (16:9)']), ('DVD', ['DVD Pantalla Completa 352x480 (4:3)', 'DVD Pantalla Panorámica 352x480 (16:9)', 'DVD Pantalla Completa 720x480 (4:3) Alta Calidad', 'DVD Pantalla Panorámica 720x480 (16:9) Alta Calidad', 'DVD Baja Calidad 720x480']), ('FLV', ['FLV Pantalla Completa 320x240 (4:3)', 'FLV Pantalla Panorámica 320x180 (16:9)']), ('MOV', ['MOV Genérico', 'Quicktime MOV Auto', 'QuickTime H.264 Alta Calidad', 'QuickTime H.264 Muy Alta Calidad']), ('MP4', ['MP4 Alta Calidad', 'MP4 Muy Alta Calidad', 'MP4 Súper Alta Calidad', 'MP4 Pantalla Completa (4:3)', 'MP4 Pantalla Panorámica (16:9)']), ('VCD', ['VCD Alta Calidad', 'PAL VCD Alta Calidad']), ('WEBM', ['WEBM Pantalla Completa (4:3)', 'WEBM Pantalla Panorámica (16:9)']), ('WMV', ['WMV Genérico']), ('MP3', ['Extraer Audio mp3', 'MP3 Buena Calidad (160 kb)', 'MP3 Alta Calidad (192 kb)'])])


# Tests for _Profile class
def test_quality_tag():
    """Test _Profile.quality_tag."""
    assert profile.quality_tag == '[MP4F]-'


def test_quality_tag_no_regex_tag():
    """Test _Profile.quality_tag if not regex tag."""
    global profile
    profile.update(new_quality='wmv generic')
    print(profile.quality_tag)
    assert profile.quality_tag == '[WG]-'


def test_update():
    """Test update."""
    profile.update(new_quality='WMV Generic')
    assert profile.params == '-vcodec wmv2 -acodec wmav2 -b:v 1000k ' \
                             '-b:a 160k -r 25'
    assert profile.extension == '.wmv'


if __name__ == '__main__':
    nose.main()
