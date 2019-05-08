function addTwoDigits(n: any): number {
    const nums = n.toString().split('');
    console.log(nums)
    let total = 0;
    return nums.reduce((a: string, b: string) => {
        return parseInt(a) + parseInt(b);
    })
}

console.log(addTwoDigits(29));
console.log(addTwoDigits(314));

// reduce is to execute for each two elements in an array,
// and return the last result. the result returned previously will be the previous value
