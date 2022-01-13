from PIL import Image
import face_recognition

# Load the jpg file into a numpy array
img = face_recognition.load_image_file("assets/purpleGroup")


# Find all the faces in the image using the default HOG-based model.
# This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
# See also: find_faces_in_picture_cnn.py
face_locations = face_recognition.face_locations(img)

for face_location in face_locations:
    # Print the location of each face in this image
    top, right, bottom, left = face_location

    # You can access the actual face itself like this:
    face_image = img[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()