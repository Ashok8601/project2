from flask import Flask,render_template,request
import pickle
app=Flask(__name__)
with open("price_prediction.pkl",'rb') as file:
    model=pickle.load(file)
@app.route("/",methods=["GET","POST"])
def home():
    predicted_price=None
    if request.method=="POST":
        area=request.form.get("area")   
        if area: 
            area=float(area)
            y_pred=model.predict([[area]])
            predicted_price=int(y_pred[0])
    return render_template("home.html",predicted_price=predicted_price)

if __name__==("__main__"):
    app.run(debug=True)

