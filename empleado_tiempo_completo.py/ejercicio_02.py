import unittest

class Vehiculos:
    def __init__(self,marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        
    def mostrar_into(self)-> str:
        return f'Datos del vehículo \n Marca: {self.marca}\n Modelo: {self.modelo}'
    
class Automovíl(vehículo):
    def __init__(self,marca: str,modelo: str, num_partes: int):
        super(). __init__(marca,modelo)
        self.num_partes = num_partes
        
        def es_deportivo(self) -> bool:
            return(self.num.puertas ==2)              
                             
  #Prueba Unitaria                 
class TestPruebaAutomovíl(whittest,TestCase):
    def setUp(self):
        auto1 = Automovíl("Mazda", '3',4)
        auto2 = Automovíl(Ferrari , 'z',2)
    def test_auto_no_deportivo(self)
        self.assertFalse(self.auto1.es_deportivo())
    
    def test_auto_deportivo(self):
        self.assertTrue(self.auto2.es_deportivo())
        
    def test_auto_deportivo_2(self):
        self.assertEqual(self.auto2.es_deportivo())
        
    def test_auto_deportivo_3(self):
        self.assertLess(self.auto2.num_puertas,3)
        
        
if __name__ == '__main__':
    #unittest.main()
    #Prueba de la clase automovíl
    auto3 = Automovíl('Honda, Accord', 2)
    if auto3.es_deportivo():
       print (auto3.mostrar_info() + '\n (Auto deportivo)')
    else:
       print (auto3.mostar_info () + '\n (auto sedán)')