import random

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

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def fisher_yates_shuffle(self, l):
        # iterate over list
        for i in range(0, len(l)):
            # choose a random index
            random_index = random.randint(i, len(l) - 1)
            # swap with current index
            l[random_index], l[i] = l[i], l[random_index]

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        
        # number for how many friendships we want
        n = num_users * avg_friendships

        # Add users
        for user in range(num_users):
            self.add_user(user)
            # starts at 1, up to and including num_users

        # to create n random friendships, 
        # you could create a list with all possible friendship combinations,
        friendship_combinations = []
        # num_users = 5
        # iterate over users
        for user in range(1, self.last_id + 1):
            # iterate over users not at this index
            for friend in range(user + 1, self.last_id + 1):
                # append each as a possible combination
                friendship_combinations.append((user,friend))
                # print(friendship_combinations)

        # shuffle the list
        self.fisher_yates_shuffle(friendship_combinations)

        # then grab the first N elements from the list, where N = total we want
        # since our add_friendship makes 2 total friends, we want to divide total by 2
        friends_to_make = friendship_combinations[:n // 2] 

        # iterate over our selected friendships we want to add
        for friendship in friends_to_make:
            # add them!
            self.add_friendship(friendship[0], friendship[1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # initiate queue
        queue = []
        # add this id
        queue.append(user_id)

        # loop 
        while queue:
            user = queue.pop(0)

            # loop over all connections to user
            print("Friendships:", self.friendships[user])
            for connection in self.friendships[user]:
                # add they're if not visited or queue
                if connection not in queue and connection not in visited:
                    queue.append(connection)
            print(queue)
            # 
            if user == user_id:
                visited[user] = [user]
                print("Visited user: ",visited)
            else:
                # this should only run once
                for conn in [x for x in self.friendships[user] if x in visited]:
                    visited[user] = visited[conn][:] # copy connection
                    visited[user].append(user) # add current node
                    print("Visited: ",visited)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print("Friendships: ",sg.friendships)
    connections = sg.get_all_social_paths(1)
    print("Collections: ", connections)
