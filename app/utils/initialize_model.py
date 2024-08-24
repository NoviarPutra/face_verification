import os
from deepface import DeepFace


def initialize_model():
    try:
        print("Downloading VGG-Face model...")
        # Initialize download by running a dummy verification
        img_path1 = "_assets/dummy1.jpg"
        img_path2 = "_assets/dummy2.jpg"

        DeepFace.verify(img1_path=img_path1, img2_path=img_path2, model_name="VGG-Face")
        print("VGG-Face model downloaded successfully.")
    except Exception as e:
        print(f"Error downloading VGG-Face model: {e}")


if __name__ == "__main__":
    initialize_model()
