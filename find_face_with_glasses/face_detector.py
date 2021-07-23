from mtcnn import MTCNN
import cv2


def detect_faces(image):
    img = cv2.cvtColor(cv2.imread(image), cv2.COLOR_BGR2RGB)
    detector = MTCNN()
    return detector.detect_faces(img)


def is_one_and_suitable(image):
    faces = detect_faces(image)
    amount_faces = len(faces)

    if amount_faces == 1:
        size = faces[0]['box']  # 'box': [x, y, width, height]

        if size[-1] >= 256 and size[-2] >= 256:
            return True
