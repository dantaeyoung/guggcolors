# guggcolors, or the 5 colors everyone thinks the helsinki guggenheim should look like

There are two scripts:
1) gugg_to_color.py
2) color_to_clusters_to_html.py

*gugg_to_color.py*
uses the Guggenheim API and downloads the first image from each entry, uses imagemagick to get the average color of the image, and saves the data as a json file.

*color_to_clusters_to_html.py*
opens the JSON file;with scipy and scikit-image, converts the RGB color to LAB values, does a k-means clustering (with k=5) to group the data into 5 groups, and writes to an html file.
 