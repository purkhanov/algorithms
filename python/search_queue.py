from collections import deque


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = {}  # Этот используется для отслеживания уже проверенных людей

    while search_queue:
        person = search_queue.popleft()

        if searched.get(person, None):
            continue

        if person_is_seller(person):
            print(person + " is a mango seller!")
            return True
        else:
            search_queue += graph[person]
            searched[person] = True
    return False


def person_is_seller(name):
    return name[-1] == "m"


if __name__ == "__main__":
    search("you")
