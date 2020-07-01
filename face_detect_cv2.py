import cv2

# Image path location
image_path = "./images/obama.jpg"

# Load cascade
cascade = cv2.CascadeClassifier('./assets/haarcascade_frontalface_default.xml')

# Load image
image = cv2.imread(image_path)

print(image)

# cv2 takes only grayscale image
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = cascade.detectMultiScale(grayscale, scaleFactor = 1.1, minNeighbors = 4, minSize = (30,30))

for (x,y,w,h) in faces:
  cv2.rectangle(image, (x,y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('image', image)
cv2.waitKey(0)
