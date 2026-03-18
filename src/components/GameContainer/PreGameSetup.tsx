import React, { useState } from "react";
import BoardSelector from "../UI/BoardSelector";
import CategorySelector from "../UI/CategorySelector";
import ColorPicker from "../UI/ColorPicker";
import PlayerNameInputs from "./PlayerNameInputs";
import { useGame } from "../../context/GameContext";
import { createBoard } from "../../utils/gameLogic";
import { BOARD_LAYOUTS } from "../../utils/constants";
import { getIconsFromCategory } from "../../utils/iconLoader";
import categories from "../../utils/categories.json";

const PreGameSetup: React.FC = () => {
  const { dispatch, state } = useGame();
  const [boardLayout, setBoardLayout] = useState(state.settings.boardLayout);
  const [difficulty, setDifficulty] = useState(state.settings.difficulty);
  const [category, setCategory] = useState("animals");
  const [cardBackColor, setCardBackColor] = useState(
    state.settings.cardBackColor,
  );
  const [names, setNames] = useState([
    state.players[0].name,
    state.players[1].name,
  ]);

  const handleStart = async () => {
    // Get card count from selected layout
    const layoutConfig = BOARD_LAYOUTS.find((l) => l.key === boardLayout);
    const cardCount = layoutConfig?.cards || 16;

    // Get icon paths using the iconLoader utility
    const iconPaths = getIconsFromCategory(
      difficulty as any,
      category,
      cardCount / 2,
    );

    // Convert to public paths (assets/icons/...)
    const publicIconPaths = iconPaths.map((path) => `/assets/${path}`);

    // Create board
    const newBoard = createBoard(publicIconPaths, cardCount);

    // Determine card shape from boardLayout
    let cardShape: "square" | "triangle" = "square";
    if (boardLayout.startsWith("triangle")) cardShape = "triangle";

    // Update state with new game settings
    dispatch({
      type: "set_settings",
      payload: {
        boardLayout,
        difficulty,
        cardBackColor,
        cardShape,
        category,
      },
    });

    // Create new game state with board and start game
    dispatch({
      type: "start_game",
      payload: { board: newBoard, names },
    });
  };

  return (
    <div className="pregame-setup">
      <h2>🧠 Cnee's Memory Game</h2>

      <div className="setup-container">
        <div className="setup-sections">
          <div className="setup-card board-selector">
            <h3>Board Layout</h3>
            <p className="setup-card-desc">
              Choose the size of your game board
            </p>
            <BoardSelector selected={boardLayout} onSelect={setBoardLayout} />
          </div>

          <div className="setup-card difficulty-selector">
            <h3>Difficulty</h3>
            <p className="setup-card-desc">Select game difficulty level</p>
            <select
              className={`difficulty-dropdown difficulty-${difficulty}`}
              value={difficulty}
              onChange={(e) => setDifficulty(e.target.value as any)}
            >
              <option value="easy">Easy</option>
              <option value="medium">Medium</option>
              <option value="hard">Hard</option>
            </select>
          </div>

          <div className="setup-card category-selector">
            <h3>Category</h3>
            <p className="setup-card-desc">Pick the theme of your cards</p>
            <CategorySelector
              difficulty={difficulty}
              selected={category}
              onSelect={setCategory}
            />
          </div>

          <div className="setup-card color-picker">
            <h3>Card Back Color</h3>
            <p className="setup-card-desc">Choose the color of card backs</p>
            <ColorPicker selected={cardBackColor} onSelect={setCardBackColor} />
          </div>

          <div className="setup-card player-name-inputs">
            <h3>Player Names</h3>
            <p className="setup-card-desc">Enter your names (optional)</p>
            <PlayerNameInputs
              names={names as [string, string]}
              onChange={(i, name) =>
                setNames(
                  (names) =>
                    names.map((n, idx) => (idx === i ? name : n)) as [
                      string,
                      string,
                    ],
                )
              }
            />
          </div>
        </div>
      </div>

      <button className="start-btn" onClick={handleStart}>
        Start Game
      </button>
    </div>
  );
};
export default PreGameSetup;
