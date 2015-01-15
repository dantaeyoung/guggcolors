#!/usr/bin/python

import re
import urllib2
import json
import os
import subprocess

DOMAIN = "https://s3-us-west-2.amazonaws.com/api.designguggenheimhelsinki.org/"
VERSION = "v1/"
DATA_DIRECTORY = "data/"
DIRECTORY_URL = "https://s3-us-west-2.amazonaws.com/api.designguggenheimhelsinki.org/v1/directory.json"

API_BASE_URL = DOMAIN + VERSION + DATA_DIRECTORY + VERSION

FILE_BASE_LOCATION = '/var/www/vps.provolot.com/public_html/GITHUB/guggdata/data/'
source = urllib2.urlopen(DIRECTORY_URL)
data = json.load(source)   

averageColor = {}

for i, entry in enumerate(data['submissions']):
	print "==", i, "===", entry

	try:
		source = urllib2.urlopen(API_BASE_URL + entry['id'] + '/' + entry['data']['images']['press_image_1'])
		filename = FILE_BASE_LOCATION + entry['id'] + '/' + entry['data']['images']['press_image_1']

		if not os.path.exists(filename):

			if not os.path.exists(FILE_BASE_LOCATION + entry['id']):
				os.makedirs(FILE_BASE_LOCATION + entry['id'])
			f = open(filename, 'w')
			f.write(source.read())
			print filename

		print ['convert', filename, "-resize", "1x1", "txt:"]
		p = subprocess.Popen(['convert', filename, "-resize", "1x1", "txt:"], stdout=subprocess.PIPE)
		#p = subprocess.Popen(['gm', 'identify', filename], stdout=subprocess.PIPE)
		convertResult = p.communicate()[0]
		print convertResult
		res = re.findall('srgb\((\d*),(\d*),(\d*)\)',convertResult)
		r = res[0][0]
		g = res[0][1]
		b = res[0][2]

		averageColor[i] = {}
		averageColor[i]['id'] = entry['id']
		averageColor[i]['p1_r'] = r
		averageColor[i]['p1_g'] = g
		averageColor[i]['p1_b'] = b
		averageColor[i]['p1'] = entry['data']['images']['press_image_1']

	except Exception, e:
		print e

with open('avgColors.json', 'w') as f:
	f.write(json.dumps(averageColor, indent=4))


