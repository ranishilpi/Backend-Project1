from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def home_fun():
   # return 'welcome to home'
   return render_template('index.html')

@app.route('/regex', methods=['POST'])
def reg():
    reg = request.form.get('regular_expression')
    string=request.form.get('test string')
    if reg in string:
        return render_template('match.html')
    else:
        return render_template('nomatch.html')
    
    #return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True)