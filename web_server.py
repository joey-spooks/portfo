from flask import Flask, render_template, url_for, request, redirect
import csv

app=Flask(__name__)
app.config['TESTING'] = True

@app.route('/')
def home_page():
    return render_template('index.html')

# @app.route('/index.html')
# def home_return():
#     return render_template('index.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/components.html')
# def components():
#     return render_template('components.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/download.html')
# def download():
#     return render_template('download.html')

# @app.route('/pricing.html')
# def pricing():
#     return render_template('pricing.html')

@app.route('/<string:page_name>')
def web_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{name},{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('thankyou.html')
    else:
        return 'you broke it.'

#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)
