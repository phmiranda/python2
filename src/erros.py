from models import *
arquivo = None
try:
        arquivo = open('../import.csv','r')
        valores = arquivo.readline().split(',')
        Perfil(*valores)
except (IOError,TypeError) as erro:
        print('Deu Error %s' % erro)
finally:
        if(arquivo is not None):
                print('fechando arquivo')
                arquivo.close()