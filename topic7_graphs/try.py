


graph_elements = {"a": ["b", "c"],
                 "b": ["a", "d"],
                 "c": ["a", "d"],
                 "d": ["b", "c", "e"],
                 "e": ["d"]}


BFS(visited, graph_elements, node="a")