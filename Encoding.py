import face_recognition
import time

image_a1 = face_recognition.load_image_file("uploads/a1.jpg")
image_a2 = face_recognition.load_image_file("uploads/a2.jpg")
image_b1 = face_recognition.load_image_file("uploads/b1.jpg")

start = time.time()
encodings_a1 = face_recognition.face_encodings(image_a1)[0]

elapsed = time.time() - start
print("The time it took to encode the image is  ", elapsed, " seconds")

encodings_a2 = face_recognition.face_encodings(image_a2)[0]
encodings_b1 = face_recognition.face_encodings(image_b1)[0]

if len (encodings_a1) == 0 or len(encodings_a2) == 0 or len(encodings_b1) == 0:
    print("The scanned face was not found in your known faces database. Please try again.")
else:
    print("The scanned face was found in your known faces database.")

same_person = face_recognition.compare_faces([encodings_a1], encodings_a2)
different_person = face_recognition.compare_faces([encodings_a1], encodings_b1)

print("Same person: ", same_person)
print("Different person: ", different_person)