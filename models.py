from google.appengine.ext import ndb

class uPersonaser(ndb.Model):
    nombre = ndb.StringProperty()
    apellido = ndb.StringProperty()