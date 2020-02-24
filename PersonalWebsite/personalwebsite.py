from flask import Flask, render_template

app = Flask(__name__) #instantiating Class

@app.route('/')    #each page
def home():
    return render_template('/home.html')

@app.route('/Projects/')    #each page
def projects():
    return render_template('projects.html')


if __name__ == "__main__":
    app.run(debug = True)
