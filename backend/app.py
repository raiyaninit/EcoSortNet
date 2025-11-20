from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

# Load trained model
MODEL_PATH = "../model/waste_model.h5"
model = load_model(MODEL_PATH)
CLASS_NAMES = ['Organic', 'Recyclable']

def prepare_image(img, target_size=(150,150)):
    if img.mode != "RGB":
        img = img.convert("RGB")
    img = img.resize(target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

@app.route("/predict", methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        # Open image from memory
        img = Image.open(file.stream)
        img_array = prepare_image(img)
        pred = model.predict(img_array)
        class_idx = np.argmax(pred, axis=1)[0]
        class_name = CLASS_NAMES[class_idx]

        return jsonify({"prediction": class_name})
    except Exception as e:
        # Return the actual error for debugging
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("Backend server is running at http://127.0.0.1:5000")
    app.run(debug=True)
