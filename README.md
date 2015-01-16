# guggcolors, or the 5 colors 1,715 architecture firms think the helsinki guggenheim should look like

There are two scripts:
1) gugg_to_color.py
2) color_to_clusters_to_html.py

*gugg_to_color.py*
uses the Guggenheim API and downloads the first image from each entry, uses imagemagick to get the average color of the image, and saves the data as a json file.

*color_to_clusters_to_html.py*
opens the JSON file;with scipy and scikit-image, converts the RGB color to LAB values, does a k-means clustering (with k=5) to group the data into 5 groups, and writes to an html file.
 
**Things to do that I will probably never get around to doing:**
- Use an image resizing service or imagemagick to make nice thumbnails so that the entire site loads faster
- Rather than getting average colors, get all the colors the image uses, and cluster those values
- Pixelate the images into 3x3 so that you can actually get averages of different quadrants/zones (horizon, sky, ground). (As an aside, many metering systems in cameras are pre-optimized to target different EV values in different zones to compensate for sky vs. ground, etc: [https://www.cameraquest.com/jpg6/Bessa-R%20meter.jpg]
- Does Helsinki actually look like this? Get the top 1715 images of Helsinki on Flickr (or instagram, etc) and do the same. Who knows; maybe these finalists are actually just very accurate.
