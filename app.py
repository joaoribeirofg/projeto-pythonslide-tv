from flask import Flask, render_template
import os

app = Flask(__name__)

# Caminho para a pasta com as imagens
CAMINHO_IMAGENS = os.path.join('static', 'imagens')

@app.route('/')
def slideshow():
    imagens = [f'imagens/{img}' for img in os.listdir(CAMINHO_IMAGENS) if img.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff'))]
    return render_template('index.html', imagens=imagens)

if __name__ == '__main__':
    app.run(debug=True)
