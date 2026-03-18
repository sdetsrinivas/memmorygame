import React from "react";
import CardGrid from "./CardGrid";
import { CardShape, BoardLayout, Card } from "../../types/gameTypes";

interface BoardRendererProps {
  board: Card[];
  layout: BoardLayout;
  shape: CardShape;
}

const BoardRenderer: React.FC<BoardRendererProps> = ({
  board,
  layout,
  shape,
}) => {
  // ...existing code for layout selection...
  return <CardGrid board={board} layout={layout} shape={shape} />;
};
export default BoardRenderer;
