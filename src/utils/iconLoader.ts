/**
 * Icon Loader Utility
 * Dynamically loads SVG icons from the assets folder
 * Supports all difficulty levels and categories
 */

import categoriesData from "./categories.json";

export type Difficulty = "easy" | "medium" | "hard";

interface Category {
  id: string;
  name: string;
  totalIcons: number;
  iconDirectory: string;
}

/**
 * Get all available categories for a difficulty
 */
export const getCategoriesByDifficulty = (
  difficulty: Difficulty,
): Category[] => {
  return categoriesData[difficulty as keyof typeof categoriesData] || [];
};

/**
 * Get a random set of icons from a category
 * @param difficulty - The difficulty level
 * @param categoryId - The category ID
 * @param count - Number of icons to get (default 32)
 * @returns Array of icon paths
 */
export const getIconsFromCategory = (
  difficulty: Difficulty,
  categoryId: string,
  count: number = 32,
): string[] => {
  const categories = getCategoriesByDifficulty(difficulty);
  const category = categories.find((c) => c.id === categoryId);

  if (!category) {
    console.warn(`Category not found: ${difficulty}/${categoryId}`);
    return getDefaultIcons(count);
  }

  const icons: string[] = [];
  const availableCount = Math.min(count, category.totalIcons);

  // Generate icon paths: /assets/icons/{difficulty}/{category}/{1..32}.svg
  for (let i = 1; i <= availableCount; i++) {
    icons.push(`${category.iconDirectory}/${i}.svg`);
  }

  return icons;
};

/**
 * Get random icons from a category, shuffled
 * @param difficulty - The difficulty level
 * @param categoryId - The category ID
 * @param count - Number of icons to get (default 32)
 * @returns Shuffled array of icon paths
 */
export const getShuffledIconsFromCategory = (
  difficulty: Difficulty,
  categoryId: string,
  count: number = 32,
): string[] => {
  const icons = getIconsFromCategory(difficulty, categoryId, count);
  return shuffleArray(icons);
};

/**
 * Get the full path to an icon asset
 * @param relativePath - Relative path from assets folder (e.g., "icons/easy/animals/1.svg")
 * @returns Public path to the icon
 */
export const getIconPath = (relativePath: string): string => {
  return `/assets/${relativePath}`;
};

/**
 * Validate if an icon path exists in the directory structure
 * @param difficulty - The difficulty level
 * @param categoryId - The category ID
 * @param iconIndex - The icon number (1-32)
 * @returns Whether the icon exists
 */
export const doesIconExist = (
  difficulty: Difficulty,
  categoryId: string,
  iconIndex: number,
): boolean => {
  const categories = getCategoriesByDifficulty(difficulty);
  const category = categories.find((c) => c.id === categoryId);

  if (!category) return false;

  return iconIndex >= 1 && iconIndex <= category.totalIcons;
};

/**
 * Get default placeholder icons (in case category is not found)
 * @param count - Number of icons to generate
 * @returns Array of placeholder icon paths
 */
const getDefaultIcons = (count: number): string[] => {
  const icons: string[] = [];
  for (let i = 1; i <= Math.min(count, 32); i++) {
    icons.push(`icons/easy/animals/${i}.svg`);
  }
  return icons;
};

/**
 * Fisher-Yates shuffle algorithm
 * @param array - Array to shuffle
 * @returns Shuffled array
 */
export const shuffleArray = <T>(array: T[]): T[] => {
  const arr = [...array];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
};

/**
 * Preload an icon SVG file
 * Useful for performance optimization
 * @param iconPath - Path to the icon (relative to public folder)
 */
export const preloadIcon = async (iconPath: string): Promise<string | null> => {
  try {
    const response = await fetch(getIconPath(iconPath));
    if (response.ok) {
      return await response.text();
    }
  } catch (error) {
    console.warn(`Failed to preload icon: ${iconPath}`, error);
  }
  return null;
};

/**
 * Preload multiple icons
 * @param iconPaths - Array of icon paths
 */
export const preloadIcons = async (iconPaths: string[]): Promise<void> => {
  await Promise.all(iconPaths.map(preloadIcon));
};

const iconLoaderExport = {
  getCategoriesByDifficulty,
  getIconsFromCategory,
  getShuffledIconsFromCategory,
  getIconPath,
  doesIconExist,
  preloadIcon,
  preloadIcons,
  shuffleArray,
};

export default iconLoaderExport;
