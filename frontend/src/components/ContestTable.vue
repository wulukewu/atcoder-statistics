<template>
  <div class="contest-table-wrapper">
    <h2>{{ contestType }} Statistics</h2>
    <table class="contest-table">
      <thead>
        <tr>
          <th>Difficulty</th>
          <th>Total Problems</th>
          <th>Problems Solved (AC)</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(data, color) in contestData" :key="color" @click="onCellClick(color, data)" class="clickable-row">
          <td :class="['difficulty-cell', color.toLowerCase()]" :style="getCellStyle(color.toLowerCase())">
            {{ color.charAt(0).toUpperCase() + color.slice(1) }} 
          </td>
          <td>{{ data.total }}</td>
          <td>{{ data.ac }}</td>
        </tr>
        <tr v-if="!hasData">
          <td colspan="3">No data available for this contest type.</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'ContestTable',
  props: {
    contestType: {
      type: String,
      required: true,
    },
    contestData: { // Expected format: { grey: { total: 10, ac: 5 }, brown: {...}, ... }
      type: Object,
      required: true,
    },
  },
  computed: {
    hasData() {
      return this.contestData && Object.keys(this.contestData).length > 0;
    }
  },
  methods: {
    onCellClick(color, data) {
      // Emit an event with the color and the data associated with that color
      // The parent component (HomeView) will use the color to filter problem_dict
      console.log(`Cell clicked: Color - ${color}, Data -`, data);
      this.$emit('cell-click', { color: color.toLowerCase() });
    },
    getCellStyle(color) {
      // This method is to dynamically apply styles if data-color-scheme="difficulty"
      // It ensures that the text color contrasts with the background color.
      // These are fallback colors if CSS variables are not applied correctly.
      const styles = {
        grey: { backgroundColor: '#808080', color: 'white' },
        brown: { backgroundColor: '#804000', color: 'white' },
        green: { backgroundColor: '#008000', color: 'white' },
        cyan: { backgroundColor: '#00C0C0', color: 'black' },
        blue: { backgroundColor: '#0000FF', color: 'white' },
        yellow: { backgroundColor: '#C0C000', color: 'black' },
        orange: { backgroundColor: '#FF8000', color: 'black' },
        red: { backgroundColor: '#FF0000', color: 'white' },
        black: { backgroundColor: '#000000', color: 'white' },
      };
      return styles[color] || {};
    }
  },
};
</script>

<style scoped>
.contest-table-wrapper {
  margin-bottom: 20px;
  overflow-x: auto; /* Ensures table is responsive on small screens */
}

.contest-table {
  width: 100%;
  border-collapse: collapse;
  background-color: var(--background-color); /* Uses CSS variable */
}

.contest-table th,
.contest-table td {
  border: 1px solid var(--table-border, #ddd); /* Fallback border color */
  padding: 12px 15px; /* Increased padding for better readability */
  text-align: center;
  font-size: 0.95em; /* Slightly adjusted font size */
}

.contest-table th {
  background-color: var(--table-header-bg, #f8f8f8); /* Fallback header background */
  font-weight: bold; /* Ensure headers are bold */
}

.clickable-row {
  cursor: pointer;
}

.clickable-row:hover {
  opacity: 0.8; /* Visual feedback on hover */
}

.difficulty-cell {
  font-weight: bold;
  text-transform: capitalize;
}

/* Difficulty color classes (will be applied by :class binding) */
/* These ensure that if global styles are not working, cells still have color */
.grey { background-color: #808080; color: white; }
.brown { background-color: #804000; color: white; }
.green { background-color: #008000; color: white; }
.cyan { background-color: #00C0C0; color: black; }
.blue { background-color: #0000FF; color: white; }
.yellow { background-color: #C0C000; color: black; }
.orange { background-color: #FF8000; color: black; }
.red { background-color: #FF0000; color: white; }
.black { background-color: #000000; color: white; }

/* Styles for when data-color-scheme="difficulty" is active from main.css */
[data-color-scheme="difficulty"] .difficulty-cell.grey { background-color: var(--diff-grey-bg, #808080); color: var(--diff-grey-text, white); }
/* Add similar lines for other colors if specific variables are defined in main.css for difficulty scheme */

</style>
