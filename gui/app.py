
from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('terminal.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['u']
    processed_text = int(text)
    if processed_text == 1:
        return redirect("http://34.70.67.87:9870/dfshealth.html#tab-overview") #Apache hadoop
    elif processed_text == 2:
        return redirect("http://34.123.150.253:8080/") #Apache Spark
    elif processed_text == 3:
        return redirect("http://104.154.151.198:8888/login?next=%2Ftree%3F") #Jupyter Notebook
    elif processed_text == 4:
        return redirect("http://35.224.173.90:9000/sessions/new?return_to=%2F") #SonarQube and SonarScanner
    else:
        return render_template('terminal.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8990)

