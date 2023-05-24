from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')

@app.route('/Explore')
def Explore():
    return render_template('Explore.html')


@app.route('/predict', methods=['POST'])
def home():
    data2 = int(request.form['b'])
    data1 = int(request.form['a'])
    data3 =int(request.form['c'])
    data4 = int(request.form['d'])
    data5 = int(request.form['e'])
    data6 = int(request.form['f'])
    data7 = int(request.form['g'])
    data8 = int(request.form['h'])
    data9 = int(request.form['i'])
    data10 = int(request.form['j'])
    data11 = int(request.form['k'])
    data12 = int(request.form['l'])
    data13 = int(request.form['m'])
    data14 = int(request.form['n'])
    data16 = int(request.form['p'])
    pred = model.predict([[data1, data2, data3, data4, data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data16]])
    print(pred)
    return render_template('after.html',data=pred[0])
    


if __name__ == "__main__":
    app.run(debug=True)















