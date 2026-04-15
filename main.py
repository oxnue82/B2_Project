import os
import numpy as np
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)
app.secret_key="7103"

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

chilli_model = load_model("Models/chilli_model.h5")
cotton_model = load_model("Models/cotton_model.h5")
maze_model = load_model("Models/maze_model.h5")
rice_model = load_model("Models/rice_model.h5")


chilli_classes = [
    "Chilli Whitefly",
    "Chilli Yellowish",
    "Chilli Healthy"
]

cotton_classes = [
    "Bacterial Blight",
    "Curl Virus",
    "Fussarium Wilt",
    "Healthy"
]

maze_classes = [
    "Blight",
    "Common Rust",
    "Gray Leaf Spot",
    "Healthy"
]

rice_classes = [
    "Bacterial Blight",
    "Brown Spot",
    "Leaf Smut"
]

product_recommendations = {

    "Chilli Whitefly": [
        {"name": "Neem Oil Spray", "image": "static/products/neem oil.jpg"}
    ],

    "Chilli Yellowish": [
        {"name": "Micronutrient Fertilizer", "image": "static/products/micronutrient.jpg"},
    ],

    "Bacterial Blight": [
        {"name": "Copper Oxychloride Fungicide", "image": "static/products/copper.jpeg"},
    ],

    "Curl Virus": [
        {"name": "Thiamethoxam Insecticide", "image": "static/products/thiamethoxam.jpg"},
    ],
    "Fussarium Wilt": [
        {"name": "Carbendazim Fungicide", "image": "static/products/carbendazim.jpg"},
    ],

    "Blight": [
        {"name": "Mancozeb Fungicide", "image": "static/products/Mancozeb.jpg"},
    ],
    "Common Rust": [
        {"name": "Propiconazole Fungicide", "image": "static/products/Propiconazole.jpeg"},
    ],
    "Gray Leaf Spot": [
        {"name": "Pyraclostrobin Fungicide", "image": "static/products/Pyraclostrobin.jpg"},
    ],
    "Brown Spot": [
            {"name": "Tricyclazole Fungicide", "image": "static/products/Tricyclazole.jpg"},
    ],
    "Leaf Smut": [
            {"name": "Copper Oxychloride Fungicide", "image": "static/products/copper.jpeg"},
    ],

    "Healthy": [
        {"name": "Organic Compost", "image": "static/products/Organic Compost.avif"},
    ]
}

def predict_image(model, img_path, classes):

    img = image.load_img(img_path, target_size=(224,224))
    img = image.img_to_array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img)
    class_index = np.argmax(pred)

    return classes[class_index]

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/predict/<crop>', methods=['GET','POST'])
def predict(crop):

    prediction = None
    img_path = None
    products = []

    if request.method == 'POST':

        file = request.files['image']

        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            img_path = filepath

            if crop == "chilli":
                prediction = predict_image(chilli_model, filepath, chilli_classes)

            elif crop == "cotton":
                prediction = predict_image(cotton_model, filepath, cotton_classes)

            elif crop == "maze":
                prediction = predict_image(maze_model, filepath, maze_classes)

            elif crop == "rice":
                prediction = predict_image(rice_model, filepath, rice_classes)

            if prediction in product_recommendations:
                products = product_recommendations[prediction]

    return render_template(
        "predict.html",
        crop=crop,
        prediction=prediction,
        img_path=img_path,
        products=products
    )


if __name__ == "__main__":
    app.run(debug=False,port=7103)
