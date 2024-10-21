# peliculas
Programa que lleva la cuenta de las series y películas vistas

## Enunciado
Estás creando un programa para llevar la cuenta de las series y películas que has visto en el cine, en blue ray, el la tv o en una plataforma online de esas que tanto te gustan.

1. Define una clase Show que permita crear cada una de ellas. La clase debe tener los siguientes atributos:

* titulo: Título de la serie o película
* tipo: puede tener uno de estos tres valores: 'serie' para una serie, 'film' para una película o 'doc' para un documental
* terminada: true indica que la has visto entera, false indica que la estás viendo o no la has empezado todavía
* fecha_entrada: este atributo se rellena automáticamente con la fecha del día

Puedes crear una película o serie solamente sabiendo el título y el tipo. Por defecto, se marcará como no terminada y la fecha de entrada será la del día.

2. Crea un objeto para cada elemento de la siguiente tabla y agrégalo a una lista llamada mis_pelis
    | Título       | Tipo       |
    -----------------------------
    | Star Wars    | película   |
    | Avatar 2     | película   |
    | Wormwood     | documental |
    | The wire     | serie      |


3. Marca la serie "The Wire" como terminada

4. Recorre la lista mis_pelis e imprime cada objeto en una línea por la consola. Para cada objeto has de mostrar, en este orden, el título, el tipo, si está terminada y la fecha de entrada.