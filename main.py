#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask  import Flask, request , Response, jsonify
from flask import json
from Usuario import user

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hola mundo'


@app.route('/usuario' , methods=['GET'])
def Usuario():
    if request.method=='GET':
        usuario = user("jairo","castaañeda")
        
        
        data = json.dumps(usuario.serializable(), indent=1,  ensure_ascii=False)
        respuesta = Response(response=data,
                            status=200,
                            mimetype='application/json'
                            )
        return respuesta

    respuesta = Response(status=500) 
    return respuesta  



