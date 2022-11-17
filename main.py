from flask import Flask, render_template, request, redirect
from forms import CourseForm

app=Flask(__name__)
app.config['SECRET_KEY']='saltsecretkey'

@app.route('/', methods=['GET', 'POST'])
def hello():
    form = CourseForm()    
    if request.method == 'POST':
        searchitem = request.form.get('search')
        print(searchitem)
        if form.validate_search(searchitem):
            return render_template('success.html',result=searchitem)
        else:
            form.search.data=""
            return render_template('index.html',form=form)
    return render_template('index.html', form=form)

@app.route('/', methods=['GET', 'POST'])
def homebutton():
    return render_template('index.html')
if __name__ == '__main__':
    app.run()