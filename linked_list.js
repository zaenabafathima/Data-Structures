const readline = require('readline-sync')


Node = function(name, val) {
	this.name = name;
	this.val = val;
	this.next = null;
}

LinkedList = function() {
	this.head = null;
}




LinkedList.prototype.insert = function(node) {
	if(this.head == null) {
		this.head = node;
	}
	else {
		current = this.head;
		while(current.next !== null) {
			current = current.next;
		}
		current.next = node;
	}
	console.log('just inserted:', node.name)
}

LinkedList.prototype.traverse = function() {
	let start = this.head;
	console.log('---------- THE LIST --------');
	while(start !== null) {
		console.log(start.name)
		start = start.next;
	}
	console.log('----------------------------');
}

LinkedList.prototype.deleteFront = function() {
	if(this.head == null) {
		console.log('List Empty!')
		return;
	}
	console.log('Deleting...', this.head.name)
	this.head = this.head.next;
}

LinkedList.prototype.deleteRear = function() {
	if(this.head == null) {
		console.log('List empty!');
		return;
	}

	if(this.head.next == null) {
		console.log('Deleting head ', this.head.name)
		this.head = null;
		return;
	}

	let ptr = this.head.next;
	let prev = this.head;

	while(ptr.next !== null) {
		prev = ptr
		ptr = ptr.next;
	}
	console.log('Deleting ', ptr.name)
	prev.next = null;

}


menu = function() {
	let choice = null;
	while(1) {
		console.log('---- MENU -----');
		console.log('1. Insert')
		console.log('2. Delete from front')
		console.log('3. Delete from rear')
		console.log('4. Traverse')
		console.log('5. Exit')
		choice = readline.question('\nEnter choice:')

		if(choice == 1) {
			name = readline.question('Enter name:')
			node = new Node(name)
			myList.insert(node)
		}
		else if(choice == 2) {
			myList.deleteFront();
		}
		else if(choice == 3) {
			myList.deleteRear();
		}
		else if(choice == 4) {
			myList.traverse();
		}
		else {
			return;
		}
	}
}

myList = new LinkedList();
menu();


