import psycopg2
import random
def password_maker():
    password = ''
    char = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            '-', '=', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 
            'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 
            'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '!', '@', '#',
            '$', '%', '^', '&', '*', '(', ')', '_', '+']
    for i in range(10):
        charecter = char[random.randint(0,49)]
        password = password + charecter
    return password
    

conn = psycopg2.connect(
    host = "localhost",
    database = 'gift_cards',
    user='postgres',
    password = 'postgres')

cursor = conn.cursor()
def add():
    print('Please enter the name of the recipant:')
    recipient = input()
    print('Enter gift discription: ')
    discription = input()
    print('Enter gift card code')
    code = input()
    print('Enter link, if non, enter N/A')
    hyperlink = input()
    password = password_maker()
    exec = "INSERT INTO gifts(name, password, giftcard_detail, gift_code) VALUES ('%s','%s','%s','%s')"
    cursor.execute(exec%(recipient,password,discription,code))
    conn.commit()
    print('username:' ,recipient)
    print('password:' ,password)
def get_pass():
    cursor.execute('SELECT * FROM gifts')
    print(cursor.fetchall())
print('MAIN MENU')
print('1) add gift')
print('2) get pass')
response = int(input())
if response == 1:
    add()
if response == 2:
    get_pass()