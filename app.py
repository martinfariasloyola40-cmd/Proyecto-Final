open("app.py","w").write(r'''
from flask import Flask, request, render_template
import os, time
from PIL import Image
import numpy as np
from superres.core import *
from superres.gd import GradientDescentSR
import matplotlib.pyplot as plt

app=Flask(__name__)

@app.route('/')
def index(): return render_template("index.html")

@app.route('/superresolution', methods=['POST'])
def sr():
    f=request.files['image']
    name=f"lr_{int(time.time())}.png"
    path="static/results/"+name
    f.save(path)

    LR = img_to_gray_array(Image.open(path))

    s = int(request.form['s'])
    lam=float(request.form['lam'])
    tau=float(request.form['tau'])
    iters=int(request.form['iters'])
    delta=float(request.form['delta'])
    reg_type=request.form['reg']
    sigma=float(request.form['sigma'])

    HR=np.repeat(np.repeat(LR,s,axis=0),s,axis=1)

    A=DegradationOperator(s, gaussian_kernel(9,sigma))
    reg = RegL2() if reg_type=="l2" else RegHuber(delta)

    gd=GradientDescentSR(A,reg,lam,tau,iters)
    x,costs=gd.run(HR,LR)

    out=f"hr_{int(time.time())}.png"
    save_img("static/results/"+out,x)

    plt.figure()
    plt.plot(costs)
    plt.savefig("static/results/cost.png")
    plt.close()

    return render_template("result.html",
                           lr_url="/static/results/"+name,
                           hr_url="/static/results/"+out,
                           cost_url="/static/results/cost.png",
                           params=str(request.form))

if __name__=="__main__":
    app.run()
''')
