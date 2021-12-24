from flask import Flask, render_template, url_for, request, redirect

app = Flask('__name__')

@app.route('/', methods=["GET","POST"])
def home():
    if request.method == 'POST':
        print(request.method)
        return "post returned"
    else:
        return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)
