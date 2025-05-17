import cv2 as cv
import face_recognition as fr
import os


# Import Functions
# Read All Images and Generate the encodings
def encodings_for_known_images():
    path = './images'
    known_encodings = dict()
    for image in os.listdir(path):
        img = cv.imread(f'{path}/{image}')
        img = cv.resize(img, (512, int(img.shape[0] * (512 / img.shape[1]))))
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        encoding = fr.face_encodings(img)

        if len(encoding) == 0:
            print(f"No face found in {image}, skipping.")
            continue

        name = image.split('.')[0].upper()
        known_encodings[name] = encoding[0]
    
    return known_encodings

known_encodings = encodings_for_known_images()


camera = cv.VideoCapture(0)





while camera.isOpened():
    retn, frame = camera.read()

    if retn:
        frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        frame_encoding = fr.face_encodings(frameRGB)

        if len(frame_encoding) == 0:
            continue

        face_locations = fr.face_locations(frameRGB)
        iy, fx, fy, ix = face_locations[0]

        name = 'Unknown'
        for key, value in known_encodings.items():
            match = fr.compare_faces([value], frame_encoding[0])
            if match[0]:
                name = key
                break
                
        
        cv.rectangle(frame, pt1=(ix, iy), pt2=(fx, fy), color=(0,255, 0), thickness=2)
        cv.rectangle(frame, pt1=(ix, iy), pt2=(fx, iy-30), color=(0,255, 255), thickness=-1)
        cv.putText(frame, org=(ix+30, iy-5),text= name , fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1.5, color=(0, 0, 0), thickness=1)
        
        cv.imshow("My Camera", frame)

        if cv.waitKey(1) == ord('q'):
            break
    else:
        print("Camera is busy.")
        break

camera.release()
cv.destroyAllWindows()