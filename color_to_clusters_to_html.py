#!/usr/bin/python

import re
import urllib2
import json
import os
import numpy
import matplotlib
matplotlib.use('Agg')
from scipy.cluster.vq import *
import pylab
pylab.close()
from collections import defaultdict
from colormath.color_conversions import convert_color
from colormath.color_objects import LabColor, LCHabColor, SpectralColor, sRGBColor, XYZColor, LCHuvColor, IPTColor

def rgb_to_lab(rgbtuple):
    labColor = convert_color(sRGBColor(rgbtuple[0],rgbtuple[1],rgbtuple[2], is_upscaled=True), LabColor)
    return labColor.get_value_tuple()

def lab_to_rgb(rgbtuple, hex=False):
    srgbColor = convert_color(LabColor(rgbtuple[0],rgbtuple[1],rgbtuple[2]), sRGBColor)
    if(hex):
        return srgbColor.get_rgb_hex()
    return srgbColor.get_upscaled_value_tuple()

json_data = open('jsons/avgColors.json').read()
data = json.loads(json_data)

id_to_rgb = {int(k): map(lambda x: int(x), (v['p1_r'], v['p1_g'], v['p1_b'])) for k,v in data.iteritems()}

id_to_lab = {k: rgb_to_lab(v) for k, v in id_to_rgb.iteritems()}

clusters, groups = kmeans2( numpy.array(id_to_lab.values()), 5)

id_to_groups = dict(zip(id_to_lab.keys(), groups))

groups_to_ids = defaultdict(list)

for i, g in id_to_groups.iteritems():
    groups_to_ids[g].append(i)

with open('index.html', 'w') as f:
    f.write('<html>\n')
    f.write('<head>\n')
    f.write('  <title>the 5 colors 1,715 architecture firms think the helsinki guggenheim should look like</title>\n')
    f.write('<meta name="description" content="the 5 colors 1,715 architecture firms think the helsinki guggenheim should look like" />')
    f.write('  <link rel="stylesheet" href="css/guggclusters.css">\n')
    f.write('  <script src="https://code.jquery.com/jquery-1.11.2.min.js"></script>\n')
    f.write('  <script src="js/guggclusters.js"></script>\n')
    f.write('</head>\n')
    f.write('<body>\n')
    f.write('<div class="title">the 5 colors<br> 1,715 architecture firms think<br> the helsinki guggenheim<br> should look like</div>\n')
    f.write('<div class="subtitle">(<a href="https://github.com/provolot/guggcolors">github repo.</a> version v.01_hacked_together. warning: full-size images, very slow. <a href="twitter.com/provolot">@provolot</a>)</div>\n')

    for g, ids in groups_to_ids.iteritems():
        f.write('<div class="cluster cluster-%s" data-cluster="%s">\n' % (str(g), lab_to_rgb(clusters[g], hex=True)))
        f.write('  <div class="cluster-color" style="background-color:%s"></div>\n' % lab_to_rgb(clusters[g], hex=True))
        f.write('  <div class="entries">\n')

        for thisid in ids:
            thishex = lab_to_rgb(rgb_to_lab(id_to_rgb[thisid]), hex=True) #too lazy tom ake this simpler
            entryid = data[str(thisid)]['id']
            url = 'data/' + entryid + '/' + data[str(thisid)]['p1']
            f.write('    <div class="entry">\n')
            f.write('      <div class="color" style="background-color:%s"></div>\n' %  thishex)
            f.write('      <div class="image"><img src="%s"></div>\n' % url)
            f.write('    </div>\n')

        f.write('  </div>\n')
        f.write('</div>\n')
    #for key, value in sorted(d.iteritems()):

    trackingCode = """
<!-- Start of StatCounter Code for Default Guide -->
<script type="text/javascript">
var sc_project=10238263; 
var sc_invisible=1; 
var sc_security="8d5c2d0a"; 
var scJsHost = (("https:" == document.location.protocol) ?
		"https://secure." : "http://www.");
document.write("<sc"+"ript type='text/javascript' src='" +
		scJsHost+
		"statcounter.com/counter/counter.js'></"+"script>");
</script>
<noscript><div class="statcounter"><a title="free hit
			counter" href="http://statcounter.com/free-hit-counter/"
			target="_blank"><img class="statcounter"
			src="http://c.statcounter.com/10238263/0/8d5c2d0a/1/"
			alt="free hit counter"></a></div></noscript>
<!-- End of StatCounter Code for Default Guide -->"""
    f.write(trackingCode)
    f.write('</body></html>\n')

