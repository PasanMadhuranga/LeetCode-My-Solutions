/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    let cache = {}

    return function(...args) {
        const input = JSON.stringify(args)

        if (input in cache) return cache[input];

        const result = fn(...args);
        cache[input] = result;
        return result
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */