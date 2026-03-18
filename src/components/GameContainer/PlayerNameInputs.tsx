import React from "react";

interface PlayerNameInputsProps {
  names: [string, string];
  onChange: (index: 0 | 1, name: string) => void;
}

const PlayerNameInputs: React.FC<PlayerNameInputsProps> = ({
  names,
  onChange,
}) => (
  <div>
    <input
      type="text"
      value={names[0]}
      onChange={(e) => onChange(0, e.target.value)}
      placeholder="Player 1"
    />
    <input
      type="text"
      value={names[1]}
      onChange={(e) => onChange(1, e.target.value)}
      placeholder="Player 2"
    />
  </div>
);

export default PlayerNameInputs;
