import React, { useMemo, CSSProperties } from "react";
import Card from "./Card";
import {
  CardShape,
  BoardLayout,
  Card as CardType,
} from "../../types/gameTypes";
import { getTrianglePositions } from "../../utils/layoutEngine";
import "../../../src/assets/styles/board.css";

interface CardGridProps {
  board: CardType[];
  layout: BoardLayout;
  shape: CardShape;
}

const getGridStyle = (layout: BoardLayout): CSSProperties => {
  switch (layout) {
    case "square4":
      return { gridTemplateColumns: "repeat(4, 1fr)" };
    case "square6":
      return { gridTemplateColumns: "repeat(6, 1fr)" };
    case "square8":
      return { gridTemplateColumns: "repeat(8, 1fr)" };
    default:
      return { display: "flex", flexWrap: "wrap" };
  }
};

const CardGrid: React.FC<CardGridProps> = ({ board, layout, shape }) => {
  const isSquareLayout = layout.startsWith("square");
  const positions = useMemo(() => {
    if (isSquareLayout) return null;
    if (layout === "triangle25") {
      return getTrianglePositions(25);
    }
    if (layout === "triangle36") {
      return getTrianglePositions(36);
    }
    return null;
  }, [layout, isSquareLayout]);

  if (isSquareLayout) {
    return (
      <div
        className={`card-grid layout-${layout} shape-${shape}`}
        style={getGridStyle(layout)}
      >
        {board.map((card) => (
          <Card key={card.id} {...card} shape={shape} />
        ))}
      </div>
    );
  }

  return (
    <div
      className={`card-grid layout-${layout} shape-${shape} polygon-layout`}
      style={{ position: "relative", width: "100%", minHeight: "400px" }}
    >
      {board.map((card, idx) => {
        const pos = positions?.[idx] || { x: 0, y: 0, orientation: "upright" };
        // For triangle25, the first card (index 0) is the center non-flippable card
        const isCenter = layout === "triangle25" && idx === 0;
        return (
          <div
            key={card.id}
            style={{
              position: "absolute",
              left: `calc(50% + ${pos.x * 80}px)`,
              top: `calc(50% + ${pos.y * 80}px)`,
              transform: "translate(-50%, -50%)",
            }}
          >
            <Card
              {...card}
              shape={shape}
              orientation={pos.orientation}
              isCenter={isCenter}
            />
          </div>
        );
      })}
    </div>
  );
};
export default CardGrid;
