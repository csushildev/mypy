#import the module for the qrcode generation.
import pyqrcode

link = "https://www.youtube.com/@matchalattepocs"

#this will create the qrcode data
url=pyqrcode.create(link)

#this wil crate the qrcode scannable image
url.svg("matchalatteqr.svg", scale=10)