# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/add')
def addition():
  a = int(request.args['a'])
  b = int(request.args['b'])
  return str(operations.add(a, b))

@app.route('/sub')
def subtraction():
  a = int(request.args['a'])
  b = int(request.args['b'])
  return str(operations.sub(a, b))

@app.route('/mult')
def multiplication():
  a = int(request.args['a'])
  b = int(request.args['b'])
  return str(operations.mult(a, b))

@app.route('/div')
def division():
  a = int(request.args['a'])
  b = int(request.args['b'])
  return str(operations.div(a, b))

ops = {
  'add': operations.add,
  'sub': operations.sub,
  'mult':operations.mult,
  'div': operations.div,
}

@app.route('/math/<operator>')
def math(operator):
  a = int(request.args.get('a'))
  b = int(request.args.get('b'))
  return str(ops[operator](a, b))
