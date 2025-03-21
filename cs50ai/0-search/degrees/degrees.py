import sys
from sqlconnect import connect_to_db
from frontier import Node, QueueFrontier


''' 
Solving search problem:
    Initial state - the problem at hand.
    Actions - stops of action to take from the initial state to the goal state.
    Transition model - describes how each action taken will output a certain state. A state space is a graph of intermediate states via a sequence of actions.
    Goal test - test whether the goal state is reached
    Path cost function - measures the cost of solution, can be money, time etc. 
'''

def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """
    # Node.state is person_id, Node.parent is parent_node, Node.action is the action of staring in the same movie(movie_id).
    init_state = Node(source, None, None)
    frontier = QueueFrontier()
    frontier.add(init_state)
    while True:
        if frontier.empty():
            return None
        expand_node = frontier.remove()
        neighbor_nodes = neighbors_for_person(expand_node.state)
        for node in neighbor_nodes:
            movie_id, person_id = node
            if person_id != target: 
                frontier.add(Node(person_id, expand_node, movie_id))
            else:
                path = []
                while(expand_node.parent != None):
                    path.insert(0, (expand_node.action, expand_node.state))
                    expand_node = expand_node.parent
                path.append((movie_id, person_id))
                return path
            

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    rows = connect_to_db(directory, "people")
    for row in rows:
        people[row["id"]] = {
            "name": row["name"],
            "birth": row["birth"],
            "movies": set()
        }
        if row["name"].lower() not in names:
            names[row["name"].lower()] = {row["id"]}
        else:
            names[row["name"].lower()].add(row["id"])

    # Load movies
    rows = connect_to_db(directory, "movies")
    for row in rows:
        movies[row["id"]] = {
            "title": row["title"],
            "year": row["year"],
            "stars": set()
        }

    # Load stars
    rows = connect_to_db(directory, "stars")
    for row in rows:
        try:
            people[row["person_id"]]["movies"].add(row["movie_id"])
            movies[row["movie_id"]]["stars"].add(row["person_id"])
        except KeyError:
            pass


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1]

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")

        
def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()

