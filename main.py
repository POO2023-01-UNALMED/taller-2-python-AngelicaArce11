class Asiento:
    def _init_(self,color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    
    def cambiarColor(self, color):
        if (color=="rojo") or (color=="verde") or (color=="amarillo") or (color=="negro") or (color=="blanco"):
            self.color=color
    
class Motor:
    def _init__(self,numeroCilindros, tipo, registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
    
    def cambiarRegistro(self, resgistro):
        self.registro=resgistro
    
    def asignarTipo(self,tipo):
        if tipo=="electrico" or tipo=="gasolina":
            self.tipo=tipo

class Auto:
    cantidadCreados=0
    def _init_(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=list(Asiento)
        self.marca=marca
        self.motor=motor
        self.registro=registro
    
    def cantidadAsientos(self):
        cantidadAsientos=0
        for i in self.asientos:
            if type(i)==Asiento:
                cantidadAsientos+=1
        return cantidadAsientos
    
    def verificarIntegridad(self):
        if self.motor.registro==self.registro:
            for i in self.asientos:
                if type(i)==Asiento:
                    if i.registro!=self.motor.registro:
                        return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"