import React from "react";
import GameContainer from "./components/GameContainer/GameContainer";
import { GameProvider } from "./context/GameContext";

const App: React.FC = () => (
  <GameProvider>
    <GameContainer />
  </GameProvider>
);

export default App;
