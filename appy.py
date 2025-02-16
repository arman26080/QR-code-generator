from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.form.get('qr_data')  # Form se QR code ka data le raha hai
    if not data:
        return "No data provided", 400

    qr = qrcode.make(data)
    img_io = BytesIO()
    qr.save(img_io, format="PNG")
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
