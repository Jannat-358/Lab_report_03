def is_safe(node, color, graph, colors):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def graph_coloring_util(graph, k, colors, node):
    if node == len(graph):
        return True
    for c in range(1, k + 1):
        if is_safe(node, c, graph, colors):
            colors[node] = c
            if graph_coloring_util(graph, k, colors, node + 1):
                return True
            colors[node] = 0  # Backtrack
    return False

def user_input_graph_coloring():
    try:
        print("Enter number of vertices, number of edges, and number of colors (N M K):")
        n, m, k = map(int, input().split())
        graph = [[] for _ in range(n)]
        print(f"Enter {m} edges (one per line, u v):")
        for _ in range(m):
            u, v = map(int, input().split())
            if u < 0 or v < 0 or u >= n or v >= n:
                print("Invalid edge! Vertices should be between 0 and", n - 1)
                return
            graph[u].append(v)
            graph[v].append(u)
        colors = [0] * n
        if graph_coloring_util(graph, k, colors, 0):
            print(f"Coloring Possible with {k} Colors")
            print("Color Assignment:", colors)
        else:
            print(f"Coloring Not Possible with {k} Colors")
    except ValueError:
        print("Invalid input! Please enter integers only.")

# Run the program
user_input_graph_coloring()
