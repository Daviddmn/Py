# ფლასკს , გააჩნია ფუნქცია abort() თავისი ვებ საიტის შეცდომის კოდებით.
# ფუნქცია პარამეტრად მიიღებს ერთერთს, ქვემოთ მოცემული კოდებიდან.

#400 − for Bad Request
#401 − for Unauthenticated
#403 − for Forbidden
#404 − for Not Found
#406 − for Not Acceptable
#415 − for Unsupported Media Type
#429 − Too Many Requests

# მაგალითი 1.
# ვებ სერვერი გამოიტანს ეკრანზე კოდს 429. 

from flask import Flask,abort
app = Flask(__name__)

@app.route('/')
def hello_world():
   return abort(429)

if __name__ == '__main__':
    app.debug=True
    app.run()

# # # # 
