from TrimExtraction_Services.DynamoDB import dynamoDB
from datetime import datetime
import uuid


def log_msg(action = "NA",imageName = "NA" ,imageID = "NA", trimInformation = "NA", imageUrl = "NA",maker = "NA" ):
    msg, imageId = build_msg(action,imageID,imageName,trimInformation,imageUrl,maker)
    dynamoDB.log_entry(msg)
    return imageId


def build_msg(action, imageID, imageName, trimInformation, imageUrl,maker):
    imageId = uuid.uuid4().hex if imageID == "NA" else imageID
    msg = {
        "ImageID": imageId,
        "Action": action,
        "ImageName":  imageName,
        "DateCapture": datetime.now().strftime("%m/%d/%Y %H:%M:%S.%f"),
        "TrimInformation":  trimInformation,
        "ImageURL":  imageUrl,
        "MakerInformation":  maker
    }
    return msg, imageId
