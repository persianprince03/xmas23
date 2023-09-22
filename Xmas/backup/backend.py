from flask import Flask, render_template, redirect, url_for, request
import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    database = 'gift_cards',
    user='postgres')

cursor = conn.cursor()

def get_gift(u_name, password):
  finder = ("SELECT * FROM gifts WHERE name = '%s' AND password = '%s'")
  cursor.execute(finder%(u_name,password))
  user = cursor.fetchone()
  return user
  
app = Flask(__name__)


@app.route('/')
def defult():
  return 'hello world'
@app.route('/home',methods = ['GET', 'POST'])

def login():
  global l
  l = []
  if request.method == 'POST':
    error = None
    username = request.form.get('username')
    password = request.form.get('password')
    data = get_gift(username,password)
    for i in data:
      l.append(i)
    return redirect(url_for('show'))
  return render_template('login.html')


@app.route('/result')
def show():

  return render_template('result.html',name = l[0], info = l[2], gift = l[3])
  





if __name__ == "__main__":
  app.run()