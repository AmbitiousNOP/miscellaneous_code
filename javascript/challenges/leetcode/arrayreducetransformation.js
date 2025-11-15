/*
Given an integer array nums, a reducer function fn, and an initial value init, return a reduced array.

A reduced array is created by applying the following operation: val = fn(init, nums[0]), val = fn(val, nums[1]), val = fn(val, nums[2]), ... until every element in the array has been processed. The final value of val is returned.

If the length of the array is 0, it should return init.

Please solve it without using the built-in Array.reduce method.

*/

let reduced = function(nums,fn,init){
    for (let i = 0; i < nums.length; i++){
        //console.log(`${init} + ${nums[i]}^2 == ${fn(init,nums[i])}`);
        init = fn(init, nums[i]);
    }
    return init;
};


let ans = reduced(nums = [1,2,3,4],
    fn = function sum(accum, curr) { return accum + curr; },
    init = 0);
console.log(ans);

ans = reduced(nums = [1,2,3,4],
    fn = function sum(accum, curr) { return accum + curr * curr; },
    init = 100);
console.log(ans);


ans = reduced(nums = [],
    fn = function sum(accum, curr) { return 0; },
    init = 25);
console.log(ans);
