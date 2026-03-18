export type BoardLayout =
  | "square4"
  | "square6"
  | "square8"
  | "triangle25"
  | "triangle36";
export type Difficulty = "easy" | "medium" | "hard";
export type CardShape = "square" | "triangle";

export interface Card {
  id: number;
  pairId: number;
  iconPath: string;
  isFlipped: boolean;
  isMatched: boolean;
}

export interface Player {
  id: 1 | 2;
  name: string;
  score: number;
}

export interface GameSettings {
  boardLayout: BoardLayout;
  difficulty: Difficulty;
  cardBackColor: string;
  cardShape: CardShape;
}

export interface GameState {
  gameState: "setup" | "playing" | "ended";
  board: Card[];
  players: [Player, Player];
  currentPlayerIndex: 0 | 1;
  flipped: number[];
  matched: number[];
  settings: GameSettings;
}

export interface GameAction {
  type:
    | "flip"
    | "check_match"
    | "next_turn"
    | "reset"
    | "set_settings"
    | "start_game"
    | "init_board";
  payload?: any;
}

export const initialGameState: GameState = {
  gameState: "setup",
  board: [],
  players: [
    { id: 1, name: "Player 1", score: 0 },
    { id: 2, name: "Player 2", score: 0 },
  ],
  currentPlayerIndex: 0,
  flipped: [],
  matched: [],
  settings: {
    boardLayout: "square4",
    difficulty: "easy",
    cardBackColor: "#4a90e2",
    cardShape: "square",
  },
};

export function gameReducer(state: GameState, action: GameAction): GameState {
  switch (action.type) {
    case "flip":
      if (typeof action.payload.cardId === "number") {
        const cardIdToFlip = action.payload.cardId;
        return {
          ...state,
          flipped: [...state.flipped, cardIdToFlip],
          board: state.board.map((card) =>
            card.id === cardIdToFlip ? { ...card, isFlipped: true } : card,
          ),
        };
      }
      // Handle board initialization
      return {
        ...state,
        board: action.payload.board || state.board,
        players: action.payload.names
          ? [
              { ...state.players[0], name: action.payload.names[0] },
              { ...state.players[1], name: action.payload.names[1] },
            ]
          : state.players,
      };
    case "check_match": {
      const [card1Id, card2Id] = action.payload;
      const card1 = state.board.find((c) => c.id === card1Id);
      const card2 = state.board.find((c) => c.id === card2Id);
      if (card1 && card2 && card1.pairId === card2.pairId) {
        // Match found
        const newMatched = [...state.matched, card1Id, card2Id];
        const isGameOver = newMatched.length === state.board.length;
        const updatedPlayers: [Player, Player] = state.players.map((p, i) =>
          i === state.currentPlayerIndex ? { ...p, score: p.score + 1 } : p,
        ) as [Player, Player];
        return {
          ...state,
          matched: newMatched,
          board: state.board.map((card) =>
            card.id === card1Id || card.id === card2Id
              ? { ...card, isMatched: true, isFlipped: true }
              : card,
          ),
          players: updatedPlayers,
          gameState: isGameOver ? "ended" : "playing",
          // Player keeps turn
        };
      } else {
        // No match - switch turn
        const boardAfterFlip = state.board.map((card) =>
          card.id === card1Id || card.id === card2Id
            ? { ...card, isFlipped: false }
            : card,
        );
        return {
          ...state,
          currentPlayerIndex: state.currentPlayerIndex === 0 ? 1 : 0,
          flipped: [],
          board: boardAfterFlip,
        };
      }
    }
    case "next_turn":
      return {
        ...state,
        currentPlayerIndex: state.currentPlayerIndex === 0 ? 1 : 0,
        flipped: [],
      };
    case "start_game":
      return {
        ...state,
        gameState: "playing",
        board: action.payload.board || state.board,
        players: action.payload.names
          ? [
              { ...state.players[0], name: action.payload.names[0], score: 0 },
              { ...state.players[1], name: action.payload.names[1], score: 0 },
            ]
          : state.players,
        flipped: [],
        matched: [],
        currentPlayerIndex: 0,
      };
    case "init_board":
      return {
        ...state,
        board: action.payload.board,
        players: action.payload.names
          ? [
              { ...state.players[0], name: action.payload.names[0] },
              { ...state.players[1], name: action.payload.names[1] },
            ]
          : state.players,
      };
    case "reset":
      return initialGameState;
    case "set_settings":
      return {
        ...state,
        settings: action.payload,
      };
    default:
      return state;
  }
}
