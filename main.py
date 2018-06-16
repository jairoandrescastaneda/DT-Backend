#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask  import Flask, request , Response, jsonify
from flask import json
from Usuario import user
from models import Topico ,Ceo
from  Serializer import Serializador
from google.appengine.ext import ndb
import requests, urllib


url_api = 'https://api.rss2json.com/v1/api.json?rss_url='
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hola mundo'


@app.route('/usuario' , methods=['GET'])
def Usuario():
    if request.method=='GET':
        """
           p = Persona()
        p.nombre = "jairo"
        p.apellido = "Castañeda"
        x = p.put()
        
        t = Tema()
        t.descripcion ="sector arroz temas agricola"
        t.titulo = "sector Arrocero"
        t.put()
        """
     
        """
        topico = Topico()
        topico.descripcion = "Todos temas relacionados con economia"
        topico.nombre = "Economia"
        topico.url = ['http://ufps.edu.co']
        topico.put()
        """

        """     
        topico = Topico.query(Topico.nombre.IN(["Economia"]))
        print(topico.fetch())
       
        """

        #ceo = Ceo()
        #ceo.nombre = "Andres"
        #ceo.correo = "andresbbx@gmail.com"
        #Model.get_by_id
        ceo = Ceo.query(Ceo.correo=="andresbbx@gmail.com").fetch()[0]
        
        ceo.topicos.append(Topico.query(Topico.nombre=="justicia").fetch()[0].key)
        ceo.put()
        usuarios = []
        usuario = user("jairo","castaañeda")
        usuarios.append(usuario)
        
        data = Serializador.serializador(usuarios)
        respuesta = Response(response=data,
                            status=200,
                            mimetype='application/json'
                         )
        
        return respuesta

    respuesta = Response(status=500) 
    return respuesta  





@app.route('/topico/',methods=['GET','POST'])
def topicos():

    if request.method=='GET':
        topicos = Topico.query().fetch()
        serializados = Serializador.serializador(topicos)
        respuesta = Response(response=serializados,
                                status=200,
                                 mimetype='application/json'
                                )
        
        return respuesta

    
    if request.method=='POST':
        datos = request.get_json(force=True)
        topico = Topico()
        topico.descripcion = datos['descripcion']
        topico.nombre = datos['nombre']
        topico.url = [datos['url']]
        topico.put()
        return Response(status=200)


@app.route('/informacion/',methods=['GET'])
def informacion():

    if request.method=='GET':
        lista = []
        ceo = Ceo.query(Ceo.correo=="andresbbx@gmail.com").fetch()[0]
        for t in ceo.topicos:
            
            for url in t.get().url:
                
                data = json.loads(urllib.urlopen(url_api+url).read())
                print(data)
                lista.append(data)
        serializer = json.dumps(lista, indent=1,  ensure_ascii=False)
        
        return Response(response=serializer,status=200,
                        mimetype='application/json')



@app.route('/ceo/', methods=['GET','POST'])
def ceos():
    if request.method=='GET':

        ceos = Ceo.query().fetch()
        
        serializados = Serializador.serializador(ceos)
        respuesta = Response(response=serializados,
                             status=200,
                             mimetype='application/json'
                             )
        return respuesta
    
    if request.method=='POST':
        datos =request.get_json(force=True)
       

        ceo = Ceo()
        ceo.nombre =datos['nombre']
        ceo.correo = datos['correo']
        ceo.empresa = datos['empresa']
        ceo.put()
        respuesta = Response(status=200)
        return respuesta


"""
Se esta trabajando el correo por default andresbbx@gmail.com , sin embargo cuando se tenga la session
con tokens ese correo se debe reemplazar por el correo que retorne la sesion

"""
@app.route('/ceo/topico/', methods=['GET','POST'])
def MisTopicos():
    if request.method=='GET':
        ceo = Ceo.query(Ceo.correo=="andresbbx@gmail.com").fetch()[0]
        serializer =   json.dumps(Serializador.convertoListDic(ceo.topicos), indent=1,  ensure_ascii=False)
        
        return Response(response=serializer, status=200,mimetype='application/json' )
    
    if request.method=='POST':
        datos = request.get_json(force=True)
        ceo = Ceo.query(Ceo.correo=="andresbbx@gmail.com").fetch()[0]
        topico = Topico.get_by_id(int(datos['id']))
        ceo.topicos.append(topico.key)
        ceo.put()
        return Response(status=200)





@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

