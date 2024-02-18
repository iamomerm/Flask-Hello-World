from flask import Flask, render_template

# Flask
app = Flask(__name__)


# Root
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.secret_key = '3d6f45a5fc12445dbac2f59c3b6c7cb1'
    app.run(host='0.0.0.0', port=5000)

