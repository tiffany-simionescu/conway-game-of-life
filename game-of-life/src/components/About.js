import React from 'react';
import '../style/Game.css';

const About = () => {
  return (
    <div className="about">
      <p>
        The Game of Life is a cellular automaton originally 
        created by John Horton Conway in 1970. This game is played
        on a 2D grid of cells. Each cell can either be alive or dead.
        There are 4 rules that determine if a cell is alive or dead:
        To learn more about Conway's Game of Life, visit 
        <a href="https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life" target="_blank">
          Wikipedia
        </a>.
      </p>
    </div>
  )
}

export default About;