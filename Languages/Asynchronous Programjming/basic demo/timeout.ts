async function bake() {
    const title = 'Baking cookies';
    let counter = 0;
    console.clear();
    console.group(title);

    counter++;
    console.log(`${counter} - Add ingredients`);

    counter++;
    console.log(`${counter} - Mix ingredients`);

    setTimeout(() =>{
        counter++;
        console.log(`${counter} - Bake at 325 degrees for 10 minutes`);
    }, 1000);

    counter++;
    console.log(`${counter} - Eat cookies`);
}

bake()