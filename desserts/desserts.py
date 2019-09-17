'''
desserts.py
Name: Emilia Huerta
Collaborators:
Date: 9/16/2019
Desscription: This program prints out recipes for desserts.
'''
def border():
    print('__________----------**********----------__________')

def Ladyfingers():
    print('Ladyfingers: ')
    print('* 6 eggs, separated')
    print('* Melted butter, for brushing pan')
    print()
#Ladyfingers()

def Mascarpone():
    print('Mascarpone Cream: ')
    print('* 6 egg yolks')
    print('* 1 cup sugar')
    print('* 1/3 cup Marsala')
    print('* 1/4 cup brandy')
    print('* 2 pounds mascarpone cheese')
    print()
#Mascarpone()

def Espresso():
    print('Espresso Syrup: ')
    print('* 1 cup espresso, hot')
    print('* 3 tablespoons brown sugar')
    print('* 1 tablespoon sugar')
    print('* 1 teaspoon lemon juice')
    print('* 1/2 cup grated bittersweet chocolate')
    print()
#Espresso()

def Tiramisu():
    border()
    print('Tiramisu (Wolfgang Puck)')
    border()
    Ladyfingers()
    Mascarpone()
    Espresso()
    border()
Tiramisu()

def ParfaitCream():
    print('ParfaitCream: ')
    print('* 2 cups melted vanilla ice cream')
    print('* 4 tablespoons orange flavored liqueur')
    print('* 1 cup raspberries')
    print()
#ParfaitCream()

def LadyfingerParfaits():
    border()
    print('Ladyfinger Parfaits')
    border()
    Ladyfingers()
    ParfaitCream()
    border()
LadyfingerParfaits()
