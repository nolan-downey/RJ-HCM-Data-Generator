export const APIURL = 'http://localhost:5000'
export const toCamelCase = (string) => {
  const camelString = string
    .split(' ')
    .map((word, idx) => {
      if (idx === 0) return word.toLowerCase();
      return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();  
    })
    .join('');
  return camelString;
}