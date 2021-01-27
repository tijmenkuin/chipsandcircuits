 # Chips and circuits
> Dit is Chip and circuits opdracht voor de vak programmeren theorie als deel van minor programmeren in de Universiteit van Amsterdam.

<img src="Chipsandcircuits2.jpg" align="right"/>


## Korte omschrijving
In deze opdracht worden chips bestudeerd. Een chip kun je voorstellen als een 3D-rooster. Een 3D-rooster bestaat uit punten, de **grid points** genaamd, en lijnstukken die deze grid points met elkaar verbinden, de **grid segments** genaamd. Van de onderste laag van het 3D-rooster kunnen sommige grid points een **gate** zijn, deze hebben elk een eigen nummer. De opdracht is om verschillende gates door middel van een pad over grid segments en langs grid points met elkaar te verbinden. Welke gates met elkaar verbonden moeten worden, wordt gegeven door een net. Een **net** is niet meer dan een tupeltje van twee gates die met elkaar verbonden moeten worden. In de opdracht hebben we voor verschillende chips verschillende lijsten met nets gekregen, zo’n lijst wordt een **netlist** genoemd. Een pad dat een net, ofwel twee gates, met elkaar verbindt, wordt een **wire** genoemd. Een wire kan gezien worden als een verzameling van op een volgende *(of naast elkaar liggende)* grid points, waarvan de eerste en de laatste grid points de te verbinden gates zijn. De bedoeling van de opdracht is om alle wires van een netlist in de chip, of 3D-rooster, te krijgen. Hier zijn echter wel wat regels aan verbonden.

### Constraints
Bij het verbinden van de nets zijn er twee situaties verboden:
Ten eerste mag een grid segment van het rooster niet meer dan één keer gebruikt worden door een wire. In het geval dat dit wel gebeurt noemen we dit een collision en is de oplossing niet geldig. 
Ten tweede is het niet toegestaan dat een wire een gate van een andere net bevat. 

### Intersection
Elke gridpoint die door meer dan een wire bewandelt wordt, wordt een intersectie genoemd. _Deze intersecties zijn toegestaan alleen, worden hier wel flinke kosten aan verbonden._

### Kosten
De totale kosten worden berekend aan de hand van de volgende formule: ```
 C = n + 300 * K .``` Hierbij is **C** de totale kosten, **n** is het totale aantal grid segments die de wires van de oplossing gebruiken en **K** is het totaal aantal intersecties die de oplossing bevat.

_Het doel van de opdracht is om zo goedkoop mogelijke oplossingen te vinden._

## Greedy Simultaneous

Het algoritme Greedy Simultaneous bouwt de wires willekeurig en gedeeltelijk op. Elke keer dat het algoritme een nieuwe stap zet *(een grid segment bewandelt)*. Het algoritme kiest willekeurig een net, waarin er tussen de uiteinden van de twee paden willekeurig een grid punt wordt gekozen. Dit grid punt is in de iteratiestap uiteindelijk het punt dat een verbinding gaat leggen met een nieuw punt. Het nieuwe punt wordt bepaald aan de hand van een eigen ontworpen heuristiek dat rekening houdt met de bewegingsmogelijkheid, intersectie mogelijkheid en de Manhattan Distance allemaal gebaseerd op een n-aantal stappen in de toekomst. 

Dit proces herhaalt zich punt voor punt tot de wires uiteindelijk opgebouwd zijn. Als er geen oplossing gevonden kan worden, dan stopt het algoritme vanzelf. Het doel van het algoritme is niet zozeer het raken van de andere gate, maar eerder het weten te verbinden van de uiteinden van de paden om zo een wire te maken.

## A*-search algoritme

Bij dit  A*-search algoritme worden net voor net de goedkoopste paden tussen twee gates neergelegd. De netlist wordt initiëel in een willekeurige volgorde gezet, om meer willekeur toe te laten. Het A*-search algoritme kiest bij gelijke waarden, onder de punten met de beste f-waarden, een willekeurig nieuw punt uit. Verder is er gebruik gemaakt van verschillende heuristieken, namelijk: **Manhattan Distance**, **Euclidische afstand** en **Ties**. 

## Hill Climber

Naast het A*-search algoritme wordt er ook gebruik gemaakt van een Hill Climber. De Hill Climber werkt als volgt: Er wordt bij elke iteratie gefocust op de x-aantal duurste wires, daarvan worden vervolgens een willekeurig y-tal wires geselecteerd. Deze y-tal wires worden uit de chip verwijderd en vervolgens aan de hand van het A*-algoritme weer teruggeplaatst. Voor dit terugplaatsen is er gebruik gemaakt van de hierboven genoemde heuristieken. Ook zijn er meerdere parameterwaarden voor x en y geprobeerd om potentieel goedkopere oplossingen te genereren. De Hill Climber is toegepast om de A*-search verworven oplossingen te verbeteren, of om zijn eigen gevonden oplossingen te verbeteren.


```python
python main.py [timer]

python main.py [chip_id] [netlist_id] [algoritme] ([hillclimber] [oude oplossing])
```