from flask import Flask, redirect, url_for, render_template, request, session, flash
# import requests
# import json
# from flask_sqlalchemy import SQLAlchemy
# import os
# os.system("pip install Flask-SQLAlchemy")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pythonwork'


# class Book(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String(80), nullable=False)
#     author = db.Column(db.String(80), nullable=False)
#     price = db.Column(db.Float, nullable=False)
#
#     def __str__(self):
#         return f'სათაური -  {self.title}, ავტორი - {self.author}, ფასი - {self.price}'


# with app.app_context():
#     db.create_all()
    # b1 = Book(title='Across the spiderverse', author='galaktion tabidze', price=100)
    # db.session.add(b1)
    # db.session.commit()
    # b7 = Book.query.first()
    # print(b7)
    # all = Book.query.all()
    # b6 = Book.query.get(5)
    # db.session.delete(b6)
    # db.session.commit()
    # idk = Book.query.filter_by(author='ilia chavchavadze').all()
    # for each in all:
    #     print(each)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/product', methods=['POST', 'GET'])
def product():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session['username'] = username
        return redirect(url_for('user'))

    return render_template('product.html')



@app.route('/user')
def user():

    return render_template('user.html')


@app.route('/<name>/<age>')
def userage(name, age):
    return f'Hello {name}, your age is {age}'

@app.route('/logout')
def logout():
    session.pop('username', None)
    return 'you are logged out'


# @app.route('/books', methods=['GET', 'POST'])
# def books():
#     if request.method == 'POST':
#         t = request.form['title']
#         a = request.form['author']
#         p = request.form['price']
#         if t == '' or a == '' or p == '':
#             flash('u missed few lines', 'error')
#         elif not p.isdecimal():
#             flash('price cant be words dumbass')
#         else:
#             b1 = Book(title=t, author=a, price=float(p))
#             db.session.add(b1)
#             db.session.commit()
#             flash('book was added', 'info')
#     return render_template('books.html')

# response = requests.get(f'https://api.adviceslip.com/advice')
# result = response.json()
# text = response.text
# with open('advice.json', 'w') as file:
#     file.write(response.text)
#     json.dump(result, file, indent=4)
# s = text.split(" ")
# for i in range(len(s)):
#     l = s[5::1]

if __name__ == "__main__":
    app.run(debug=True)