import json
class Serializador:


    def __init__(self):
        pass

    @staticmethod
    def serializador(objeto):
        if type(objeto) is list:
            lista = []
            for x in objeto:
                lista.append(x.serializable())
            

            return json.dumps(lista, indent=1,  ensure_ascii=False)
            
        return json.dumps(objeto.serializable(), indent=1,  ensure_ascii=False)



    @staticmethod
    def convertoListDic(objetos):
        lista = []
        for l in objetos:
            lista.append(l.get().serializable())
        
        return lista
