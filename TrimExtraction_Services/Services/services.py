import cv2
import numpy
from TrimExtraction_Services.DynamoDB import dynamoDB
from TrimExtraction_Services.Services import ImagePreprocessing as ip
from TrimExtraction_Services.Logging import logger
from TrimExtraction_Services.TextDetection import googleVision as gv
import json

def process_image(inputImg, imageId, imageName):
    img = cv2.imdecode(numpy.fromstring(inputImg, numpy.uint8), cv2.IMREAD_UNCHANGED)
    imageId = logger.log_msg(action="Processing",imageName=imageName, trimInformation="NA", imageID=imageId)
    img = ip.preprocessImage(img, imageId, imageName)
    trimInformation = gv.extract_text(img, imageName, imageId)
    logger.log_msg(action="extracting Text",imageName=imageName, trimInformation=json.dumps(trimInformation), imageID=imageId)

    return json.dumps(trimInformation)

    # East dataset code here to get the chunks of images from larger images



    # foreach image run masking and then vision api to extract details of the text
