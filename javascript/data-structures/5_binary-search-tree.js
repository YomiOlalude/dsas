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
      return this
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
}
