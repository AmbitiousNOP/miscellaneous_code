/*
Given an integer array arr and a filtering function fn, return a filtered array filteredArr.

The fn function takes one or two arguments:

    arr[i] - number from the arr
    i - index of arr[i]

filteredArr should only contain the elements from the arr for which the expression fn(arr[i], i) evaluates to a truthy value. A truthy value is a value where Boolean(value) returns true.

Please solve it without the built-in Array.filter method.
*/

const filter = function(arr, fn){
    transformed_arr = [];
    for (const n of arr){
        if (fn(n, arr.indexOf(n))){
            transformed_arr.push(n);
        };
    }
    return transformed_arr;
};

let answer = filter(arr = [0,10,20,30], fn = function greaterThan10(n) { return n > 10; });
console.log(answer);

answer = filter(arr = [1,2,3], fn = function firstIndex(n, i) { return i === 0; });
console.log(answer);

answer = filter(arr = [-2,-1,0,1,2], fn = function plusOne(n) { return n + 1 });
console.log(answer);