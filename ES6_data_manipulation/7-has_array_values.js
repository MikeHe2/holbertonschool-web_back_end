export default function hasValuesFromArray(set, array) {
  const i = 0;
  for (const i of array) {
    if (set.has(i) === false) {
      return false;
    }
  }
  return true;
}
