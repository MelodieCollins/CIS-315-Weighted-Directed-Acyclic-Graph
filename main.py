
a,b = list(map(int, input().split(" ")))

# initialize list of arrays
adj_matrix = [[] for x in range(a + 1)]

for i in range(b):
    ln = list(map(int, input().split(" ")))
    adj_matrix[ln[0]].append((ln[1],ln[2]))

# initialize number of longest paths array
num = [0 for z in range(a+1)]
# initialize distance array
distance = [-1 for y in range(a+1)]
# distance from source node to itself is 0
distance[1] = 0

# update the distance for each node to node x and how many times they show up
for x in range(a+1):
    for e in adj_matrix[x]:
        # distance of edge 0 is smaller than distance of parent node x and edge 1
        if distance[x] + e[1] > distance[e[0]]:
            distance[e[0]] = distance[x] + e[1]
            num[e[0]] = 1
        # distance of edge 0 is equal to distance of parent node x and edge 1
        elif distance[x] + e[1] == distance[e[0]]:
            # distance is equal, add to number of longest paths
            num[e[0]] += num[x]
        # distance of edge 0 not yet visited
        elif distance[e[0]] == -1:
            # distance of edge 0 set to distance of parent node x and edge 1
            distance[e[0]] = distance[x] + e[1]
            num[e[0]] = 1

# print the longest path
print("longest path: ", distance[a])
# print the number of longest paths
print("number of longest paths: ", num[a])