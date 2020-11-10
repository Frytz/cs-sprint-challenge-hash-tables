#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    #define route length and location
    route = [None] * length
    tickets_dict = {}
    #loop through tickets setting dest and next location
    for ticket in tickets:
        tickets_dict[ticket.source] = ticket.destination
    next = tickets_dict["NONE"]

    #loop over length setting the route index to the next location and the next to the next location in the list 
    for i in range(0, length):
        route[i] = next
        next = tickets_dict[next]


    return route
