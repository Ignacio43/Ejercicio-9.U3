from manejador import ManejaAutos
from Nuevo import Vehiculonuevo
from ObjectEncoder import ObjectEncoder
import unittest

class Test(unittest.TestCase):
    def run(self):
        jsonF = ObjectEncoder()   
        manejador = ManejaAutos() 
        
        diccionario=jsonF.leerJSONArchivo('vehiculos.json')
        jsonF.decodificarDiccionario(diccionario, manejador)
       
        # Opcion 1
        
        vehiculo = Vehiculonuevo("Aguile", 4, "Blanco", 100000, "Chevrolet", "Full")
        posicion = 1
        manejador.agregaAutoPorPos(posicion, vehiculo)
        manejador.Muestra()
        
        self.assertIn(vehiculo,manejador)
        print("\n \n")
        posicion = 4
        manejador.agregaAutoPorPos(posicion, vehiculo)
        
        self.assertIn(vehiculo,manejador)
        manejador.Muestra()
        print("\n \n")
        posicion = manejador.getTope() + 1
        manejador.agregaAutoPorPos(posicion, vehiculo)
        
        self.assertIn(vehiculo,manejador)
        manejador.Muestra()
        print("\n \n")
        
        # Opcion 2
        
        manejador.agregarAuto(vehiculo)
        manejador.Muestra()
        print("\n \n")
        
        # Opcion 3
        
        posicion = 5
        vehiculo = manejador.buscaPorPos(posicion)
        print(vehiculo)
        manejador.MuestraPorPos(posicion)
        
        self.assertEqual(vehiculo.getClass(), manejador.MuestraPorPos(posicion))

        print("\n \n")
        
        # Opcion 4
        
        vehiculo = manejador.BuscaPorPatente("lala", 1000)
        self.assertEqual(vehiculo.importe(),245)
