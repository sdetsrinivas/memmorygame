import React from "react";
import PreGameSetup from "./PreGameSetup";
import GameBoard from "../Board/GameBoard";
import PlayerInfo from "./PlayerInfo";
import EndGameModal from "../Modals/EndGameModal";
import { useGame } from "../../context/GameContext";

const GameContainer: React.FC = () => {
  const { state } = useGame();

  if (state.gameState === "setup") return <PreGameSetup />;
  if (state.gameState === "ended") return <EndGameModal />;

  return (
    <div className="game-container">
      <PlayerInfo />
      <GameBoard />
    </div>
  );
};

export default GameContainer;
