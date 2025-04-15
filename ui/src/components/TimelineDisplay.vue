<template>
  <div>
    <h1>Data from API</h1>
    <ul>
      {{ items }}
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      items: []
    };
  },
  created() {
    axios.get(process.env.VUE_APP_API_URL + '/data')
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the data:', error);
      });
  }
};
</script>