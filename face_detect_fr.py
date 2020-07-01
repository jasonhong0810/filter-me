from PIL import Image, ImageDraw
import face_recognition

# Load jpg
image = face_recognition.load_image_file("./images/obama.jpg")

# Load filter
mask = Image.open("./filters/fdog.png")

# Find filter median
fwidth, fheight = mask.size
fx = int(fwidth/2)
fy = int(fheight/2)

# Find facial features
face_landmarks_list = face_recognition.face_landmarks(image)

# PIL imagedraw to modify the picture
f_image = Image.fromarray(image)
d = ImageDraw.Draw(f_image)

for face_landmarks in face_landmarks_list:
  for facial_feature in face_landmarks.keys():
       print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))
  for facial_feature in face_landmarks.keys():
        d.line(face_landmarks[facial_feature], width=1)
        print(facial_feature)

# Place rectangele around facial features


# combine mask
f_image.paste(mask,(479-fx,244-fy),mask)

# Show the picture
f_image.show()
