class Station:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
    def add_connection(self, another_station):
        if another_station not in self.neighbors:
            self.neighbors.append(another_station)
        if self not in another_station.neighbors:
            another_station.neighbors.append(self)


with open('stations.txt') as fh:
    stations = dict()
    for line in fh:
        line= line.strip()
        wordlist=line.split('-')
        for (index, word) in enumerate(wordlist):
            wordlist[index]= word.strip()
        for word in wordlist:
            if word not in stations.keys():
                stations[word] = Station(word)
        for i in range(len(wordlist)-1):
            a=wordlist[i]
            b=wordlist[i+1]
            stations[a].add_connection(stations[b])

def bfs(start, goal):
    previous = {}
    queue = []
    current = None

    previous[start]=None
    queue.append(start)
    while len(queue)!=0 and goal not in queue:
        current = queue[0]
        for neighbor in current.neighbors:
            if neighbor not in previous.keys():
                previous[neighbor] = current
                queue.append(neighbor)
        
        queue.pop(0)
        
    
    if goal in queue:
        path = []
        i = goal
        
        path.append(i)
        
        while i != start:
            path.append(previous[i])
            i = previous[i]
            
        return path
    else:
        return None
start_name = "이태원"
goal_name = "잠원"

start = stations[start_name]
goal = stations[goal_name]


path = bfs(start, goal)
for station in path:
    print(station.name)
