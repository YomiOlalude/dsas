class Node {
	constructor(value) {
		this.value = value;
		this.left = null;
		this.right = null;
	}
}

class BST {
	constructor() {
		this.root = null;
	}

	insert(value) {
		let newNode = new Node(value);

		if (!this.root) {
			this.root = newNode;
			return this;
		}

		let current = this.root;

		while (true) {
			if (value === current.value) {
				return false;
			}

			if (value < current.value) {
				if (current.left) {
					current = current.left;
				} else {
					current.left = newNode;
					return this;
				}
			}

			if (value > current.value) {
				if (current.right) {
					current = current.right;
				} else {
					current.right = newNode;
					return this;
				}
			}
		}
	}

	find(value) {
		if (!this.root) {
			return null;
		}

		current = this.root;

		while (current) {
			if (value < current.value) {
				current = current.left;
			} else if (value > current.value) {
				current = current.right;
			} else {
				return true;
			}
		}
		return false;
	}

	bfs() {
		let result = [];
		let queue = [this.root];
		let current = this.root;

		while (queue.length > 0) {
			current = queue.pop();
			result.push(current.value);

			if (current.left) {
				queue.push(current.left);
			}
			if (current.right) {
				queue.push(current.right);
			}
		}

		return result;
	}

	dfs_preorder() {
		let result = [];

		function traverse(node) {
			result.push(node.value);
			if (node.left) {
				traverse(node.left);
			}
			if (node.right) {
				traverse(node.right);
			}
		}

		traverse(this.root);
		return result;
	}

	dfs_postorder() {
		let result = [];

		function traverse(node) {
			if (node.left) {
				traverse(node.left);
			}
			if (node.right) {
				traverse(node.right);
			}
			result.push(node.value);
		}

		traverse(this.root);
		return result;
	}

	dfs_inorder() {
		let result = [];

		function traverse(node) {
			if (node.left) {
				traverse(node.left);
			}
			result.push(node.value);
			if (node.right) {
				traverse(node.right);
			}
		}

		traverse(this.root);
		return result;
	}
}

let bst = new BST();

bst.insert(6);
bst.insert(5);
bst.insert(4);
bst.insert(1);
bst.insert(8);
bst.insert(9);
bst.insert(3);
bst.insert(10);

console.log(bst.bfs());
