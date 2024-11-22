from flask import Flask , render_template , request ,jsonify ,redirect ,url_for, flash
import  os
import json
from datetime import datetime


app = Flask(__name__)
app.secret_key = "test"  # Required for flash messages

@app.route('/')
def home():
    return render_template('index.html')

DATA_FILE = "C:/Users/Manoj/OneDrive/PixelLool/Web_page/CD/Coustomer.json"



@app.route('/Submit', methods=['POST'])
def submit_form():
    try:
        form_data = {
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "subject": request.form.get("subject"),
            "number": request.form.get("number"),
            "message": request.form.get("message"),
            "timestamp": datetime.now().isoformat() 
        }
        
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                existing_data = json.load(file)
        else:
            existing_data = {}
        
        unique_key = str(datetime.now().timestamp())
        existing_data[unique_key] = form_data
        
        with open(DATA_FILE, "w") as file:
            json.dump(existing_data, file, indent=4)
        
        flash("submitted saved successfully!", "success")
        return redirect(url_for("home"))
    except Exception as e:
        flash(f"An error occurred: {e}", "error")
        return redirect(url_for("home"))

    
    

if __name__ == '__main__':
    app.run(debug=True)
