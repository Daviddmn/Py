# ჩვენ პითონის ფუნქციიდანვე შეგვიძლია დავწეროთ და დავაბრუნოთ HTML & CSS გვერდი, მაგრამ ეს მოუხერხებელი და ცოტა ძნელია,
# ასერომ არსებობს სხვა გზა, იმისმაგიერ რომ მთლიანი html დიდი კოდი ჩავწეროთ პითონში, არსებობს ფუნქცია render_template()

from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('hello.html')

if __name__ == '__main__':
   app.run(debug = True)


# ფლასკი შეეცდება იპოვოს HTML ფაილი თიმფლეითის ფოლდერში, იმ ფოლდერის შიგნით სადაც პითონის სკრიპტია გაშვებული,
# Application folder > flask.py > templates > index.html
