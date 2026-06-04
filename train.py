from insightface.app import FaceAnalysis


def setup_model():
    # Load the InsightFace buffalo_l model on CPU
    recognizer = FaceAnalysis(name="buffalo_l")

    recognizer.prepare(
        ctx_id=-1,
        det_size=(640, 640)
    )

    print("Model loaded and ready.")

    return recognizer


if __name__ == "__main__":
    setup_model()
