# filter-me
Add filters to your photos

## Written by Jason Hong and Jeffrey Li

### Dependencies
```
pip install -r requirements.txt
```

### Usage
To add a filter,

Using ImageMagick, remove the white background, and trim the alpha along the edges. The source file must be a .png file.

```
convert SRC_IMAGE.png -fuzz 10%% -transparent white DEST_IMAGE.png
convert SRC_IMAGE.png -trim +repage DEST_IMAGE.png
```

To run,

```
python face_detect_cv2.py     # uses the opencv library 
python face_detect_fr.py      # uses the face-detection library (much more accurate)
```

### DONE
1. Rectangle around the face with opencv, traced facial features with face-recog

### TODO
1. Algorithm to align filter with features
