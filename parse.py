#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as et

def to_utf8_xml(sjis_xml):
    sjis_xml = unicode(sjis_xml, 'cp932')
    sjis_xml = sjis_xml.replace('encoding="Shift_JIS"', 'encoding="utf-8"')
    return sjis_xml.encode('utf-8')


def print_xml(filename):
    print filename
    print

    # open xml as text file and convert charset from sjis to utf-8
    data = open(filename).read()
    data = to_utf8_xml(data)

    # parse xml from string
    xml = et.fromstring(data)

    ## extract unit tag
    for unit in xml.findall("TEXT/unit"):
        attributes = unit.attrib
        for a, v in attributes.items():
            print 'attributes:', a.encode('utf-8'), v.encode('utf-8')

        for e in unit.findall('*'):
            print e.tag, e.text.encode('utf-8') if e.text else ''

        print


if __name__ == '__main__':
    import os
    import sys

    filenames = sys.argv[1:]

    for filename in filenames:
        print_xml(filename)
