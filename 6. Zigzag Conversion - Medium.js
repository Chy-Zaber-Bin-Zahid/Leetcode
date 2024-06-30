/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function (s, numRows) {
  if (numRows === 1) {
    return s;
  }
  const matrix = [];
  let count = 0;
  let current = "forward";
  for (let i = 0; i < numRows; i++) {
    matrix.push([]);
  }
  for (let j = 0; j < s.length; j++) {
    if (count < numRows && current === "forward") {
      matrix[count].push(s[j]);
      count++;
      if (count === numRows) {
        current = "backward";
      }
    } else {
      if (count === numRows) {
        count -= 2;
        if (count === 0) {
          matrix[count].push(s[j]);
          current = "forward";
          count++;
          continue;
        }
      } else if (count !== 0) {
        count--;
      } else {
        count++;
        matrix[count].push(s[j]);
        count++;
        current = "forward";
        continue;
      }
      matrix[count].push(s[j]);
    }
  }
  return matrix.map((subArray) => subArray.join("")).join("");
  // return matrix;
};

console.log(convert("ABCDEF", 2));
