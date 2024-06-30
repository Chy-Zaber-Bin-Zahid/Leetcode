function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
  const mergedArray = [...nums1, ...nums2].sort((a, b) => a - b);
  if (mergedArray.length % 2 !== 0) {
    return mergedArray[Math.floor(mergedArray.length / 2)];
  } else {
    return (
      (mergedArray[Math.floor(mergedArray.length / 2) - 1] + mergedArray[Math.floor(mergedArray.length 2)]) / 2
    );
  }
}
