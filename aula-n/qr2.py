from flask import Flask, render_template, request
import pyqrcode  # pip install pyqrcode
import png       # pip install pypng

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('qr-code-gen.html', img = "")

@app.route("/qrcode", methods = ["POST"])
def new_qr():
    try:
        input = request.form['qr']
        code = pyqrcode.create(input)
        image_as_str = code.png_as_base64_str(scale = 5)
        html_img = f'<img src="data:image/png;base64,{image_as_str}">'
        return render_template('qr-code-gen.html', img = html_img)
    except Exception as x:
        print(x)
        return ""

def main():
    app.run(host = "0.0.0.0", port = 5000)

if __name__ == "__main__":
    main()