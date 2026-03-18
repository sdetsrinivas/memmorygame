// Utility functions for geometric card positioning

export function getTrianglePositions(
  cardCount: number,
): { x: number; y: number; orientation: "upright" | "inverted" }[] {
  // Pyramid patterns:
  // 25 cards: 1+3+5+7+9 = 25 (5 rows pyramid)
  // 36 cards: 1+3+5+7+9+11 = 36 (6 rows pyramid)
  // Each row has odd number of triangles (1, 3, 5, 7, 9, 11)
  // Triangles alternate upright (△) and inverted (▽) to form honeycomb pattern
  const positions: {
    x: number;
    y: number;
    orientation: "upright" | "inverted";
  }[] = [];

  // Define pyramid row sizes
  let rowSizes: number[];
  if (cardCount === 25) {
    rowSizes = [1, 3, 5, 7, 9]; // 5 rows = 25 cards
  } else if (cardCount === 36) {
    rowSizes = [1, 3, 5, 7, 9, 11]; // 6 rows = 36 cards
  } else {
    // Fallback for any other unexpected cardCount
    return [];
  }

  // Calculate triangle dimensions for tight packing
  // Each small equilateral triangle has height = sqrt(3)/2 when side = 1
  const triangleWidth = 1;
  const triangleHeight = Math.sqrt(3) / 2;

  // Generate positions for each row
  let cardIndex = 0;
  for (let row = 0; row < rowSizes.length; row++) {
    const cardsInRow = rowSizes[row];
    // Center the row horizontally
    const rowWidth = cardsInRow * triangleWidth;
    const xOffset = -(rowWidth - triangleWidth) / 2;

    for (let col = 0; col < cardsInRow; col++) {
      // Calculate x position
      const x = col + xOffset;

      // Calculate y position (rows go down)
      const y = row * triangleHeight;

      // Alternate orientation: upright for even (row+col), inverted for odd (row+col)
      // This creates the honeycomb pattern where adjacent triangles fit together
      const orientation = (row + col) % 2 === 0 ? "upright" : "inverted";

      positions.push({ x, y, orientation });
      cardIndex++;
    }
  }

  return positions.slice(0, cardCount);
}

export function getPolygonPositions(
  cardCount: number,
  sides: number,
): { x: number; y: number }[] {
  // Arrange cards in concentric rings
  const positions: { x: number; y: number }[] = [];
  const rings = cardCount <= sides * 2 ? 2 : 3;
  let cardIndex = 0;
  for (let ring = 1; ring <= rings; ring++) {
    const cardsInRing = Math.min(sides, cardCount - cardIndex);
    for (let i = 0; i < cardsInRing; i++) {
      const angle = (360 / cardsInRing) * i;
      positions.push({
        x: ring * Math.cos((angle * Math.PI) / 180),
        y: ring * Math.sin((angle * Math.PI) / 180),
      });
      cardIndex++;
    }
  }
  return positions;
}
