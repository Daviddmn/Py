#HTTP მეთოდებთან და ფორმებთან სამუშობ გვჭირდება ფუნქცია request
#ძირითადად მოთხივნის გაგზავნა ვებსერვერთან ხდება GET მეთოდით მაგრამ როდესაც form ებზე ვმუშაობთ გვჭირდება POST მეთოდი
#შემოგვაქ request

from flask import Flask, redirect, url_for,request
app = Flask(__name__)
#სერვერმა რომ იმუშაოს GET სა და POST მეთოდზე ერთდროულად, ამისთვის როუტში შეგვყავს პარამეტრი methods=['GET','POST']
#ამ პარამეტრის არქონის შემთხვევაში თუ გავაგზავნიდით POST მეთოდს ამოგვიგდებდა 405 Method Not Allowed შეცდომას
@app.route('/one', methods=['GET','POST'])
def bacon():
    if request.method == 'POST':   # მოთხოვნის მეთოდი თუ იქნება POST ი დააბრუნებს ქვემოთ მოცემულ ტექსტს. 
        return "Method used: POST"
    else:
        return '<form action="/one" method="POST"><input type="submit" value="submit"/></form>'
    # თუ იქნება სხვა მოთხოვნის მეთოდი, დააბრუნებს form ის ღილაკს რომელიც გააგზავნის მოთხოვნას POST მეთოდით
if __name__ == '__main__':
   app.run(debug = True)


###################################################################################################################################

# შევქმნათ HTML form მეთოდი რომელიც სერვერს გადააწვდის მონაცემებს ცვლადებში, ამ ცვლადებს კიდე სერვერს გამოვაქვეყნებინებთ ბრაუზერში

<html>
   <body>
      <form action = "http://localhost:5000/" method = "post">
         <p>Enter Name:</p>
         <input type = "text" name = "test" >
         <p><input type = "submit" value = "submit" /></p>
      </form>
   </body>
</html>

# სერვერს დავქოქავთ.
# ჰტმლ კოდს შევინახავთ და გავუშვებთ ბრაუზერში, შევიყვანთ ტექსტს დავაწვებით ღილაკს და, შეყვანილი მონაცემები გადაეცემა ვებ-სერვერს.

from flask import Flask,request
app = Flask(__name__)

@app.route('/',methods=['GET',"POST"])
def hello_world():
    test = request.form['test']
    return test

if __name__ == '__main__':
   app.run()





