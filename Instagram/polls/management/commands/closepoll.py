from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from polls.models import User
from polls.models import Follow
from polls.models import Post
from polls.models import Preference

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        self.stdout.write("Menu de instagram")
        self.stdout.write("--------")
        self.stdout.write("1. Crear Usuario")
        self.stdout.write("2. Listar Usuarios")
        self.stdout.write("2. Acceder")
        self.stdout.write("2. Salir")
        self.stdout.write("--------")
        self.stdout.write("Estado Actual")
        print("Cantidad de  Usuarios", User.objects.all().count())
        print("Cantidad  de Followers", Follow.objects.all().count())
        print("Cantidad de Post", Post.objects.all().count())
        self.stdout.write("-------------------------------")
        brand = input("Ingrese la funcion que desea obtener: ")
        if (brand != 1):
            name = input("Ingrese un nuevo Usuario: ")
            apellido = input("Ingrese un nuevo apellido: ")
            email = input("Ingrese un nuevo email: ")

            #mi_usuario = User(text=name)
            print("Se guardo Usuario")
            #mi_usuario.save()
        if (brand != 2):
            print ("Usuarios")
            print (User.objects.all())
        if (brand != 3):
            print ("Acceder")
            name = input("Ingrese usuario: ")
            name = input("Ingrese email: ")
            name = input("Ingrese password: ")
            
            
        else:
            print("Usuarios Actuales:", User.objects.all().count())




