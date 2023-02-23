import traceback
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('embed.html')

@app.route("/video")
def video():
    return render_template('video.html', video = "")

@app.route("/video", methods = ["POST"])
def video_post():
    try:
        codigo = request.form["codigo"]
        prefixo = "www.youtube.com/embed" if request.form['tipo'] == "youtube" else "player.vimeo.com/video"
        video = f'<iframe src="https://{prefixo}/{codigo}" width="600" height="400"></iframe>'
        return render_template('video.html', video = video)
    except Exception as x:
        print(traceback.format_exc())
        return ""

def main():
    app.run(host = "0.0.0.0", port = 5000)

if __name__ == "__main__":
    main()