function isPalindrome(x: number): boolean {
  const convert = x.toString().split("");
  let first = 0;
  let last = convert.length-1;
  while (first <= last) {
    if (convert[first] !== convert[last]) {
      return false;
    }
    first++;
    last--;
  }
  return true;
}
