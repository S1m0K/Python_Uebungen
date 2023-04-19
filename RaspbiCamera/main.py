from picamera import PiCamera
from time import sleep
import json
from PIL import Image

camera = PiCamera()
sleep(5)
camera.capture('/home/pi/image.jpg')


im = Image.open('/home/pi/image.jpg')

breite, hoehe = im.size
data = {'breite': breite, 'hoehe': hoehe, 'format': im.format, 'mode': im.mode}
j2 = json.dumps(data)

