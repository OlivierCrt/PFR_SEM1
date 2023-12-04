import cv2
import numpy as np

image = cv2.imread('python_shapes_detection_base.png')
if image is None:
    print("L'image n'a pas pu être chargée.")
    exit()

#  RGB en HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)








def detect_bleu() :
    lower_blue = np.array([90, 50, 50])  
    upper_blue = np.array([130, 255, 255])

    # filtre/masque
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    #contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #contours
    for contour in contours:
        # delta plage de detection , on enleve les trucs trop petit
        if cv2.contourArea(contour) > 1000:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    
def detect_rouge() :
    lower_red = np.array([0, 50, 50])       # Rouge vif à l'extrémité inférieure du spectre HSV
    upper_red = np.array([10, 255, 255])

    

    # filtre/masque
    mask = cv2.inRange(hsv, lower_red, upper_red)#on filtre les pixel, si oui ou non ils sont dans la plage, en binaire noir ou blanc, on a donc en evidence les formes dans la p^lage il ne reste plus qu a les entouré en evitant les bruits

    #contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)#ici on met ,_ par convention afin de signaler que la deuxieme valeur de bleu renvoyé par la fonction n est pas utilisé

    #contours
    for contour in contours:
        # delta plage de detection , on enleve les trucs trop petit
        if cv2.contourArea(contour) > 1000:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)


def detect_vert() :
    lower_green = np.array([40, 50, 50])    # Vert vif à l'extrémité inférieure du spectre HSV
    upper_green = np.array([80, 255, 255])
    

    # filtre/masque
    mask = cv2.inRange(hsv, lower_green, upper_green)

    #contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #contours
    for contour in contours:
        # delta plage de detection , on enleve les trucs trop petit
        if cv2.contourArea(contour) > 1000:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)



detect_bleu()
detect_rouge()
detect_vert()

# Sauvegarder l'image
cv2.imwrite('resultat_detection.jpg', image)
