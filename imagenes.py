import numpy as np
import cv2
import os

def Setup(yolo):
    global net, ln, LABELS
    weights = os.path.sep.join([yolo, "yolov3.weights"])
    config = os.path.sep.join([yolo, "yolov3.cfg"])
    labelsPath = os.path.sep.join([yolo, "coco.names"])
    LABELS = open(labelsPath).read().strip().split("\n")
    net = cv2.dnn.readNetFromDarknet(config, weights)
    ln = net.getLayerNames() #layer_names
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()] #output layers

def img(path):
    yolo = "yolo-coco/"
    Setup(yolo)
    CLASSES = ["car", "motorbike"]
    COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),
	dtype="uint8")



    font = cv2.FONT_HERSHEY_PLAIN


    img=cv2.imread(path)
    img=cv2.resize(img, None, fx=0.6, fy=0.6)
    H, W, channels = img.shape
#detecting ImageProcess

    blob = cv2.dnn.blobFromImage(img, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    layerOutputs = net.forward(ln)
    confidences = []
    outline = []
    classIDs = []
    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]

            if LABELS[classID] == "motorbike" :
                if confidence > 0.6:
                # Object detected
                    center_x = int(detection[0] * W)
                    center_y = int(detection[1] * H)
                    w = int(detection[2] * W)
                    h = int(detection[3] * H)
            # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    outline.append([x, y, w, h])
                    confidences.append(float(confidence))
                    classIDs.append(classID)
            elif LABELS[classID] == 'car':
                if confidence > 0.6:
                    # Object detected
                    center_x = int(detection[0] * W)
                    center_y = int(detection[1] * H)
                    w = int(detection[2] * W)
                    h = int(detection[3] * H)
                # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    outline.append([x, y, w, h])
                    confidences.append(float(confidence))
                    classIDs.append(classID)


    idxs = cv2.dnn.NMSBoxes(outline, confidences, 0.5, 0.4)

    for i in range(len(outline)):
    	# loop over the indexes we are keeping
    	if i in idxs:
    		# extract the bounding box coordinates
    		(x, y) = (outline[i][0], outline[i][1])
    		(w, h) = (outline[i][2], outline[i][3])
    		# draw a bounding box rectangle and label on the image
    		color = [int(c) for c in COLORS[classIDs[i]]]
    		cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
    		text = "{}: {:.4f}".format(LABELS[classIDs[i]], confidences[i])
    		cv2.putText(img, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
    			0.5, color, 2)
    # show the output image


    cv2.imshow('Image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':

    print('Enter the img file path')

    path = input()

    img(path)
