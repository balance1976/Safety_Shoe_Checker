from flask import Flask, render_template, url_for, request, redirect
from data import *
app = Flask('__name__')

@app.route('/', methods=["GET","POST"])
def home():
    if request.method == 'POST':
        rf = request.form['barcode']
        print("postie", rf)
        writescan(rf)
        print(request.form)
        return render_template('base.html')
    else:
        return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)
