class Persona():
    def __init__(self,nombre,apellido,ci,direccion,fechaNacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci
        self.direccion = direccion
        self.fechaNacimiento = fechaNacimiento
    
    def mostrarDatos(self):
        print("Nombre:",self.nombre)
        print("Apellido:",self.apellido)
        print("Fecha de Nacimiento:",self.fechaNacimiento)
        print("CI:",self.ci)
        print("Direccion:",self.direccion)




class Usuario(Persona):
    def __init__(self,nombre,apellido,ci,direccion,fechaNacimiento,usuario,contrasenia):
        super().__init__(nombre,apellido,ci,direccion,fechaNacimiento)
        self.usuario = usuario
        self.contrasenia = contrasenia
    
    def mostrarDatos(self):
        super().mostrarDatos()
        print("Usuario:",self.usuario)
        print("Contraseña:","**************")
    def login(self,usuario, contrasenia):
        if usuario == self.usuario and contrasenia == self.contrasenia:
            return True
        else:
            return False
class Desarrollador(Usuario):
    def __init__(self,nombre,apellido,ci,direccion,fechaNacimiento,usuario,contrasenia,token):
        super().__init__(nombre,apellido,ci,direccion,fechaNacimiento,usuario,contrasenia)
        self.token = token

    def mostrarDatos(self):
        super().mostrarDatos()
        print("Token:","544454ewrwr5645646w")
    
    def banear(self,gamer):
        gamer.darDeBaja()
    def activar(self,gamer):
        gamer.darDeAlta()

class Gamer(Usuario):
    def __init__(self,nombre,apellido,ci,direccion,fechaNacimiento,usuario,contrasenia):
        super().__init__(nombre,apellido,ci,direccion,fechaNacimiento,usuario,contrasenia)
        self.activo = True
    
    def mostrarDatos(self):
       super().mostrarDatos()
       print("Activo:",self.activo)
    def darDeBaja(self):
        self.activo  = False
    def darDeAlta(self):
        self.activo = True

    def login(self,usuario,contrasenia):
        logueo = super().login(usuario,contrasenia)
        if self.activo:
            return logueo
        else:
            print("Fuiste baneado por ....... Hablar con los administradores 0800-3333-1456")
            return False
        
    

gamer = Gamer("Agustin","Lujan","12345456","Salta, Argentina Capital...","03-11-2000","agulujan41","21321231231")
desarrollador = Desarrollador("Jhon","Sejas","123132123123","Santa Cruz, Bolivia...","03-12-2003","jhonsje","asdfsdfsdf","sdfsdf4564646")
desarrollador.banear(gamer)
"""
#desarrollador login
while True:
    usuario = input("Usuario: ")
    contrasenia = input("Contrasenia:")
    if desarrollador.login(usuario,contrasenia):
        print("Bienvenido")
        desarrollador.mostrarDatos()
        break
    else:
        print("Datos no validos")
"""


while True:
    usuario = input("Usuario: ")
    contrasenia = input("Contrasenia:")
    if gamer.login(usuario,contrasenia):
        print("Bienvenido")
        gamer.mostrarDatos()
        break
    else:
        print("Datos no validos")