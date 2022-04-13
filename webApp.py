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
        <div class="form-check">
        <input class="form-check-input" type="radio" name="file" id="exampleRadios1" value="file1.txt" checked>
        <label class="form-check-label" for="exampleRadios1">
            File 1
        </label>
        </div>
        <div class="form-check">
        <input class="form-check-input" type="radio" name="file" id="exampleRadios2" value="file2.txt">
        <label class="form-check-label" for="exampleRadios2">
            File 2
        </label>
        </div>
        <div class="form-check">
        <input class="form-check-input" type="radio" name="file" id="exampleRadios2" value="file3.txt">
        <label class="form-check-label" for="exampleRadios2">
            File 3
        </label>
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
    filename = "C:/Users/Rohith Ram/Desktop/directory-traversal-attack/files/"+request.args.get('file')
    #print(filename)
    file = open(filename,'r')
    output = file.read()
    file.close()
    return output

if __name__=="__main__":
    app.run(debug=False)

"""
"../../../../../windows\system32\license.rtf"
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