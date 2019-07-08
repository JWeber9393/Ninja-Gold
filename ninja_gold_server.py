from flask import Flask, render_template, redirect, request, session
import random
import math

app = Flask(__name__)
app.secret_key = "money maker"

@app.route("/")
def ninja_gold():
    if "gold" not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    if 'color' not in session:
        session['color'] = []
    return render_template('ninja_gold.html', activities = session['activities'])

@app.route("/process_money", methods=["POST"])
def process_money():
    session['location'] = request.form['loc']

    if session['location'] == "farm":
        gold = random.randint(10, 20)
    if session['location'] == "cave":
        gold = random.randint(5, 10)
    if session['location'] == "house":
        gold = random.randint(2, 5)
    if session['location'] == "casino":
        gold = random.randint(-50, 50)
    
    session['gold'] += gold

    if gold > 0:
        session['activities'].insert(0, 'You gained '+str(gold)+' gold at the '+session['location']+'. NOICE!!')
        session['color'].insert(0, 'green')
        
    else:
        session['activities'].insert(0, 'You lost '+ str(abs(gold))+' gold at the '+session['location']+'. That sucks...')
        session['color'].insert(0,'red') 

    return redirect('/')

if __name__==('__main__'):
    app.run(debug=True)