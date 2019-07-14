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

# # # # # # # # # # # # # #
# web templating system გამოიყენება იმისთვის რომ HTML კოდში ჩავდოთ დინამიური მონაცემთა ცვლადი(var)
# პითონის ცვლადის HTML ში გასაშვებად საჭიროა {{ }} - ორმაგი ბრეკეტი და სიგნით განვსაძღვრავთ ცვლადის სახელს.

#HTML კოდი (hello.html)
<html>
   <body>
   
      <h1>Hello {{ test }}!</h1>
      
   </body>
</html>

# Flask კოდი.
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('hello.html',test='aq ganvsazgvravt cvlads, aseve strings.')

if __name__ == '__main__':
   app.run(debug = True)

# სერვერის გაშვების შემდეგ , დიდი ფონტით დაბრუნდება წარწერა   aq ganvsazgvravt cvlads, aseve strings. 




# # # #
# {% %} - აქ გაეშვება statements-ები (for,if,else,endif...)  
#html
<html>
   <body>
      {% if marks>50 %}
         <h1> Your result is success!</h1>
      {% else %}
         <h1>Your result is fail</h1>
      {% endif %}
   </body>
</html>

#flask # # # # ## # # # # # # # # # #
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<int:score>')
def hello_name(score):
   return render_template('hello.html', marks = score)

if __name__ == '__main__':
   app.run(debug = True)
   
# თუ URL ში შეყვანილი იქნება რიცხვი 50 ზე მეტი გამოიტანს 'შედეგი წარმატებულია' თუ ნაკლებია 'შედეგი წარუმატებელი'  
# ბოლოში statement ის დასასრულებლად იწერება {% endif %}  
# {{ ბრეკეტებს შორის გამოტოვება არის რეკომენდირებული. }}



