from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/decide", methods=["POST"])
def give_judgement():
    annual_income = request.json.get("input-annual-income")
    if annual_income is None:
        annual_income = request.form.get("input-annual-income")
    if annual_income is not None:
        annual_income = int(annual_income)
        if annual_income > 1000000:
            return render_template("index.html", not_eligible=False)
        else:
            return render_template("index.html", not_eligible=True)


if __name__ == "__main__":
    app.run(port=3012, host='0.0.0.0')
