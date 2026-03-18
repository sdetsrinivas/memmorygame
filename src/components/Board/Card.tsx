import React from "react";
import { Card as CardType, CardShape } from "../../types/gameTypes";
import { useGame } from "../../context/GameContext";

interface CardProps extends CardType {
  shape: CardShape;
  orientation?: "upright" | "inverted";
  isCenter?: boolean;
  onFlip?: (cardId: number) => void;
}

const getCardShapeSVG = (shape: CardShape, color: string) => {
  switch (shape) {
    case "triangle":
      // Default upright triangle
      return (
        <svg viewBox="0 0 100 100" className="card-shape">
          <polygon points="50,10 90,90 10,90" fill={color} />
        </svg>
      );
    default:
      return (
        <div
          className="card-shape"
          style={{
            backgroundColor: color,
            borderRadius: 8,
            width: "100%",
            height: "100%",
          }}
        />
      );
  }
};

const Card: React.FC<CardProps> = ({
  id,
  isFlipped,
  isMatched,
  iconPath,
  shape,
  orientation = "upright",
  isCenter,
  onFlip,
}) => {
  const { state, dispatch } = useGame();
  const cardBackColor = state.settings.cardBackColor;

  // For 24-card triangle layout, the center tile is non-flippable
  const canFlip =
    !isCenter && !isFlipped && !isMatched && state.flipped.length < 2;

  const handleClick = () => {
    if (!canFlip) return;

    dispatch({ type: "flip", payload: { cardId: id } });
    const newFlipped = [...state.flipped, id];

    if (newFlipped.length === 2) {
      setTimeout(() => {
        dispatch({ type: "check_match", payload: newFlipped });
      }, 800);
    }

    onFlip?.(id);
  };

  return (
    <div
      className={`card ${isFlipped ? "flipped" : ""} ${isMatched ? "matched" : ""}`}
      onClick={handleClick}
      style={{ cursor: canFlip ? "pointer" : "default" }}
    >
      <div className="card-inner">
        <div className="card-face card-front">
          {shape === "triangle" && orientation === "inverted" ? (
            <svg viewBox="0 0 100 100" className="card-shape">
              <polygon points="50,90 90,10 10,10" fill={cardBackColor} />
            </svg>
          ) : (
            getCardShapeSVG(shape, cardBackColor)
          )}
        </div>
        <div className="card-face card-back">
          <img src={iconPath} alt="icon" className="card-icon" />
        </div>
      </div>
    </div>
  );
};
export default Card;
