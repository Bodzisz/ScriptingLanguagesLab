import random


countries = ['Uruguay', 'Russia', 'Saudi Arabia', 'Egypt', 'Spain', 'Portugal', 'Iran', 'Morocco', 'France', 'Denmark', 'Peru', 'Australia', 'Croatia', 'Argentina', 'Nigeria', 'Iceland', 'Brazil', 'Switzerland', 'Serbia', 'Costa Rica', 'Sweden', 'Mexico',
             'Korea Republic', 'Germany', 'Belgium', 'England', 'Tunisia', 'Panama', 'Colombia', 'Japan', 'Senegal', 'Poland']


def shuffle(list):
    random.shuffle(list)


def takeRandomCountryFrom(list):
    return list[random.randint(0, len(list) - 1)]


shuffle(countries)
print(countries)

A = [takeRandomCountryFrom(countries)]
B = [takeRandomCountryFrom(countries)]
C = [takeRandomCountryFrom(countries)]
D = [takeRandomCountryFrom(countries)]
E = [takeRandomCountryFrom(countries)]
F = [takeRandomCountryFrom(countries)]
G = [takeRandomCountryFrom(countries)]
H = [takeRandomCountryFrom(countries)]

print(A)
print(B)
print(C)
print(D)
print(E)
print(F)
print(G)
print(H)
