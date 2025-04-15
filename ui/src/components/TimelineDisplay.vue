<template>
  <div>
    <h1>Data from API</h1>
    <ul>
      <li v-for="item in items" :key="item._id">{{ item.name }}</li>
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
        this.items = response.data;
      })
      .catch(error => {
        console.error('There was an error fetching the data:', error);
      });
  }
};
</script>