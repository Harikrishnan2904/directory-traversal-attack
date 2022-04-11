from flask import Flask, request      
app = Flask(__name__)

home_page = """
<html>
    <head>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <title> Home</title>
    </head>
    <body>
    <br />
    <form action="/file" method="GET">
      <h1>Files</h1>
      <div class="form-group">
        <label for="file1">file name</label>
        <input class="form-control" type="text" name="file" placeholder="Enter file name">
      </div>
      <button type="submit" class="btn btn-success">Open</button>
    </form>
    </body>
</html>
"""

@app.route('/')
def home():
    return home_page

@app.route('/file')
def comments():   
    filename = "Z:/sem6/security in computing/directoryTraversalAttack/files/"+request.args.get('file')
    #print(filename)
    file = open(filename,'r')
    output = file.read()
    file.close()
    return output

if __name__=="__main__":
    app.run(debug=False)

