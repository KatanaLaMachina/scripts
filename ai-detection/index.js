const axios = require("axios");
const options = {
  method: "POST",
  url: "https://api.edenai.run/v2/video/explicit_content_detection_async",
  headers: {
    Authorization: "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMzhhMTExNTEtYzFlNS00NDg5LWI3Y2MtZWIwNTE2OWZlYWU0IiwidHlwZSI6ImFwaV90b2tlbiJ9.cIhwkoNp--9-YehP4MO0jLrBG1KfIAXRwvh6Fu2ItKI",
  },
  data: {
    providers: "amazon, google",
    file_url: "https://www.youtube.com/watch?v=MTTLuuX3BqE",
  },
};
axios
  .request(options)
  .then((response) => {
    console.log(response.data);
  })
  .catch((error) => {
    console.error(error);
  });
