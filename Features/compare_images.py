#thank you to Nllesh Sharma on stackoverflow for majority of this function
import ImageChops
import Image

def equal(im1, im2):
    im1 = Image.open(im1)
    im2 = Image.open(im2)
    return ImageChops.difference(im1, im2).getbbox() is None

