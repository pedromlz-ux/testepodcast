from flask import Flask, request, render_template, redirect, url_for, flash, send_from_directory
import os
from werkzeug.utils import secure_filename

BASE_DIR = os.path.dirname(__file__)
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
ALLOWED_EXTENSIONS = {'mp3'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'change-me-to-a-secure-random-value'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('upload'))


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        title = request.form.get('title', '')
        description = request.form.get('description', '')
        file = request.files.get('file')

        if not file:
            flash('Nenhum arquivo enviado.')
            return redirect(request.url)

        if not allowed_file(file.filename):
            flash('Arquivo inválido — envie um .mp3')
            return redirect(request.url)

        filename = secure_filename(file.filename)
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(save_path)

        # grava meta simples ao lado do arquivo
        meta_path = save_path + '.meta.txt'
        with open(meta_path, 'w', encoding='utf-8') as f:
            f.write(f'Title: {title}\n')
            f.write(f'Description: {description}\n')
            f.write(f'Filename: {filename}\n')

        flash('Upload realizado com sucesso.')
        return render_template('upload.html', uploaded=True, filename=filename)

    return render_template('upload.html')


@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
