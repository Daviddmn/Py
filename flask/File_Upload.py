# ფაილების ატვირთვა ფლასკის სერვერზე ხდედბა ფორმებით form, 
#პირველ რიგში ფაილის ასატვირთად, html form კოდში უნდა ჩავუმატოთ: enctype = "multipart/form-data"   და შევქმნათ ინპუტ/სუბმიტ 
#ფლასკისთვის დაგვჭირდება request.files[''] და .save

#html კოდი: 

<html>
   <body>
      <form action = "http://localhost:5000/uploader" method = "POST" 
         enctype = "multipart/form-data">
         <input type = "file" name = "file" />
         <input type = "submit"/>
      </form>
   </body>
</html>


# python კოდი:

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)
   
   # ფაილი აიტვირთება ფლასკის სერვერის ფაილში.
   

########
#ფაილის ატვირთვისას, ფაილის ზომაზე ლიმიტის დასადებად ვაკეთებთ ასე :
# if len(f.read()) < (30720):  რიცხვებით განისზღვრება ბაიტები/bytes 

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
   if request.method == 'POST':
      f =request.files['file']
      if len(f.read()) < (30720):  # თუ ფაილი ნაკლებია 30 კილობაიტზე მაშინ აიტვირთება ფაილი            
          f.save(f.filename)
          return 'uploaded'
      else:    
          return('File size too big ! (max:30Kb)') # თუ მეტია 30 კილობაიტზე გამოიტანს რომ ფაილი აღემატება ნორმას ! 

   
   
