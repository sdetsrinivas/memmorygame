export const COLOR_SWATCHES = [
  { name: "Blue", value: "#4a90e2" },
  { name: "Red", value: "#e24a4a" },
  { name: "Green", value: "#4ae24a" },
  { name: "Purple", value: "#9d4ae2" },
  { name: "Orange", value: "#e2904a" },
  { name: "Pink", value: "#e24ab8" },
  { name: "Teal", value: "#4ae2d8" },
  { name: "Gray", value: "#6b7280" },
];

export const BOARD_LAYOUTS = [
  { key: "square4", label: "4×4", cards: 16 },
  { key: "square6", label: "6×6", cards: 36 },
  { key: "square8", label: "8×8", cards: 64 },
  { key: "triangle25", label: "Triangle (25 cards)", cards: 25 },
  { key: "triangle36", label: "Triangle (36 cards)", cards: 36 },
];

export const DIFFICULTY_CATEGORIES = {
  easy: ["animals", "sports", "fruits"],
  medium: ["flags", "vehicles", "emojis"],
  hard: ["art", "patterns"],
};
