class Graph {
	constructor() {
		this.adjacencyList = {};
	}

	addVertex(vertex) {
		if (!(vertex in this.adjacencyList)) {
			this.adjacencyList[vertex] = [];
		}
		return this.adjacencyList;
	}

	addEdge(vertex1, vertex2) {
		if (!(vertex1 in this.adjacencyList) || !(vertex2 in this.adjacencyList)) {
			throw new Error("Key error with vertices");
		}

		this.adjacencyList[vertex1].push(vertex2);
		this.adjacencyList[vertex2].push(vertex1);
		return this.adjacencyList;
	}

	removeEdge(vertex1, vertex2) {
		if (!(vertex1 in this.adjacencyList) || !(vertex2 in this.adjacencyList)) {
			throw new Error("Key error with vertices");
		}

		this.adjacencyList[vertex1] = this.adjacencyList[vertex1].filter(
			(item) => item !== vertex2
		);
		this.adjacencyList[vertex2] = this.adjacencyList[vertex2].filter(
			(item) => item !== vertex1
		);

		return this.adjacencyList;
	}

	removeVertex(vertex) {
		if (!(vertex in this.adjacencyList)) {
			throw new Error("Key error with vertex");
		}

		delete this.adjacencyList[vertex];
		return this.adjacencyList;
	}

	depthFirstTraversalRecursive(startVertex) {
		let visited = {};
		let result = [];

		const dfs = (vertex) => {
			if (vertex in visited) {
				return;
			}

			visited[vertex] = true;
			result.push(vertex);

			for (let neighbor of this.adjacencyList[vertex]) {
				if (!(neighbor in visited)) {
					dfs(neighbor);
				}
			}
		};

		dfs(startVertex);
		return result;
	}
}
