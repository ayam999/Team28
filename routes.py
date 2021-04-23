from  codejana_flask import app,db
from flask import render_template,url_for,redirect,flash
from codejana_flask.forms import RigistrationForm,LoginForm
from codejana_flask.models import developer
@app.route('/')
@app.route('/developerPage')
def developerPage():
    return render_template('developer.html')

@app.route('/register',methods=['POST','GET'])
def register():
    form=RigistrationForm()
    if form.validate_on_submit():
        dev=developer(username=form.username.data,password=form.password.data,id=form.id.data,email=form.email.data,firstname=form.firstname.data,lastname=form.lastname.data)
        db.session.add(dev)
        db.session.comit
        flash(f'Account created succsessfully {form.username.data}',category='success')
        return redirect(url_for('login'))
    return render_template('register.html',titil=register,form=form)


@app.route('/login',methods=['POST','GET'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        dev=developer.query.filter_by(username=form.username.data).first()
        if form.username.data==dev.username and form.password.data==dev.password:
             flash(f'login succsessful for {form.username.data}',category='success')
             return redirect(url_for('developerPage'))
        else:
           flash(f'login unsuccsessf for {form.username.data}',category='danger')

    return render_template('login.html',title='Login',form=form)


       
if __name__ =='__main__':
    app.run(debug=True)