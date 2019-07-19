
from flask import Flask, render_template
app = Flask (__name__)

print("please enter your name")
name = ""
input(name)
@app.route('/')
def index():
        return render_template('index.html', to = name)

@app.route('/whereami')
def whereami():
        return 'Ghana!'

if __name__ == '__main__':
        app.run(debug = True, host='0.0.0.0')

