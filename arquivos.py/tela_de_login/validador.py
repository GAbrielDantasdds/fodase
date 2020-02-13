from firebase import Firebase
import sqlite3 as sq
#  config gerais:
# firebaseConfig = {
#     apiKey: "AIzaSyDfHAVkykrG8LYUAKUWXhZF6dj8HVaTPwc",
#     authDomain: "whatsbot123.firebaseapp.com",
#     databaseURL: "https://whatsbot123.firebaseio.com",
#     projectId: "whatsbot123",
#     storageBucket: "whatsbot123.appspot.com",
#     messagingSenderId: "53273904378",
#     appId: "1:53273904378:web:6a99f3c7fcb5f8b786b543",
#     measurementId: "G-GTGSNZ48RK"}

config = { "apiKey": "AIzaSyDfHAVkykrG8LYUAKUWXhZF6dj8HVaTPwc",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://whatsbot123.firebaseio.com",
  "storageBucket": "whatsbot123.appspot.com"
}

def fazer_login(email: str, senha: str) -> list:
    '''Tenta faze login usando o firebase'''
    firebase = Firebase(config)
    auth = firebase.auth()
    try:
        user = auth.sign_in_with_email_and_password(email, senha)
        return [user, 200]
    except:
        return [404]

def validar(user):
    conexao = sq.connect('users.db')
    cursor  = conexao.cursor()
    cursor.execute('''SELECT userID, hash FROM users WHERE userID = ? and hash = ?''',
    (user['localId'], user['registered']) )
    query = cursor.fetchall()
    if len(query) == 0:
        cursor.execute('''INSERT INTO users (userID, hash) values(?,?)''',
        (user['localId'], user['registered']))
        # print('Usuário adicionado')
        conexao.commit()
        return 'OK'
    else:
        # print('Usuário já existe no banco!')
        return 'DENIED'
