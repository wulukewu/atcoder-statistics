<template>
  <div>
    <h1>AtCoder Statistics</h1>
    <h2>Latest Contests: N/A</h2>
    <atcoder-table />
  </div>
</template>

<script>
import AtcoderTable from "./AtcoderTable.vue";

export default {
  name: "StatisticsView",
  components: {
    AtcoderTable,
  },
};
</script>

<style>
h1 {
  text-align: center;
}
</style>
