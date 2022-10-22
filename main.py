
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


from ast import Num


def greet(name, name2):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!" + name2)


greet('anton', 'martijn')

mass = []
body = {
    'sun': 2.74,
    'jupiter': 24.9,
    'neptune': 11.2,
    'earth': 9.8,
    'uranus': 8.9,
    'venus': 8.9,
    'mars': 3.7,
    'mercury': 3.7,
    'moon': 1.6,
    'pluto': 0.6

}


def force(mass, body):

    force1 = body * mass
    return force1


l = force(2, body['earth'])
print('de zwaartekracht= ', l)




m1 = []
m2 = []
d = []


def pull(m1, m2, d):
    pull1 = 6.674*10**-11 * (m1*m2)/(d**2)
    return pull1


z = pull(800, 1500, 3)
print('de kracht in newton is ', z)
