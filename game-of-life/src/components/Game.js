import React, { Component } from 'react';
// change to less later
import '../style/Game.css';

const cell_size = 20;
const width = 800;
const height = 600;

class Cell extends Component {
  render() {
    const { x, y } = this.props;

    return (
      <div className="cell" style={{ left: `${cell_size * x + 1}px`, top: `${cell_size * y + 1}px`, width: `${cell_size - 1}px`, height: `${cell_size - 1}px`}} />
    )
  }
}
class Game extends Component {
  constructor() {
    super();
    this.rows = height/cell_size;
    this.cols = width/cell_size;
    this.board = this.makeEmptyBoard();
  }

  state = {
    cells: []
  }

  makeEmptyBoard() {
    let board = [];
    for (let y = 0; y < this.rows; y++) {
      board[y] = [];
      for (let x = 0; x < this.cols; x++) {
        board[y][x] = false;
      }
    }
    return board;
  }

  // Generates the cell list from the board state
  makeCells() {
    let cells = [];
    for (let y = 0; y < this.rows; y++) {
      for (let x = 0; x < this.cols; x++) {
        if (this.board[y][x]) {
          cells.push({ x, y });
        }
      }
    }
    return cells;
  }

  // Calculates the position of the board element
  getElementOffset() {
    const rect = this.boardRef.getBoundingClientRect();
    const doc = document.documentElement;

    return {
      x: (rect.left + window.pageXOffset) - doc.clientLeft,
      y: (rect.top + window.pageYOffset) - doc.clientTop,
    };
  }

  // Retrieve the click position of the board element
  handleClick = e => {
    const elemOffset = this.getElementOffset();

    const offsetX = e.clientX - elemOffset.x;
    const offsetY = e.clientY - elemOffset.y;

    const x = Math.floor(offsetX/cell_size);
    const y = Math.floor(offsetY/cell_size);

    if (x >= 0 && x <= this.cols && y >= 0 && y <= this.rows) {
      this.board[y][x] = !this.board[y][x];
    }

    this.setState({ cells: this.makeCells() });
  }
  
  render() {
    const { cells } = this.state;

    return (
      <div>
        <div className="board" style={{ width: width, height: height, backgroundSize: `${cell_size}px ${cell_size}px`}} onClick={this.handleClick} ref={e => {this.boardRef = e;}}>
          {cells.map(cell => {
            return (
            <Cell x={cell.x} y={cell.y} key={`${cell.x},${cell.y}`} />
          )})}
        </div>
      </div>
    )
  }
}

export default Game;