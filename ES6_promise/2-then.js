export default function handleResponseFromAPI(promise) {
  /* eslint-disable no-unused-vars */
  return promise
    .then((response) => {
      console.log('Got a response from the API');
      return {
        status: 200,
        body: 'success',
      };
    })
    .catch((error) => {
      console.log('Got a response from the API');
      return new Error();
    });
}
