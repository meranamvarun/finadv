<template>
  <div>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>User ID</th>
          <th>Platform ID</th>
          <th>Investment Type</th>
          <th>Name</th>
          <th>Invested Time</th>
          <th>Annual Return Rate</th>
          <th>Expected XOR</th>
          <th>Volatility</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="investment in investments" :key="investment.id">
          <td>{{ investment.id }}</td>
          <td>{{ investment.user_id }}</td>
          <td>{{ investment.platform_id }}</td>
          <td>{{ investment.invest_type }}</td>
          <td>{{ investment.name }}</td>
          <td>{{ investment.invested_time }}</td>
          <td>{{ investment.annual_return_rate }}</td>
          <td>{{ investment.expected_xor }}</td>
          <td>{{ investment.volatility }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      investments: []
    };
  },
  mounted() {
    axios.get('http://localhost:8000/investments/')
      .then(response => {
        this.investments = response.data;
      })
      .catch(error => {
        console.error("There was an error fetching the investments:", error);
      });
  }
};
</script>

<style>
/* Add styles for your table here */
</style>
