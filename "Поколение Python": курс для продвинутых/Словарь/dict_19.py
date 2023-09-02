# put your python code here
whats_country, whats_cities = {}, ''

for i in range(int(input())):
    cities = input().split()
    whats_country[cities[0]] = cities[1:]

for j in range(int(input())):
    cities = input()
    for key, value in whats_country.items():
        if cities in value:
            whats_cities += key + ' '
print(*whats_cities.split(), sep='\n')