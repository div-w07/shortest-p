# shortest-path-c25 --- Shortest Path Finder

 shortest-path-c25 is a graph-based shortest-path finder for navigating a
building. It represents locations and connections between them as a
weighted graph and uses Dijkstra's algorithm to find a minimum-weight
route between a specified start and destination.

## Project Structure

``` text
 shortest-path-c25-shortest-path-finder/
├── Dataset/
│   └── data_creation.py
├── djikstra_module/
│   └── algo.py
└── Map.json
```

-   **`Dataset/data_creation.py`** --- Defines the building's nodes and
    connections, then generates `Map.json`.
-   **`djikstra_module/algo.py`** --- Implements the shortest-path
    algorithm.
-   **`Map.json`** --- Stores the building map as a weighted adjacency
    list.

## How It Works

### 1. Mapping the Building

The building is represented as a graph:

-   **Nodes** represent locations such as rooms, blocks, junctions,
    stairs, and elevators.
-   **Edges** represent direct connections between locations.
-   **Weights** represent the estimated distance or traversal cost
    associated with an edge.

The graph includes locations across the ground, first, second, and third
floors. Each location has a unique identifier so the algorithm can
distinguish between locations and determine how they connect.

### 2. Estimating Edge Weights

Measuring every connection on-site can be time-consuming and
labor-intensive. Apostasi therefore uses practical heuristics to
estimate edge weights, providing a workable representation of the
building without requiring precise measurements for every connection.

These weights are used to compare possible routes. The route with the
lowest sum of edge weights is selected.

### 3. Modeling Stairs and Elevators

In the current implementation, stairs and elevators are modeled using
the same graph-based approach. Both are represented as nodes connecting
locations across floors, with different identifiers distinguishing
stairs from elevators.

Their connections use weights within the same graph representation, so
Dijkstra's algorithm processes them in the same way as other
connections. Elevators do not currently use a separate time-based cost
function; their traversal costs are represented by the weights assigned
to their edges.

### 4. Finding a Shortest Path

The algorithm in `djikstra_module/algo.py`:

1.  Initializes the start location with distance zero and all other
    locations with an initially unknown distance.
2.  Selects the unvisited location with the smallest known distance.
3.  Examines its connected locations and updates their distances when a
    shorter route is found.
4.  Records predecessor locations so the route can be reconstructed.
5.  Reconstructs and prints the path from the destination back toward
    the start, along with the total path weight.

The algorithm uses Dijkstra's shortest-path method to find the
minimum-total-weight route in the supplied weighted graph.

## Requirements

-   Python 3

The project uses Python's standard library for JSON file handling and
the shortest-path implementation.

## Running the Project

Run commands from the repository's root directory, because the algorithm
loads `Map.json` using a relative path.

### 1. Generate the map

``` bash
python Dataset/data_creation.py
```

This creates or updates `Map.json` using the graph data defined in the
script.

### 2. Run the shortest-path algorithm

The `djikstra` function is defined in `djikstra_module/algo.py` and
accepts the map, a start node, and an end node:

``` python
djikstra(mapp, start, end)
```

To use it, load the map from `Map.json` and call the function with valid
node identifiers from that map. The function prints the reconstructed
route and its total weight.

## Map Data Format

`Map.json` stores the graph as a weighted adjacency list. Each node maps
to its directly connected nodes and the corresponding edge weights.

Conceptually, the data has this structure:

``` json
{
  "J1": {
    "J2": 10,
    "A1": 6
  },
  "J2": {
    "J1": 10,
    "E1": 12
  }
}
```

This is an illustrative example of the format, not a literal excerpt
from the building map. Node identifiers and weights must match the data
in the project's `Map.json`.

## Notes

-   Use node identifiers that exist in `Map.json` for the start and
    destination.
-   Run the commands from the repository root so the relative path to
    `Map.json` resolves correctly.
-   The route is optimized for the sum of the supplied edge weights. The
    meaning and accuracy of the resulting route depend on how those
    weights are assigned.
