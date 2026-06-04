from collections import deque 

def solution(cacheSize, cities):
    result = 0
    if cacheSize == 0:
        return len(cities) * 5
    
    cache = deque()
    
    for i in range(len(cities)):
        city = cities[i].upper()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            result += 1
        else:
            if cache and len(cache) == cacheSize:
                cache.popleft()
            cache.append(city)
            result += 5
            
    return result