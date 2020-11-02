import base64
import io, json
from PIL import Image
import requests
import matplotlib.pyplot as plt


# convert base64 strings to 
def base64str_to_PILImage(base64str):
   base64_img_bytes = base64str.encode('utf-8')
   base64bytes = base64.b64decode(base64_img_bytes)
   bytesObj = io.BytesIO(base64bytes)
   img = Image.open(bytesObj) 
   return img

payloads = json.dumps({
  "path": "./app/seq-01/frame-000993.color.png"
})

## response.json() is the base64str of the image
response = requests.put("http://0.0.0.0:900/predict",data = payloads)
print(response)
data = response.json()

img = base64str_to_PILImage(data)

imgplot = plt.imshow(img)

plt.show()
