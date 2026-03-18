import React from "react";
import { useGame } from "../../context/GameContext";

const PlayerInfo: React.FC = () => {
  const { state } = useGame();
  const { players, currentPlayerIndex } = state;
  return (
    <div className="player-info">
      <div className={currentPlayerIndex === 0 ? "active" : ""}>
        {players[0].name}: {players[0].score}
      </div>
      <div className={currentPlayerIndex === 1 ? "active" : ""}>
        {players[1].name}: {players[1].score}
      </div>
      <div className="turn-indicator">
        Turn: {players[currentPlayerIndex].name}
      </div>
    </div>
  );
};
export default PlayerInfo;
