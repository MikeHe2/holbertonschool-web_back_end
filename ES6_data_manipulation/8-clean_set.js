export default function cleanSet(set, startString) {
  const str = [];

  if (typeof set !== 'object' || typeof startString !== 'string' || startString.length === 0) {
    return '';
  }

  for (const i of set) {
    if (i && i.startsWith(startString)) {
      str.push(i.slice(startString.length));
    }
  }
  return str.join('-');
}
