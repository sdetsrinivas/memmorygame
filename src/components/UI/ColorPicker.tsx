import React from "react";
import { COLOR_SWATCHES } from "../../utils/constants";

interface ColorPickerProps {
  selected: string;
  onSelect: (color: string) => void;
}

const ColorPicker: React.FC<ColorPickerProps> = ({ selected, onSelect }) => (
  <select
    className="color-dropdown"
    style={{
      backgroundColor: selected,
      color: ["#4a90e2", "#9d4ae2", "#4ae2d8", "#6b7280"].includes(selected)
        ? "#fff"
        : "#333",
    }}
    value={selected}
    onChange={(e) => onSelect(e.target.value)}
  >
    {COLOR_SWATCHES.map((swatch) => (
      <option key={swatch.value} value={swatch.value}>
        {swatch.name}
      </option>
    ))}
  </select>
);

export default ColorPicker;
