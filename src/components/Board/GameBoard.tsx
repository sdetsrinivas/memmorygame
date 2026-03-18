import React from "react";
import BoardRenderer from "./BoardRenderer";
import { useGame } from "../../context/GameContext";

const GameBoard: React.FC = () => {
  const { state } = useGame();
  return (
    <div className="game-board">
      <BoardRenderer
        board={state.board}
        layout={state.settings.boardLayout}
        shape={state.settings.cardShape}
      />
    </div>
  );
};
export default GameBoard;
