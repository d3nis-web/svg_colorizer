#!/usr/bin/env python
#coding:utf-8
import os
import sys
import re
import xml.etree.ElementTree as ET
print('''
┌─┐┬  ┬┌─┐  ┌─┐┌─┐┬  ┌─┐┬─┐┬┌─┐┌─┐┬─┐
└─┐└┐┌┘│ ┬  │  │ ││  │ │├┬┘│┌─┘├┤ ├┬┘
└─┘ └┘ └─┘  └─┘└─┘┴─┘└─┘┴└─┴└─┘└─┘┴└─
	''')
svg_folder = False
svg_color = False
print("path to folder with svg icons:")
svg_folder = raw_input()
print("color:")
svg_color = raw_input()
try:
	for i in filter(lambda x: re.search("\.svg$",str(x)) ,os.listdir(svg_folder)):
		filepath = os.path.join(svg_folder,i)
		tree = ET.parse(filepath)
		root = tree.getroot()
		root.set('fill',svg_color)
		tree.write(filepath)
		print("[+] {} done".format(filepath))
except Exception as e:
	print(e)