<template>
  <div class="home-view-container">
    <div class="tabs">
      <button 
        v-for="tab in tabs" 
        :key="tab.key" 
        @click="activeTab = tab.key"
        :class="{ active: activeTab === tab.key }"
      >
        {{ tab.name }}
      </button>
    </div>

    <div v-if="loading" class="loading-message">Loading data...</div>
    <div v-if="error" class="error-message">{{ error }}</div>

    <div v-if="!loading && !error && allData" class="content-area">
      <div v-for="tab in tabs" :key="tab.key" v-show="activeTab === tab.key">
        <ContestTable 
          :contest-type="tab.name" 
          :contest-data="getChartDataForTab(tab.key)"
          @cell-click="handleCellClick" 
        />
      </div>
      
      <ProblemList v-if="selectedProblems.length > 0" :problems="selectedProblems" />
      <div v-else-if="showNoProblemsMessage" class="no-problems-message">
        Select a cell from the table to see problems.
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import ContestTable from '../components/ContestTable.vue';
import ProblemList from '../components/ProblemList.vue';

export default {
  name: 'HomeView',
  components: {
    ContestTable,
    ProblemList,
  },
  data() {
    return {
      allData: null,
      loading: true,
      error: null,
      activeTab: 'all', // Default tab
      tabs: [ // Defining tabs including 'ALL'
        { key: 'all', name: 'ALL' }, 
        // Individual contest types can be added if data structure supports it
        // For now, 'ALL' will display the aggregated chart data
      ],
      selectedProblems: [],
      showNoProblemsMessage: true, // Initially true, false when a cell is clicked
    };
  },
  async created() {
    await this.fetchData();
  },
  methods: {
    async fetchData() {
      this.loading = true;
      this.error = null;
      try {
        // Assuming backend is running on port 3000
        const response = await axios.get('http://localhost:3000/api/all_data');
        this.allData = response.data;
        console.log("Data fetched:", this.allData);
      } catch (e) {
        console.error('Error fetching data:', e);
        this.error = 'Failed to load data. Ensure the backend server is running.';
        if (e.response) {
            this.error += ` (Status: ${e.response.status})`;
        } else if (e.request) {
            this.error += ' (No response from server)';
        }
      } finally {
        this.loading = false;
      }
    },
    getChartDataForTab(tabKey) {
      // This method might need adjustment based on how `allData.chart` is structured
      // and if we introduce specific tabs like ABC, ARC, AGC later.
      // For now, it returns the main chart data for the 'ALL' tab.
      if (this.allData && this.allData.chart) {
        return this.allData.chart; 
      }
      return {};
    },
    handleCellClick({ color }) { // Assuming event payload is { color: 'grey', total: 10, ac: 5 }
      this.showNoProblemsMessage = false;
      if (!this.allData || !this.allData.problem_dict) {
        this.selectedProblems = [];
        return;
      }

      // Filter problems from problem_dict based on the clicked color
      // This assumes problem_dict contains all problems and each problem has a 'color' property
      this.selectedProblems = Object.values(this.allData.problem_dict).filter(
        problem => problem.color === color
      );
      
      if(this.selectedProblems.length === 0) {
        console.log(`No problems found for color: ${color}`);
      } else {
        console.log(`Displaying ${this.selectedProblems.length} problems for color: ${color}`);
      }
    },
  },
};
</script>

<style scoped>
.home-view-container {
  padding: 1rem;
}

.tabs {
  display: flex;
  margin-bottom: 20px;
  border-bottom: 1px solid var(--table-border, #ddd); /* Fallback color */
}

.tabs button {
  padding: 10px 20px;
  cursor: pointer;
  border: none;
  background-color: transparent;
  font-size: 1em;
  color: var(--text-color, #333); /* Fallback color */
  border-bottom: 3px solid transparent;
}

.tabs button.active {
  border-bottom-color: var(--link-color, #007bff); /* Fallback color */
  font-weight: bold;
}

.loading-message, .error-message, .no-problems-message {
  text-align: center;
  padding: 20px;
  font-size: 1.2em;
}

.error-message {
  color: red;
}

.content-area {
  margin-top: 20px;
}
</style>
