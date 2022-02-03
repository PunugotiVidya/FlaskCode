from flask import *


app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('base.html', name='vidya')


def homepage():
    return render_template('login.html')


app.add_url_rule('/vidya', 'vidya', homepage)


@app.route('/main/<about>')
def about(about):
    if about == 'vidya':
        return redirect(url_for('home'))


@app.route('/login', methods=['get'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    if username == 'vidyasagar':
        return redirect('home')


if __name__ == '__main__':
    app.run(debug=True)
