function bubbleSort(array) {
	for (let i = 0; i < array.length; i++) {
		for (let j = 0; j < array.length; j++) {
			if (array[j] > array[i]) {
				[array[i], array[j]] = [array[j], array[i]];
			}
		}
	}

	return array;
}
