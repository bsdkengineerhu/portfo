from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
##print(__name__)
##print(app)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def page(page_name):
    return render_template(page_name)

def write_to_file(datadict):
    with open('database.txt', 'a', encoding='utf-8') as database:
        email = datadict["email"]
        subject = datadict["subject"]
        message = datadict["message"]
        
        file = database.write(f"\n {email} \n {subject} \n {message}\n ")


@app.route('/submitted', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_to_csv(data)
        return redirect('/submit_form.html')
    else:
        return 'something went wrong. Please try again!'

def write_to_csv(datadict):
    with open('database.csv', mode='a', newline='') as database2:
        email = datadict["email"]
        subject = datadict["subject"]
        message = datadict["message"]
        csv_writer = csv.writer(database2, delimiter = ',')
        csv_writer.writerow([email, subject, message])

    
    
##    error = None
##    if request.method == 'POST':
##        if valid_login(request.form['username'],
##                       request.form['password']):
##            return log_the_user_in(request.form['username','password'])
##        else:
##            error = 'Invalid username/password'

    




















##@app.route("/<username>")
##def hello_world2(username=None):
##    return render_template('index.html', name=username)
##
##@app.route("/<username>/<int:post_id>")
##def hello_world3(username=None, post_id=None):
##    return render_template('index.html', name=username, post_id=post_id)

##@app.route("/blog")
##def blog():
##    return 'These are my thought on blogs'


