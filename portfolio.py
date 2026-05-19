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

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/abiomed')
def abiomed():
    return render_template('abiomed.html')

@app.route('/msd')
def msd():
    return render_template('mad_street_den.html')

@app.route('/graduate_research')
def graduate_research():
    return render_template('graduate_research.html')

@app.route('/teaching_assistant')
def teaching_assistant():
    return render_template('teaching.html')


@app.route('/seg_mask')
def seg_mask():
    return render_template('segmask_topic.html')

@app.route('/vqa')
def vqa():
    return render_template('vqa_topic.html')

@app.route('/qa')
def qa():
    return render_template('qa_topic.html')



if __name__ == '__main__':
    app.run(debug=False,host="0.0.0.0",port=5000)

