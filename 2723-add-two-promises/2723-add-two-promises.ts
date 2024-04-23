type P = Promise<number>

async function addTwoPromises(promise1: P, promise2: P): P {
    return new Promise<number>( async (resolve, _) => {
        const [num1, num2] = await Promise.all([promise1, promise2]);
        const result = num1 + num2;
        resolve(result);
    });
}

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */