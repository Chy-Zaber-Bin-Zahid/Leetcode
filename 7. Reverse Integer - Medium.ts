function reverse(x: number): number {
  const reverse = Number(Math.abs(x).toString().split("").reverse().join(""));
  if (-Math.pow(2, 31) <= reverse && reverse >= Math.pow(2, 31) - 1) {
    return 0;
  }
  return x < 0 ? -reverse : reverse;
}
