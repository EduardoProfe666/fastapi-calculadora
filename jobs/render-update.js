const axios = require('axios');

axios.get('https://fastapi-calculadora.onrender.com/')
 .then((response) => {
   console.log(response.data);
 })
 .catch((error) => {
   console.error(error);
 });
