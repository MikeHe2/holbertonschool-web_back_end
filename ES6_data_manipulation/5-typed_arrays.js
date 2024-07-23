export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const bufferData = new DataView(buffer);

  if (position > length) {
    throw new Error('Position outside range');
  }
  bufferData.setInt8(position, value);
  return bufferData;
}
