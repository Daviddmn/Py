#<b>მოვაწყოთ გარემო ფლასკში,</b> 

#ფლასკი არის მოდული / ბიბლიოთეკა , ასერომ მოგვიწევს, `flask` ბიბლიოთეკის დაყენება
#დასაყენებლად cmd-ში ვწერთ  `pip install flask` 

#გასათვალისწინებელია რომ python 2.6 ან ამ ვერსიაზე მაღალი უნდა იყოს დაყენებული, თუგბინდა რომ გამოვიყენოთ ფლასკი, უმჯობესია `პითონ3`

#ფლასკის სერვერის ჩასართავად(დასატესტად) გვჭირდება ეს კოდი/ქვემოთ:

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
   app.run()
   
   
#დებაგ მოდის ჩასართავად ვიყენებთ ამ კოდს: `app.debug=True`  

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
   app.debug = True
   app.run()
