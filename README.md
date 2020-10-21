# Conway's Game of Life and Cellular Automata

## What is the project?

The Game of Life is a cellular automaton originally created by John Horton Conway in 1970. This game is played on a 2D grid of cells. Each cell can either be alive or dead.

## What problem does it solve?

The algorithm implements the following rules to visually showcase Conway's Game of life:

1. Any live cell with fewer than two live neighbors dies, as if by underpopulation

2. Any live cell with two or three live neighbors lives on to the next generation.

3. Any live cell with more than three live neighbors dies, as if by overpopulation.

4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction. 

## Tech used?

- React
- Material UI

## How to use?

- You can create your own cell patterns or use the pre-programmed buttons to see Conway's Game of Life in action.

- Once you have the pattern selected, click Run.

- The game keeps track of how many Generations it takes to get to its current pattern.

- If you wish for the cells and Generation to stop, click the stop button

- If you wish to start over, click the clear button.

- For more information about the game, please view the left-side panels

## Exceptional difficulties and solutions, if any.

The only difficulty I ran into was getting the Generation count to stop once the cell automaton finished.

## TODO list/wishlist. What do you want to add to it if you have more time?

- A responsive layout for smaller screen sizes.
