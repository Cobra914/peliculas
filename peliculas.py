class Show:
    """
    Clase que recibe el título y tipo (film, doc o serie). También si está terminada (True) sino (False)
    y la fecha de entrada (por defecto: 19/10/2024).
    Crea una lista de mis películas con todos sus atributos antes mencionados.
    Imprime la lista creada con sus atributos en orden.
    """

    def __init__(self, titulo, tipo, terminada=False, fecha_entrada="19/10/2024"):
        self.titulo = titulo
        self.tipo = tipo
        self.terminada = terminada
        self.fecha_entrada = fecha_entrada

    
    def estaTerminada(self):
        self.terminada = True

    def __str__(self):
        return f"{self.titulo} es {self.tipo}. Está {self.terminada}. La fecha de entrada es: {self.fecha_entrada}"



if __name__ == "__main__":

    star_wars = Show("Star Wars", "film")
    avatar_2 = Show("Avatar 2", "film")
    wormwood = Show("Wormwood", "doc")
    the_wire = Show("The Wire", "serie")

    mis_pelis = []

    mis_pelis.append(star_wars)
    mis_pelis.append(avatar_2)
    mis_pelis.append(wormwood)
    mis_pelis.append(the_wire)

    the_wire.estaTerminada()

    for element in mis_pelis:
        print("-"*80)
        print(element)

    

