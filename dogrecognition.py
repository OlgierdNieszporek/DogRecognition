import tensorflow as tf
import numpy as np

import matplotlib.pyplot as plt

from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import imagenet_utils

def recognizeDog(filename):
    filename = 'uploads/' + filename

    # resnet = tf.keras.applications.resnet50.ResNet50()
    # lets try another nodel
    mobile = tf.keras.applications.mobilenet_v2.MobileNetV2()

    img = image.load_img(filename, target_size=(224, 224))  # the model works with 224X224 resolution

    resizedImage = image.img_to_array(img)
    print("Resized image shape")
    print(resizedImage.shape)

    imageWithMoreDimantion = np.expand_dims(resizedImage, axis=0)
    print("imageWithMoreDimantion image shape")
    print(imageWithMoreDimantion.shape)

    finalImage = tf.keras.applications.mobilenet.preprocess_input(imageWithMoreDimantion)

    predictions = mobile.predict(finalImage)

    results = imagenet_utils.decode_predictions(predictions)

    print('Results :')
    print(results)

    return prepareResults(results)

    # show the image
    # plt.imshow(img)
    # plt.show()


def prepareResults(results):
    possibleBreedsTable = []
    possibleBreed = results[0][0][1]
    parsedName = parseToName(possibleBreed)
    possibleBreedsTable.append(parsedName)
    certainty = results[0][0][2]
    parsedCertainty = parseToPercent(certainty)
    possibleBreedsTable.append(parsedCertainty)
    return possibleBreedsTable


def parseToPercent(certainty):
    parsedValue = round(float(certainty), 2)*100
    return parsedValue


def parseToName(possibleBreed):
    if possibleBreed.find("_") != -1:
        possibleBreed.replace("_", " ")
        return possibleBreed.capitalize()
    else:
        return possibleBreed.capitalize()
