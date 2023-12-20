from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base_page.html')

@app.route('/home')
def home_page():
    return render_template('base_page.html')

@app.route('/work')
def work():
    return render_template('work_experience.html')

@app.route('/research')
def research():
    return render_template('research_experience.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/patents')
def patents():
    return render_template('patents.html')

if __name__ == '__main__':
    app.run(debug=False,host=0.0.0.0)