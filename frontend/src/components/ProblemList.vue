<template>
  <div class="problem-list-container">
    <h2 v-if="problems.length > 0">Showing {{ problems.length }} Problems</h2>
    <div v-if="problems.length === 0 && showNoProblemsMessage" class="no-problems-message">
      No problems found for the selected criteria.
    </div>
    <div class="problem-cards-grid">
      <div v-for="problem in problems" :key="problem.id" class="problem-card">
        <div class="problem-card-header">
          <h3 :title="problem.title">{{ problem.title }}</h3>
        </div>
        <div class="problem-card-body">
          <p>
            <strong>Contest:</strong> 
            <a :href="`https://atcoder.jp/contests/${problem.contest_id}`" target="_blank" rel="noopener noreferrer">
              {{ problem.contest_id }}
            </a>
          </p>
          <p v-if="problem.difficulty !== undefined">
            <strong>Difficulty:</strong> {{ problem.difficulty }} 
            <span v-if="problem.color" :class="['difficulty-indicator', problem.color.toLowerCase()]">
              ({{ problem.color }})
            </span>
          </p>
           <p v-else><strong>Difficulty:</strong> N/A</p>
        </div>
        <div class="problem-card-footer">
          <a :href="`https://atcoder.jp/contests/${problem.contest_id}/tasks/${problem.id}`" target="_blank" rel="noopener noreferrer" class="view-problem-link">
            View Problem
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProblemList',
  props: {
    problems: {
      type: Array,
      required: true,
      default: () => []
    },
    // This prop can be used by the parent to control the initial message visibility
    showNoProblemsMessage: { 
        type: Boolean,
        default: false 
    }
  },
};
</script>

<style scoped>
.problem-list-container {
  margin-top: 20px;
}

.problem-list-container h2 {
  margin-bottom: 15px;
  text-align: center;
  font-size: 1.5em;
  color: var(--text-color);
}

.no-problems-message {
  text-align: center;
  padding: 20px;
  font-size: 1.1em;
  color: var(--text-color);
}

.problem-cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); /* Responsive grid */
  gap: 20px; /* Space between cards */
}

.problem-card {
  background-color: var(--problem-card-bg, #f9f9f9); /* Fallback background */
  border: 1px solid var(--problem-card-border, #eee); /* Fallback border */
  border-radius: 8px;
  padding: 15px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.05);
  display: flex;
  flex-direction: column;
  justify-content: space-between; /* Distributes space between header, body, footer */
  transition: transform 0.2s ease-in-out;
}

.problem-card:hover {
    transform: translateY(-5px); /* Slight lift effect on hover */
}

.problem-card-header h3 {
  margin-top: 0;
  margin-bottom: 10px;
  font-size: 1.15em;
  color: var(--text-color);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis; /* Adds ellipsis for long titles */
}

.problem-card-body p {
  margin: 8px 0;
  font-size: 0.9em;
  color: var(--text-color);
}

.problem-card-body strong {
  font-weight: 600;
}

.difficulty-indicator {
  padding: 2px 5px;
  border-radius: 4px;
  font-weight: bold;
  text-transform: capitalize;
}

/* Difficulty color classes from main.css should apply here if problem.color is set */
/* Example of how they might be reinforced or defined if not globally available */
.grey { background-color: #808080; color: white; }
.brown { background-color: #804000; color: white; }
.green { background-color: #008000; color: white; }
.cyan { background-color: #00C0C0; color: black; }
.blue { background-color: #0000FF; color: white; }
.yellow { background-color: #C0C000; color: black; }
.orange { background-color: #FF8000; color: black; }
.red { background-color: #FF0000; color: white; }
.black { background-color: #000000; color: white; }


.problem-card-footer {
  margin-top: 15px;
  text-align: right;
}

.view-problem-link {
  color: var(--link-color, #007bff); /* Fallback link color */
  text-decoration: none;
  font-weight: bold;
  padding: 8px 12px;
  border: 1px solid var(--link-color, #007bff);
  border-radius: 4px;
  transition: background-color 0.2s, color 0.2s;
}

.view-problem-link:hover {
  background-color: var(--link-color, #007bff);
  color: var(--button-text, #fff); /* Fallback button text color */
  text-decoration: none;
}
</style>
