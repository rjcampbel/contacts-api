from flask import Flask

app = Flask(__name__)

contacts = [
   { 'id': '1', 'name' : 'Shaun', 'phone': '123-234-3456' },
   { 'id': '2', 'name' : 'Bob', 'phone': '512-234-3456' },
   { 'id': '3', 'name' : 'Sue', 'phone': '203-234-3456' },
   { 'id': '4', 'name' : 'Betty', 'phone': '612-234-3456' },
]

@app.get('/contacts')
def list_contacts():
   return contacts

@app.get('/contacts/<id>')
def read_single_contact(id):
   for contact in contacts:
      if contact['id'] == id:
         return contact

   return 'That contact does not exist'

if __name__ == '__main__':
   app.run(port=8000, debug=True)