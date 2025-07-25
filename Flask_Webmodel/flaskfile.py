from flask import Flask, render_template, jsonify, request
from users import users_bp
app = Flask(__name__)


app.register_blueprint(users_bp, url_prefix='/api/users')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-method')
def run_method(msg = "Ismail"):
    # Your Python logic here
    result = {"message": f"Python method called successfully by! {msg}"}
    return jsonify(result)

@app.route('/run-method1')
def run_method1():
    # Your Python logic here
    result = {"message": "2: Python method called successfully! Ismail"}
    return jsonify(result)


@app.route('/submit', methods=['POST'])
def submit():

    user_input = request.form['user_input']
    hobby = ','.join(request.form.getlist('hobby'))
    gender = request.form['gender']
    # Server-side validation
    if not user_input or len(user_input.strip()) < 3:
        error = "Input must be at least 3 characters long."
        return render_template('index.html', error=error)

    return render_template('result.html', user_input=user_input, hobby=hobby, gender=gender)


if __name__ == '__main__':
    app.run(debug=True)


