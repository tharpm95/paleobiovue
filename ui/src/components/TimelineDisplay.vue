<template>
  <div>
    <h1>Data from API</h1>
    <ul>
      <li v-for="(item, index) in items" :key="index">{{ item }}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      items: []  // Initialize items as an empty array
    };
  },
  created() {
    console.log('Loaded TimelineDisplay component');
    axios.get(process.env.VUE_APP_API_URL + '/data')
      .then(response => {
        console.log('API data received:', response.data);
        this.items = response.data; // Assign the response data to items
      })
      .catch(error => {
        console.error('There was an error fetching the data:', error);
      });
  }
};
</script>