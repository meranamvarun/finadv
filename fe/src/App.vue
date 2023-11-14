<template>
  <div id="app">
    <InvestmentsTable/>
  </div>
</template>

<script>

import InvestmentsTable from './components/InvestmentsTable.vue'
export default {
  name: 'App',
  components: {
    InvestmentsTable
  }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
