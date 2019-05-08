function addBorder(picture: string[]): string[] {
    // const lengthOfWall = picture[0].length + 2;
    // let wall = '';
    const wall = '*'.repeat(picture[0].length + 2);

    // for (let i = 0; i < lengthOfWall; i++) {
    //     wall = wall.concat('*');
    // }
    picture.unshift(wall); // will shoot the wall the the front
    // picture.unshift('*'.repeat(lengthOfWall));
 
    picture.push(wall);

    for (let i = 1; i < picture.length - 1; i++) {
        picture[i] = '*'.concat(picture[i], '*');
    }
    return picture;
}

console.log(addBorder(["abc", "ded"]));