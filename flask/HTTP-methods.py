#HTTP მეთოდებთან და ფორმებთან სამუშობ გვჭირდება ფუნქცია request
#ძირითადად მოთხივნის გაგზავნა ვებსერვერთან ხდება GET მეთოდით მაგრამ როდესაც form ებზე ვმუშაობთ გვჭირდება POST მეთოდი
#შემოგვაქ request

from flask import Flask, redirect, url_for,request
app = Flask(__name__)
#სერვერმა რომ იმუშაოს GET სა და POST მეთოდზე ერთდროულად, ამისთვის როუტში შეგვყავს პარამეტრი methods=['GET','POST']
#ამ პარამეტრის არქონის შემთხვევაში თუ გავაგზავნიდით POST მეთოდს ამოგვიგდებდა 405 Method Not Allowed შეცდომას
@app.route('/one', methods=['GET','POST'])
def bacon():
    if request.method == 'POST':
        return "Method used: POST"
    else:
        return '<form action="/one" method="POST"><input type="submit" value="submit"/></form>'

if __name__ == '__main__':
   app.run(debug = True)




