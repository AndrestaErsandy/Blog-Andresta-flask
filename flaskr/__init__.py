# import aplikasi flask untuk dipakai diweb kita
from flask import Flask

#mengatur nama aplikasi
app = Flask(__name__)

#mengatur URI(universal resource identifier), dan apa yang ditampilkan jika URI tersebut diakses
@app.route('/') #ketika alamat http://127.0.0.1:5000/ dipanggil maka server akan mengeksekusi fungsi hello ()
def Hello(): #function dengan nama hello
    return 'hello, world!'

    #mengatur URI ke http://127.0.0.1:5000/login, dan mengeksekusi fungsi login() jika diakses dialamat URI http://127.0.0.1:5000/login 
    @app.route("/login")
    def login():
        return 'halaman login'