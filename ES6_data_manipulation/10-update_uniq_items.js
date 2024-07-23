export default function updateUniqueItems(map) {
  if (map instanceof Map) {
    map.forEach((i, j) => {
      if (i === 1) {
        map.set(j, 100);
      }
    });
  } else {
    throw new Error('Cannot process');
  }
  return map;
}
