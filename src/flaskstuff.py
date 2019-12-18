from flask import Flask, render_template

app = Flask('Edna🍕')


@app.route('/')
def hello():
    msg = 'Hello from the Twitch Stream'
    return msg


# @app.route('/home')
# def home():
#     return render_template('index.html')


@app.route('/home/<firstname>')
def render_name(firstname=None):
    result = render_template('index.html', firstname=firstname)
    return result


if __name__ == "__main__":  # name of the module or __main__
    app.run(port=8080, debug=True)
