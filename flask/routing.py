from flask import Flask

app = Flask(__name__)
#URL /hello მიბმული არის ფუნქცია hello_name() ფუნქციასთან, თუ მომხმარებელი ეწვევა http://localhost:5000/hello  ამ მისამართს,გამოისახება
#hello_name() ფუნქცია, ანუ 'Saiti Chartulia.'
@app.route('/hello')
def hello_name():
   return('Saiti Chartulia.')

if __name__ == '__main__':
   app.debug=True
   app.run()
   
#.route() ში რა URL საც გვინდა იმ უერლის ჩავწერთ. 


#ვებ-სერვერის გასაშვებად cmd ში ვწერთ python flaskname.py
