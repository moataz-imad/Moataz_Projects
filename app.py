from cs50 import SQL
from flask import Flask, jsonify, render_template, request
import pandas as pd
from calc import SOLVE
import math as mt

app = Flask(__name__)



@app.route("/")
def index():
    # return render_template("index.html")
    return render_template("wolfram.html")


@app.route("/search")
def search():
    q = request.args.get("q")
    if q:
        
        # shows = db.execute("SELECT * FROM shows WHERE title LIKE ? LIMIT 50", "%" + q + "%")
        shows=[q,q,q,q,q]
    else:
        shows = []
    return jsonify(shows)

@app.route('/check')
def check():
    eq=request.args.get('equation')
    a1=request.args.get('from')
    a2=request.args.get('to')
    print('equation and limits=',eq,a1,a2)
    try:
        a1,a2=float(a1),float(a2)
        if a1>a2:
            custr=[a2,a1]
        else:
            custr=[a1,a2]
    except:
        custr=[]
    print(f'custom range is {custr}, and with {len(custr)} items')
    
    x,y,sol=SOLVE(func=eq,custr=custr,acc=0.01)
    header=['x','y']
    # print(len(x),'points')
    points=[[x[i],y[i]] for i in range(len(x))]
    points.insert(0,header)
    # print('====',y)
    
    if ('x' not in eq):
        sol="Equation does not contain x.<br> Please use a formula similar to this:\nx^2+x^3-sin(x)"
    return jsonify([points,sol])
    # return render_template('login.html',points=points)