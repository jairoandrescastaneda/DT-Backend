from google.appengine.ext import ndb
from Serializer import Serializador


class Topico(ndb.Expando):
    #url []
    nombre = ndb.StringProperty(repeated=False)
    descripcion = ndb.StringProperty()

    def serializable(self):
        
        return {'id':self.key.id(),'nombre':self.nombre, 'descripcion':self.descripcion, 'url':self.url}


class Ceo(ndb.Expando):
    nombre = ndb.StringProperty()
    correo = ndb.StringProperty()
    empresa = ndb.StringProperty()
    topicos = ndb.KeyProperty(kind='Topico', repeated=True)


    def serializable(self):
        
        
        return {'nombre':self.nombre,'correo':self.correo,'topico':Serializador.convertoListDic(self.topicos)}


   

