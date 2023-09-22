from flask import Flask, render_template, redirect, url_for, request
import psycopg2
forbidden = ['INSERT','DELETE','SELECT * FROM','DROP','TABLE']


conn = psycopg2.connect(
    host = "localhost",
    database = 'gift_cards',
    user='postgres'
    )

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
  global info
  info = []
  if request.method == 'POST':
    error = None
    username = request.form.get('username')
    password = request.form.get('password')
    if username in forbidden:
      username = None
      print('attack was detected')
      return redirect(url_for('caught'))
      
    if password in forbidden:
      password = None
      print('attack was detected')
      return redirect(url_for('caught'))
    data = get_gift(username,password)
    if data == None:
      return render_template('login.html')
    for i in data:
      info.append(i)
    return redirect(url_for('show'))
  return render_template('login.html')


@app.route('/result')
def show():
  return render_template('result.html',name = info[0], message = info[2], gift = info[3])
  
@app.route('/bruh')
def caught():
  return render_template('wtf.html')




if __name__ == "__main__":
  app.run()