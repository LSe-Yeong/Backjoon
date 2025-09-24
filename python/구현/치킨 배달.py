from itertools import combinations
import math

N,M = map(int,input().split())
# city = []
# chicken = []
# house = []
# lengths = []

# for _ in range(N):
#     city.append(list(map(int,input().split())))

# for r in range(N):
#     for c in range(N):
#         if(city[r][c]==1):
#             house.append([r,c])
#         elif(city[r][c]==2):
#             chicken.append([r,c])

# test_list = list(combinations(chicken,M))

# for chicken_house in test_list:
#     houseSum=0
#     for h in house:
#         min_value = 10e9
#         for c in chicken_house:
#             distance = abs(h[0]-c[0])+abs(h[1]-c[1])
#             if(distance<=min_value):
#                 min_value=distance
#         houseSum+=min_value
#     lengths.append(houseSum)

# print(min(lengths))

def calDistance(ch1,ch2):
    return abs(ch1[0]-ch2[0])+abs(ch1[1]-ch2[1])

def calCityDistance(city,ch_list):
    distance = 0
    for r in range(len(city)):
        for c in range(len(city[r])):
            if city[r][c] == 1:
                add_distance = 100000
                for ch in ch_list:
                    add_distance = min(add_distance,calDistance((r,c),ch))
                distance += add_distance
    return distance

city = []
chicken = []
result = 10e9

for _ in range(N):
    city.append(list(map(int,input().split())))

for r in range(N):
    for c in range(N):
        if city[r][c] == 2:
            chicken.append((r,c))

combi = combinations(chicken,M)
for com in combi:
    cityDistance = calCityDistance(city,com)
    result = min(result,cityDistance)

print(result)

