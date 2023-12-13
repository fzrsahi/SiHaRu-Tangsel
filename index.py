from flask import Flask,redirect, request,url_for,render_template
from algorithm import input_attribute
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def get_price():
    if request.method == "POST":
        tipe_rumah = request.form["tipe_rumah"]
        jumlah_lantai = request.form["jumlah_lantai"]
        tipe_kamar = request.form["tipe_kamar"]
        tipe_kamar_mandi = request.form["tipe_kamar_mandi"]
        tipe_garasi = request.form["tipe_garasi"]
        return render_template("index.html", content=input_attribute(tipe_rumah,jumlah_lantai,tipe_kamar,tipe_kamar_mandi,tipe_garasi))
    return render_template("index.html", content=None)



if __name__ == '__main__':
    app.run(debug=True)