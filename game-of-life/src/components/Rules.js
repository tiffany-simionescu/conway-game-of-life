import React from 'react';
import "../style/Game.css";

const Rules = () => {
  return (
    <div className="rules">
      {/* <h1>Rules:</h1> */}
      <p>1. Any live cell with fewer than two live neighbours dies, as if by underpopulation</p>
      <p>2. Any live cell with two or three live neighbours lives on to the next generation.</p>
      <p>3. Any live cell with more than three live neighbours dies, as if by overpopulation.</p>
      <p>4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.</p>
    </div>
  )
}

export default Rules;