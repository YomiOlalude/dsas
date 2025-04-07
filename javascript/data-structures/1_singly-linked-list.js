class Node {
	constructor(value) {
		this.value = value;
		this.next = null;
	}
}

class SLL {
	constructor() {
		this.head = null;
		this.tail = null;
		this.length = 0;
	}

	toString() {
		let values = [];
		let current = this.head;

		while (current) {
			values.push(`${current.value}`);
			current = current.next;
		}

		return values.join(" --> ");
	}

	push(value) {
		let newNode = new Node(value);

		if (!this.head) {
			this.head = newNode;
			this.tail = this.head;
			this.length++;
			return this;
		}

		this.tail.next = newNode;
		this.tail = newNode;
		this.length++;
		return this;
	}

	push2(value) {
		let newNode = new Node(value);

		if (!this.head) {
			this.head = newNode;
			this.length++;
			return this;
		}

		let current = this.head;

		while (current.next) {
			current = current.next;
		}

		current.next = newNode;
		this.length++;
		return this;
	}

	pop() {
		if (!this.head) {
			return null;
		}

		let current = this.head;
		let newTail = current;

		while (current.next) {
			newTail = current;
			current = current.next;
		}

		this.tail = newTail;
		this.tail.next = null;
		this.length--;

		if (this.length === 0) {
			this.head = null;
			this.tail = null;
		}
		return this.tail;
	}

	shift() {
		if (!this.head) {
			return null;
		}

		let currentHead = this.head;
		this.head = this.head.next;
		this.length--;

		if (this.length === 0) {
			this.head = null;
			this.tail = null;
		}
		return currentHead;
	}

	unshift(value) {
		let newNode = new Node(value);

		if (!this.head) {
			this.head = newNode;
			this.tail = this.head;
			this.length++;
			return this;
		}

		newNode.next = this.head;
		this.head = newNode;
		this.length++;
		return this;
	}

	get(index) {
		let current = this.head;
		let count = 0;

		if (index >= this.length || index < 0) {
			throw new Error("Index is out of range");
		}

		if (index === 0) {
			return this.head;
		}

		while (count != index) {
			current = current.next;
			count += 1;
		}

		return current;
	}

	set(index, value) {
		let node = this.get(index);

		if (node) {
			node.value = value;
			return true;
		}

		return false;
	}

	insert(index, value) {
		if (index > this.length || index < 0) {
			throw new Error("Index is out of range");
		}

		if (index == 0) {
			return this.unshift(value);
		}

		if (index == this.length) {
			return this.push(value);
		}

		let newNode = new Node(value);
		let currentNode = this.get(index);
		let prevNode = this.get(index - 1);

		prevNode.next = newNode;
		newNode.next = currentNode;
		this.length++;
		return this;
	}

	remove(index) {
		if (index >= this.length || index < 0) {
			throw new Error("Index is out of range");
		}

		let node = this.get(index);

		if (index === this.length - 1) {
			return this.pop(node);
		}

		if (index === 0) {
			return this.shift(node);
		}

		let nextNode = node.next;
		let prevNode = this.get(index - 1);

		prevNode.next = nextNode;
		this.length--;
		return this;
	}

	reverse() {
		let prev, nextNode;
		let current = this.head;

		while (current) {
			nextNode = current.next;
			current.next = prev;
			prev = current;
			current = nextNode;
		}

		this.tail = this.head;
		this.head = prev;
		return this;
	}
}
