/**
 * @return {Function}
 */
var createHelloWorld = function () {

    return function (...args) {
        return "Hello World"
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */


// Another Solution find in Solutions
var createHelloWorld = function () {
    return () => "Hello World";
};