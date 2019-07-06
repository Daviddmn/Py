#შევქმნით დინამიურ URL-ს, ამისთვის საჭიროა <> მეტობანაკლებობა და მის შიგნით განვსაზღვროთ ცვლადი, ეს ყველაფერი კი უნდა ჩაიწეროს .route()
#-ში 
# თუ ვინმე შევა http://localhost:5000/hello/david ამ მისამართზე , საიტზე გამოისახება ის რასაც შევიყვანთ /hello/ ს შემდეგ.
from flask import Flask
app = Flask(__name__)
# როუტში ჩაწერილი ცვლადი, მიებმება ფუნქცია hello_name() ის არგუმენტს, ფუნქციაში უნდა იყოს შეტანილი არგუმენტი იგივე სახელით რაც როუტი.
@app.route('/hello/<name>')
def hello_name(name):
   return('gamarjoba : {}'.format(name))

if __name__ == '__main__':
   app.run(debug = True)
