from flask import Flask, render_template, url_for, request, redirect
from data import *
import time

app = Flask('__name__')


@app.route('/', methods=["GET","POST"])
def home():
    if request.method == 'POST':
        rf = request.form['barcode']
        print("postie", rf)
        writescan(rf)
        print(request.form)
        diag = "pop"
        time.sleep(2)
        return render_template('flag.html', diag=diag)
    else:
        return render_template('flag.html')


if __name__ == '__main__':
    app.run(debug=True)
