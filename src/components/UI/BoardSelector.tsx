import React from "react";
import { BOARD_LAYOUTS } from "../../utils/constants";
import { BoardLayout } from "../../types/gameTypes";

interface BoardSelectorProps {
  selected: string;
  onSelect: (layout: BoardLayout) => void;
}

const BoardSelector: React.FC<BoardSelectorProps> = ({
  selected,
  onSelect,
}) => (
  <div className="board-options">
    {BOARD_LAYOUTS.map((layout) => (
      <button
        key={layout.key}
        className={selected === layout.key ? "selected" : ""}
        onClick={() => onSelect(layout.key as BoardLayout)}
      >
        {layout.label}
      </button>
    ))}
  </div>
);

export default BoardSelector;
