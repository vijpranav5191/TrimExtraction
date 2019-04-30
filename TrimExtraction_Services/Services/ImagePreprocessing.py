import numpy as np
import cv2
from scipy import ndimage
from TrimExtraction_Services.Logging import logger


def masking(img):
    mask = np.zeros(img.shape[:2],np.uint8)
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)
    rect = (1,1,665,344)
    cv2.grabCut(img,mask,rect,bgdModel,fgdModel,8,cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img = img*mask2[:,:,np.newaxis]
    return img

def preprocessImage(img, imageId, imageName):
    imageId = logger.log_msg(action="Preprocessing",imageName=imageName, trimInformation="NA", imageID=imageId)
    img = masking(img)
    img = ndimage.rotate(img, 180)
    img = masking(img)
    img = ndimage.rotate(img, 180)
    img = 255 - img
    return img
