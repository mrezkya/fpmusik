from flask import Flask, render_template ,request ,session, url_for, send_file
from pytube import YouTube
from io import BytesIO
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Informatika22'
@app.route("/", methods=["POST","GET"])
def download():
    if request.method == 'POST':
        session['pnni'] = request.form.get("url")
        link = YouTube(session['pnni'])
        try:
            dion = link.streams.filter(only_audio=True).first()
            hasil = dion.download()
            return send_file(hasil, as_attachment=True) 
            # os.system(f'rm {hasil}.mp4')  
        except:
            return f"{link.title} not downloaded :("
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=1)