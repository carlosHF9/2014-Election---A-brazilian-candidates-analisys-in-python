class Node:
    def __init__(self, data):
        self.previous = None
        self.next = None
        self.data = data


    def __str__(self):
    	return str(self.previous) + str(self.next)

    def __repr__(self):
    	return str(self.previous) + str(self.next)




