
from flask import Flask, render_template  
app = Flask(__name__)    

# Have the /play route render a template with 3 blue boxes
@app.route('/play')         
def hello_world():
    return render_template("playground.html", num_boxes = 3)  

# Have the /play/<x> route render a template with x number of blue boxes
@app.route('/play/<int:nums>')
def num(nums):
    return render_template("playground.html", num_boxes = nums)

# Have the /play/<x>/<color> route render a template with x number of boxes the color of the provided value
@app.route('/play/<int:nums>/<string:color>')
def dif(nums, color):
    return render_template("playground.html", num_boxes = nums, color = color )
    


if __name__=="__main__":      
    app.run(debug=True)    
