/*
Given an integer array arr and a mapping function fn, return a new array with a transformation applied to each element.

The returned array should be created such that returnedArray[i] = fn(arr[i], i).

Please solve it without the built-in Array.map method.

*/

var map = function(arr, fn) {
    let ans = [];
    for (const i of arr){
        ans.push(fn(i, arr.indexOf(i)));
    }    
    return ans;
};


let answer = map([1,2,3], fn = function plusone(n) { return n + 1; });
console.log(answer);

answer = map(arr = [1,2,3], fn = function plusI(n, i) { return n + i; });
console.log(answer);

answer = map(arr = [10,20,30], fn = function constant() { return 42; });
console.log(answer);
