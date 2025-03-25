from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

music_folder = "static/music"
trash = []

@app.route('/')
def index():
    songs = [f for f in os.listdir(music_folder) if f.endswith('.mp3')]
    current_song = songs[0] if songs else "Ninguna"
    return render_template('index.html', songs=songs, trash=trash, current=current_song)

@app.route('/delete/<song>')
def delete(song):
    if song not in trash:
        trash.append(song)
    return redirect(url_for('index'))

@app.route('/recover/<song>')
def recover(song):
    if song in trash:
        trash.remove(song)
    return redirect(url_for('index'))

@app.route('/delete_permanently/<song>')
def delete_permanently(song):
    if song in trash:
        trash.remove(song)
        file_path = os.path.join(music_folder, song)
        if os.path.exists(file_path):
            os.remove(file_path)
    return redirect(url_for('index'))

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(url_for('index'))
    
    file = request.files['file']
    position = int(request.form.get('position', 1)) - 1  # Ajustar índice
    
    if file.filename == '' or not file.filename.endswith('.mp3'):
        return redirect(url_for('index'))
    
    save_path = os.path.join(music_folder, file.filename)
    file.save(save_path)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
