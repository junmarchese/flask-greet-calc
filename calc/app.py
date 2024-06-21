#  Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def perform_add():
    """Add a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)
    return str(result)
  
    
@app.route("/sub")
def perform_sub():
    """Subtract a and b parameters."""
    
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)
    return str(result)

    
@app.route("/mult")
def perform_mult():
    """Multiply a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)
    return str(result)


@app.route("/div")
def perform_div():
    """Divide a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)
    return str(result)


# # Further Study

# from flask import Flask, request
# from operations import add, sub, mult, div

# app = Flask(__name__)
operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}

@app.route("/math/<operation>")
def perform_math(operation):
    """Perform math operations based operation parameter"""

    if operation not in operations:
        return "Invalid operation", 400
    
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations[operation](a, b)
    return str(result)



