import { Card, Player } from "../types/gameTypes";

export function createBoard(categoryIcons: string[], count: number): Card[] {
  // Pair the icons (each icon appears twice)
  const paired = categoryIcons.slice(0, count / 2).flatMap((icon, idx) => [
    {
      id: idx * 2,
      pairId: idx,
      iconPath: icon,
      isFlipped: false,
      isMatched: false,
    },
    {
      id: idx * 2 + 1,
      pairId: idx,
      iconPath: icon,
      isFlipped: false,
      isMatched: false,
    },
  ]);
  return shuffle(paired);
}

export function shuffle<T>(array: T[]): T[] {
  const arr = [...array];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

export function isGameOver(matched: number[], totalCards: number): boolean {
  return matched.length === totalCards;
}

export function getWinner(players: Player[]): Player | null {
  if (players[0].score === players[1].score) return null;
  return players[0].score > players[1].score ? players[0] : players[1];
}
