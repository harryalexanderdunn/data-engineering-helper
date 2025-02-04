// Read more in the JS API documentation here: https://docs.dataform.co/guides/javascript/js-api

const schemaDescriptions = {
    key: `The unique key for the data`,
    year: `applicable year`,
    day: `day of the month`
 }
 
 
 const getSchemaDescriptions = (customDescriptions) => {
   return Object.assign({}, schemaDescriptions, customDescriptions);
 }
 
 module.exports = {
   getSchemaDescriptions
 };