class Node {
	constructor(value) {
		this.value = value;
		this.next = null;
	}
}

class Stack {
	constructor() {
		this.first = null;
		this.last = null;
		this.size = 0;
	}

	toString() {
		let values = [];
		let current = this.first;

		while (current) {
			values.push(`${current.value}`);
			current = current.next;
		}

		return values.join(" --> ");
	}

	enqueue(value) {
		let newNode = new Node(value);

		if (!this.first) {
			this.first = newNode;
			this.last = this.first;
			this.size++;
			return this;
		}

		newNode.next = this.first;
		this.first = newNode;
		this.size++;
		return this;
	}

	dequeue() {
		if (!this.first) {
			return null;
		}

		let currentHead = this.first;
		this.first = this.first.next;
		this.size--;

		if (this.size === 0) {
			this.first = null;
			this.last = null;
		}
		return currentHead;
	}
}
