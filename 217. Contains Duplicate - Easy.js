/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  const check = [...new Set(nums)];
  if (check.length !== nums.length) {
    return true;
  }
  return false;
};
