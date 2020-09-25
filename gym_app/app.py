from flask import Flask, render_template

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(sessions_blueprint)
app.register_blueprint(bookings_blueprint)





@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)