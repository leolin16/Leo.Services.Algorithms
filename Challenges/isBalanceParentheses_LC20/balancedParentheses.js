const isValid = s => {
    let stack = [];
    let pairsHashMap = {"(":")", "[":"]", "{":"}"};

    for (let i=0;i<s.length;i++) {
        const char = s[i];
        if (pairsHashMap[char]) { // belongs to start parenthesese
            stack.push(char)
        } else {
            const topOfStack = stack[stack.length - 1] // the top char of the stack
            char === pairsHashMap[topOfStack] ? stack.pop() : stack.push(char);
        }
    }

    return stack.length === 0;
};

module.exports = isValid;
