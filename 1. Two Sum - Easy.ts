function twoSum(nums: number[], target: number):{
  let check: string = "";
  for (let index = 0; index < nums.length; index++) {
    if (check.length !== 0) {
      break;
    }
    for (let i = 0; i < nums.length; i++) {
      if (i !== index) {
        if (nums[index] + nums[i] === target) {
          check = "found";
          return [index, i];
        }
      }
    }
  }
}
