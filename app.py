from flask import Flask, render_template, request, redirect
import quandl as qd
import pandas as pd
import numpy as np
from bokeh.charts import Line,output_file, show
from bokeh.embed import components
import scipy

def plot_close(tickr):
    qd.ApiConfig.api_key = "FtpsTU3J-q2x2pa2KBqV"
    tickrfinal=''.join(('WIKI/',tickr))
    mydata=qd.get(tickrfinal,start_date="2017-5-1", end_date="2017-5-31")
    print list(mydata)
    y=mydata['Close']
    #output_notebook()
    p = Line(y, title="Closing Price/ Day in May",width=500, height=400,xlabel='Dates', ylabel='Closing Price')
    #output_file("templates\closing.html", title="Closing Price in May")
    return p

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')
app.var={}
@app.route('/index',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        #app.var['name'] = request.form['ticker']
        #f = open('Hello.txt','w')
        #f.write('Ticker: %s\n'%(app.var['name']))
        #f.close()
        tickr=request.form['ticker']
        p=plot_close(tickr)
        script, div = components (p)
        return render_template("index1.html", script=script, div=div,Ticker=tickr)


if __name__ == '__main__':
  #app.run(port=33507)
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)
