function alphabeticShift(inputString: string): string {
    // const alphabet: string[] = ['a','b','c','d','e','f','g',
    //                             'h','i','j','k','l','m','n',
    //                             'o','p','q','r','s','t','u',
    //                             'v','w','x','y','z'];
// faster way is to make the array be an object(keyed value)
    const alphabet: object = {
        'a': 'b', 'b': 'c', 'c': 'd',
        'd': 'e', 'e': 'f', 'f': 'g',
        'g': 'h', 'h': 'i', 'i': 'j',
        'j': 'k', 'k': 'l', 'l': 'm',
        'm': 'n', 'n': 'o', 'o': 'p',
        'p': 'q', 'q': 'r', 'r': 's',
        's': 't', 't': 'u', 'u': 'v',
        'v': 'w', 'w': 'x', 'x': 'y',
        'y': 'z', 'z': 'a'

    };
// much faster way is ascii

    let inputShifted = inputString.split('');
    console.log(inputShifted);

    for(let i=0; i < inputShifted.length; i++) {
        let index = 0;
    // for array
        // if(inputShifted[i] !== 'z') {
        //     index = alphabet.indexOf(inputShifted[i]) + 1;
        // }
        // inputShifted[i] = alphabet[index];
    // for dictionary/object
        inputShifted[i] = alphabet[inputShifted[i]];
    }
    return inputShifted.join('');
}

console.log(alphabeticShift('crazy'));