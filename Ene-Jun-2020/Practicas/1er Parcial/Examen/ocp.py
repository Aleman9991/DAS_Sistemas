class Animal:
    def __init__(self, nombre: str):
        self.nombre = nombre
    
    def get_nombre(self) -> str:
        pass

animales = [
    Animal('león'),
    Animal('ratón')
]

def animal_sound(animales: list):
    for animal in animales:
        if animal.nombre == 'león':
            print('roar')

        elif animal.nombre == 'ratón':
            print('squeak')

animal_sound(animales)