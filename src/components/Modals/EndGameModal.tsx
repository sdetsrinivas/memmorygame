import React from "react";
import { useGame } from "../../context/GameContext";

const EndGameModal: React.FC = () => {
  const { state, dispatch } = useGame();
  const { players } = state;
  const winner =
    players[0].score === players[1].score
      ? null
      : players[0].score > players[1].score
        ? players[0]
        : players[1];

  return (
    <div className="endgame-modal">
      <h2>Game Over</h2>
      <div>Player 1: {players[0].score}</div>
      <div>Player 2: {players[1].score}</div>
      <div className="winner">
        {winner ? `Winner: ${winner.name}` : "It’s a tie!"}
      </div>
      <button onClick={() => dispatch({ type: "reset" })}>Play Again</button>
      <button
        onClick={() =>
          dispatch({ type: "set_settings", payload: state.settings })
        }
      >
        Change Settings
      </button>
    </div>
  );
};
export default EndGameModal;
