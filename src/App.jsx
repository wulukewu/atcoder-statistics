import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import ProblemList from './components/ProblemList';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Dashboard />} />
      <Route path="/lists/:contestType/:point/:color" element={<ProblemList />} />
    </Routes>
  );
}

export default App;
