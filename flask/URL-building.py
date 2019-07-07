#პირველ რიგში გვჭირდება ორი ახალი ფუნქციის შემოტანა ესენია, redirect და url_for 
# redirect() ით ხდება ჩვენს მიერ მითითებულ რაიმე სტრინგზე გადამისამართება და url_for() ით კი ხდება ფუნქციის მეშვეობით გადამისამართება.

from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

if __name__ == '__main__':
   app.run(debug = True)
   
# hello_user() ფუნქცია მიიღებს არგუმენტს .route() დინამიური URL დან, და თუ მიღებული არგუმენტი არის 'admin' მაშინ გადაამისამართებს
# hello_admin() ფუნქციაზე და თუ არგუმენტი არის სხვა რამე მაშინ გადაამისამართებს hello_guest() ზე.   
