import os
from google.oauth2 import service_account
import googleapiclient.discovery
import io
import json
from google.cloud import vision
import cv2
from TrimExtraction.Logging import logger


print(os.pardir)
dir_path = os.path.dirname(os.path.realpath(__file__))
keyPath = dir_path+"/google-vision-api.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = keyPath
credentials = service_account.Credentials.from_service_account_file(
    filename=os.environ['GOOGLE_APPLICATION_CREDENTIALS'],
    scopes=['https://www.googleapis.com/auth/cloud-platform'])

def extract_text(img, imageName, imageId):
    try:
        # cv2.imshow("img",img)
        # cv2.waitKey()
        imageId = logger.log_msg(action="extracting Text",imageName=imageName, trimInformation="NA", imageID=imageId)
        client = vision.ImageAnnotatorClient()

        # with io.open(path, 'rb') as image_file:
        #     content = image_file.read()

        content = cv2.imencode(".jpg",img)[1].tostring()
        image = vision.types.Image(content=content)

        response = client.text_detection(image=image)
        texts = response.text_annotations
        print('Texts:')
        trimInformation = []
        for text in texts:
            print('\n"{}"'.format(text.description))
            trimInformation.append(text.description.replace("\n",""))

            vertices = (['({},{})'.format(vertex.x, vertex.y)
                        for vertex in text.bounding_poly.vertices])

            print('bounds: {}'.format(','.join(vertices)))

        print(trimInformation)
        return list(dict.fromkeys(trimInformation))
    except Exception as identifier:
        print(str(identifier))
#detect_text("Acura 2010 SH-AWD Luxury Car.jpg")
