from __future__ import print_function
import requests
import json
import cv2

image = Image.open('/home/mmaskur/mysite/test1.jpg')
image.show()

addr = 'http://vikifebri7219.pythonanywhere.com/api/test'
test_url = addr + '/api/test'

# prepare headers for http request
content_type = 'home/mmaskur/mysite/test1.jpg'
headers = {'content-type': content_type}

img = cv2.imread('test1.jpg')
# encode image as jpeg
_, img_encoded = cv2.imencode('.jpg', img)
# send http request with image and receive response
response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
# decode response
print(json.loads(response.text))

# expected output: {u'message': u'image received. size=124x124'}