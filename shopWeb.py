from flask import Flask, session,render_template,request,redirect,url_for,g
import os, ssl
import sqlite3


app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/', methods= ['GET' , 'POST'])
def index():

    if request.method == 'POST':
        Connection = sqlite3.connect('DB_file5.db')
        c = Connection.cursor()
        Item = request.form['search']
        c.execute('SELECT name, price From shop_items WHERE name LIKE "%{}%" '.format(Item))

        all_rows = c.fetchall()

        Dic = {}

        for key in all_rows:
            Product = key[0]
            price = key[1]
            Dic[Product] = price

        return render_template('shopex.html', result = Dic)

    return render_template('shop.html')



@app.route('/login', methods= ['GET', 'POST'])
def login():
    Connection = sqlite3.connect('DB_file5.db')
    c = Connection.cursor()

    if request.method == 'POST':
        session.pop('user',None)
        User = request.form['username']

        c.execute('SELECT  password From employees WHERE name LIKE "{}"'.format(User))
        all_rp = c.fetchall()

        for key in all_rp:

            all_rpw = key[0]

            if  str(request.form['password'])  == str(all_rpw):
                session['user'] = request.form['username']

                return redirect(url_for('protectedex'))

        return render_template('indexexon.html')

    return render_template('indexex.html')


@app.route('/register', methods= ['GET', 'POST'])
def register():
    Connection = sqlite3.connect('DB_file5.db')
    c = Connection.cursor()

    if request.method == 'POST':
        c.execute('SELECT name From employees WHERE name = "{}"'.format(request.form['username']))
        all_r = c.fetchall()
        for key in all_r:
            exist = key[0]
            if str(exist) == str(request.form['username']):
                return render_template('signupex.html')

        if request.form['password'] == request.form['passwordR']:
            Connection = sqlite3.connect('DB_file5.db')
            c = Connection.cursor()
            c.execute("""INSERT INTO employees VALUES("{}", "2", "{}")""".format(request.form['username'], request.form['password']))
            Connection.commit()
            c.close()
            return redirect(url_for('login'))
        return render_template('signupex.html')
    return render_template('signup.html')

@app.route('/index/protected')
def protectedex():
    if g.user:
        return render_template('protectedex.html')

    return redirect(url_for('indexex'))

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']
@app.route('/index/getsession')
def getsession():
    if 'user' in session:
        return session['user']

    return 'cant log in'
@app.route('/index/dropp')
def dropp():
    session.pop('user', None)
    return 'dropped'

if __name__ == "__main__":

    app.run(host = '0.0.0.0', port = 80)


