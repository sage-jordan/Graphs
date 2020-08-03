class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def earliest_ancestor(ancestors, starting_node):
    # initiate queue 
    queue = Queue()
    # print(ancestors)
    # initiate a dict for neighbors
    neighbors = {}

    # loop over ancestors 
    for node in ancestors:
        # if value not in neighbors
        if node[1] not in neighbors:
            # initiate a set at this value's index in neighbors
            neighbors[node[1]] = set()
        # either way, we're gonna add this connection
        neighbors[node[1]].add(node[0])

    if starting_node not in neighbors:
        return -1
    else:
        queue.enqueue(neighbors[starting_node])

    while True:
        # dequeue next 
        n = queue.dequeue()
        # grab the smaller num
        current_node = min(n)
        # if node is in neighbors
        if current_node in neighbors:
            # queue up the next neighbors
            queue.enqueue(neighbors[current_node])
        else:
            # otherwise, this is it!
            return current_node