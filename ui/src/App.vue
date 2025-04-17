<template>
  <TimelineDisplay/>
</template>

<script>
import TimelineDisplay from './components/TimelineDisplay.vue'

export default {
  name: 'App',
  components: {
    TimelineDisplay
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #FFFFFF;
  margin-top: 60px;
}
</style>
