from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def success():
    return "Dojo"

@app.route('/say/<something>')
def hello(something):
    return f"Hi {something.capitalize()}"

@app.route('/repeat/<int:num>/<whatever>') 
def show_user_profile(num, whatever):
    print_repeat = ""
    for i in range(num):
        print_repeat += f"<h1>{whatever}</h1>" 
    return print_repeat 



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

