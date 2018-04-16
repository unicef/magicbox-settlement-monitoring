#!/usr/bin/python
# GoogleSatelliteImageDownloader.py 
#
# A script which when given a longitude, latitude and zoom level downloads a
# high resolution google satellite image

import io
from urllib2 import Request, urlopen, URLError
import  PIL
from PIL import Image


class GoogleSatelliteImageDownloader:
    """
        A class which generates high resolution google maps images given
        a longitude, latitude and zoom level
    """

    def __init__(self, lat, lng, zoom=12):
        """
            GoogleMapDownloader Constructor

            Args:
                lat:    The latitude of the location required
                lng:    The longitude of the location required
                zoom:   The zoom level of the location required, ranges from 0 - 23
                        defaults to 12
        """
        self._lat = lat
        self._lng = lng
        self._zoom = zoom
        print("I am here")

    

    def getImage(self):

        """
            Calls google static maps api to download satellite imagery at specified lat, long, zoom, scale, height & width
        """

        global apikey
        apikey = "AIzaSyCkjcI42PXt1iL9cPHwk6T2p6ZXfOVFjKI"
        width = 640
        height = 400
        image = Image.new('RGB', (width,height))
        url = "https://maps.googleapis.com/maps/api/staticmap?maptype=satellite&center=%s,%s&zoom=%s&size=%sx%s&scale=2&key=%s" % (self._lat, self._lng, self._zoom,width,height,apikey)
        print("url: "+url)
        request = Request(url)
        try:
            response = urlopen(request).read()
            print("Received response")
            image = Image.open(io.BytesIO(response))
        except URLError, e:
            print 'No images. Got an error code:', e
        return image

def main():
    # Create a new instance of GoogleMap Downloader
    latitude = 35.7976
    longitude = 43.2932
    gsid = GoogleSatelliteImageDownloader(latitude,longitude, 13)

    try:
        # Get the high resolution image
        img = gsid.getImage()
    except IOError:
        print("Could not generate the image - try adjusting the zoom level and checking your coordinates")
    else:
        #Save the image to disk
        img.save("satellite_image_"+str(latitude)+"_"+str(longitude)+".png")
        print("The map has successfully been created")

if __name__ == '__main__':  main()
