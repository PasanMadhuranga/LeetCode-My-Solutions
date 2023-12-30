/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    newArr = []
    for (let i = 0; i < arr.length; i++){
        newArr.push(fn(arr[i], i))
    }
    return newArr
};


// Find another sollution in the discussion section
var map = function(arr, fn) {
    for (let i = 0; i < arr.length; ++i) {
        arr[i] = fn(arr[i], i);
    }
    return arr;
};


var map = function(arr, fn) {
    const transformedArr = [];
    arr.forEach((element, index) => {
      transformedArr[index] = fn(element, index);
    });
    return transformedArr;
};