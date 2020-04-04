from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # name = request.form['name']
            # email = request.form['email']
            # subject = request.form['subject']
            # message = request.form['message']
            write_to_file(data)
            write_to_csv(data)
            return redirect('/')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong. Try again'


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        name = data['name']
        message = data['message']
        file = database.write(f'\n{name}, {email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database:
        email = data['email']
        subject = data['subject']
        name = data['name']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='-', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])
