function adjacentElementsProduct(inputArray: number[]): number {
    let largestProduct = inputArray.length ? (inputArray.length > 1 ? inputArray[0] * inputArray[1] : (inputArray.length < 1 ? 0 : inputArray[0])) : 0;

    for (let i = 1; i < inputArray.length - 1; i++) {
        const product = inputArray[i] * inputArray[i+1];

        largestProduct = largestProduct < product ? product : largestProduct;
    }
    return largestProduct;
}

console.log(adjacentElementsProduct([3, 6, -2, -5, 7, 3]));
console.log(adjacentElementsProduct([3,5]));
// console.log(adjacentElementsProduct(0));
console.log(adjacentElementsProduct([]));