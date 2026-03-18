import React from "react";
import { DIFFICULTY_CATEGORIES } from "../../utils/constants";
import { Difficulty } from "../../types/gameTypes";

interface CategorySelectorProps {
  difficulty: string;
  selected: string;
  onSelect: (category: string) => void;
}

const CategorySelector: React.FC<CategorySelectorProps> = ({
  difficulty,
  selected,
  onSelect,
}) => {
  const categories = DIFFICULTY_CATEGORIES[difficulty as Difficulty] || [];

  return (
    <select
      className="category-dropdown"
      value={selected}
      onChange={(e) => onSelect(e.target.value)}
    >
      {categories.map((cat: string) => (
        <option key={cat} value={cat}>
          {cat.charAt(0).toUpperCase() + cat.slice(1)}
        </option>
      ))}
    </select>
  );
};

export default CategorySelector;
