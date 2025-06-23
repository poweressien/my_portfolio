from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        print("Form submitted!")
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        print(f"Received: {name}, {email}, {subject}, {message}")
        with open('messages.txt', 'a') as f:
            f.write(f"Name: {name}, Email: {email}, Subject: {subject}, Message: {message}\n")
        return "Message received! Check messages.txt."
    return render_template('contact.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    if request.method == 'POST' and request.form.get('clear') == 'true':
        # Clear messages.txt
        with open('messages.txt', 'w') as f:
            f.write('')
        messages = []
    else:
        messages = []
        try:
            with open('messages.txt', 'r') as f:
                messages = f.readlines()
        except FileNotFoundError:
            messages = []
    return render_template('messages.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)