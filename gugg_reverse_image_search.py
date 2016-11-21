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

for i, entry in enumerate(data['submissions'][:3]):
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


                req = urllib2.Request("https://sender.blockspring.com/api_v2/blocks/4521f0eb2b5658d71ab4cf25a7af0a0c?api_key=947b009aeaa33b92c20db3012884c3de")
                req.add_header('Content-Type', 'application/json')

                data = {"image_url": "http://vps.provolot.com/GITHUB/guggdata/data/" + entry['id'] + '/' + entry['data']['images']['press_image_1']}

                print data

                results = urllib2.urlopen(req, json.dumps(data)).read()

                print json.loads(results)

	except Exception, e:
		print e

#with open('avgColorsScale.json', 'w') as f:
#	f.write(json.dumps(averageColor, indent=4))


