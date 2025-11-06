from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'secret🤫'


# ---------- HOME PAGE ----------
@app.route('/')
def dashboard():
    return render_template('dashboard.html')


# ---------- LOGIN ----------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == "admin" and password == "1234":
            session['user'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')


# ---------- LOGOUT ----------
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out successfully.', 'info')
    return redirect(url_for('home'))


# ---------- DASHBOARD ----------
@app.route('/home')
def home():
    return render_template('index.html')


# ---------- OTHER PAGES ----------
@app.route('/demand_forecast')
def demand_forecast():
    return render_template('dashboard.html')

@app.route('/manage_inventory')
def manage_inventory():
    return "<h2>Manage Inventory Page</h2>"


@app.route('/community_forum')
def community_forum():
    return "<h2>Community Forum Page</h2>"


@app.route('/procurement_chatbot')
def procurement_chatbot():
    return "<h2>Procurement Chatbot Page</h2>"


@app.route('/settings')
def settings():
    return "<h2>Settings Page</h2>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
