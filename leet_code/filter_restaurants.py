import operator

def filter_restaurants(restaurants, veganFriendly, maxPrice, maxDistance):
    restaurants = list(filter(lambda rest:(1 if not veganFriendly else veganFriendly == rest[2]) and rest[3] <= maxPrice and rest[4]<= maxDistance, restaurants))
    restaurants.sort(key=operator.itemgetter(1, 0), reverse=1)
    return [i[0] for i in restaurants]


# print(filter_restaurants([[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], 1, 50, 10))

# restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]
# veganFriendly = 0
# maxPrice = 50
# maxDistance = 10

restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]
veganFriendly = 0
maxPrice = 30
maxDistance = 3
print(filter_restaurants(restaurants, veganFriendly, maxPrice, maxDistance))

