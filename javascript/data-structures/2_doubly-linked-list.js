class Node {
	constructor(value) {
		this.value = value;
		this.next = null;
		this.prev = null;
	}
}

class DLL {
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
		return values.join(" <-> ");
	}

	push(value) {
		let newNode = new Node(value);

		if (!this.head) {
			this.head = newNode;
			this.tail = this.head;
		} else {
			this.tail.next = newNode;
			newNode.prev = this.tail;
			this.tail = newNode;
		}

		this.length++;
		return this;
	}

	pop() {
		if (!this.head) {
			return null;
		}

		let node;

		if (this.length === 1) {
			node = this.head;
			this.head = null;
			this.tail = null;
		} else {
			node = this.tail;
			this.tail = this.tail.prev;
			this.tail.next = null;
			node.prev = null;
		}

		this.length--;
		return node;
	}

	shift() {
		if (!this.head) {
			return null;
		}

		let node = this.head;

		if (this.length === 1) {
			this.head = null;
			this.tail = null;
		} else {
			this.head = this.head.next;
			this.head.prev = null;
			node.next = null;
		}

		this.length--;
		return node;
	}

	unshift(value) {
		let newNode = new Node(value);

		if (!this.head) {
			this.head = newNode;
			this.tail = this.head;
		} else {
			this.head.prev = newNode;
			newNode.next = this.head;
			this.head = newNode;
		}

		this.length++;
		return this;
	}

	get(index) {
		if (index >= this.length || index < 0) {
			throw new Error("Index is out of range");
		}

		if (index === 0) {
			return this.head;
		}

		let current, counter;
		let middle = Math.floor(this.length / 2);

		if (index <= middle) {
			current = this.head;
			counter = 0;

			while (counter !== index) {
				current = current.next;
				counter++;
			}
		} else {
			current = this.tail;
			counter = this.length - 1;

			while (counter !== index) {
				current = current.prev;
				counter--;
			}
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

		if (index === 0) {
			return this.unshift(value);
		}

		if (index === this.length) {
			return this.push(value);
		}

		let newNode = new Node(value);
		let foundNode = this.get(index);
		let prevFoundNode = foundNode.prev;

		prevFoundNode.next = newNode;
		newNode.next = foundNode;
		foundNode.prev = newNode;
		newNode.prev = prevFoundNode;
		this.length++;
		return true;
	}

	remove(index) {
		if (index >= this.length || index < 0) {
			throw new Error("Index is out of range");
		}

		if (index === 0) {
			return this.shift();
		}

		if (index === this.length - 1) {
			return this.pop();
		}

		let foundNode = this.get(index);
		let foundNodePrev = foundNode.prev;
		let foundNodeNext = foundNode.next;

		foundNodePrev.next = foundNodeNext;
		foundNodeNext.prev = foundNodePrev;
		this.length--;
		return this;
	}
}
