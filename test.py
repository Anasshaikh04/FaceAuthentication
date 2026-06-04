import cv2
import numpy as np
from insightface.app import FaceAnalysis

# Load model once at startup
recognizer = FaceAnalysis(name="buffalo_l")
recognizer.prepare(ctx_id=-1)


def compute_similarity(emb_a, emb_b):
    # Cosine similarity between two face embeddings
    dot_product = np.dot(emb_a, emb_b)
    magnitude = np.linalg.norm(emb_a) * np.linalg.norm(emb_b)
    return dot_product / magnitude


def check_faces(photo_a_path, photo_b_path):

    # Read both images from disk
    photo_a = cv2.imread(photo_a_path)
    photo_b = cv2.imread(photo_b_path)

    if photo_a is None:
        return {"error": "Could not open first image"}

    if photo_b is None:
        return {"error": "Could not open second image"}

    # Detect faces in each image
    detected_a = recognizer.get(photo_a)
    detected_b = recognizer.get(photo_b)

    if len(detected_a) == 0:
        return {"error": "No face found in first image"}

    if len(detected_b) == 0:
        return {"error": "No face found in second image"}

    # Get embeddings from the first detected face in each image
    face_vector_a = detected_a[0].embedding
    face_vector_b = detected_b[0].embedding

    # Calculate how similar the two faces are
    score = float(compute_similarity(face_vector_a, face_vector_b))

    # Threshold: above 0.60 means same person
    match_result = "same person" if score > 0.60 else "different person"

    return {
        "verification_result": match_result,
        "similarity_score": round(score, 4),
        "bounding_box_image1": detected_a[0].bbox.tolist(),
        "bounding_box_image2": detected_b[0].bbox.tolist()
    }
