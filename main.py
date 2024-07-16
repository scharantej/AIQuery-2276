
# main.py

from flask import Flask, render_template, request
import json

app = Flask(__name__)

sample_data = [
    {
        "serial_number": "SN123456",
        "attachments": ["Attachment1.pdf", "Attachment2.doc"]
    },
    {
        "serial_number": "SN654321",
        "attachments": ["Attachment3.pdf", "Attachment4.xlsx"]
    },
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/query", methods=["POST"])
def query():
    serial_numbers = request.form.get("serial_numbers").split(",")
    attachment_names = request.form.get("attachment_names").split(",")

    results = []
    for data in sample_data:
        if data["serial_number"] in serial_numbers and set(attachment_names).issubset(data["attachments"]):
            results.append(data)

    return render_template("results.html", query_result=json.dumps(results))

if __name__ == "__main__":
    app.run(debug=True)
