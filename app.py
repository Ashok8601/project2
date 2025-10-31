from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
with open("multi_linear.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/", methods=["GET", "POST"])
def home():
    predicted_price = None
    if request.method == "POST":
        try:
            bedrooms = float(request.form["bedrooms"])
            age = float(request.form["age"])
            area = float(request.form["area"])

            # Prepare input as 2D array
            input_features = np.array([[bedrooms, age, area]])
            predicted_price = model.predict(input_features)[0]
            predicted_price = round(predicted_price, 2)
        except:
            predicted_price = "Invalid input!"
    
    return render_template("home.html", predicted_price=predicted_price)

if __name__ == "__main__":
    app.run(debug=True)
