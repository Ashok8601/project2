from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Model load
with open("insurance_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        age = float(request.form.get("age"))

        # DataFrame with feature name
        input_data = pd.DataFrame([[age]], columns=["age"])
        prediction = model.predict(input_data)[0]

        # Convert 1 → Yes, 0 → No
        result = "Yes" if prediction == 1 else "No"

    return render_template("home.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
