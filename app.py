from flask import Flask, render_template

app = Flask(__name__)


my_contacts = [
   {"name": "ran", "age": 44, "email": "ran@gmail.com", "phone": "05066332"},
   {"name": "inbal", "age": 50, "email":"inbal@gmail.com", "phone":"555555"},
   {"name": "dor", "age": 24, "email":"dor@gmail.com", "phone":"444444"},
   {"name": "danielle", "age": 20, "email":"danielle@gmail.com", "phone":"333333"},

]

@app.route("/")
def contact_list():
    return render_template('contact_list.html', contacts = my_contacts)


# @app.route("/")
# def contact_list():
#     final_html_str = ''
#     for contact in my_contacts:
#         final_html_str += f"{contact['name']} - {contact['age']}<br>"
#     return final_html_str

@app.route("/single_contact/<int:usernumber>")
def single_contact(usernumber):
   index = usernumber - 1
   if 0 <= index < len(my_contacts):
        contact = my_contacts[index]
        return f"The user is {contact['name']}. The age is {contact['age']}. The phone is {contact['phone']}."
   else:
        return "User not found.", 404
    
# @app.route("/single_contact/<int:usernunber>") 
# def single_contact(usernumber):
#    return f"user is:  {usernumber}"

@app.route("/add")
def add_contact():
   return "<p>Enter new contact name!</p>"

if __name__ == '__main__':
   app.run(debug=True, port=9000)