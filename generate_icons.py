#!/usr/bin/env python3
"""
Generate SVG icons for Memory Game
Creates 32 unique icons for each of 8 categories
Total: 256 SVG files
"""

import os
import random
import colorsys
from pathlib import Path

# Base path for icons
BASE_PATH = Path("src/assets/icons")

# Category definitions
CATEGORIES = {
    "easy": {
        "animals": {
            "totalIcons": 32,
            "shapes": ["circle", "square", "triangle"],
            "colors": ["#FF6B6B", "#4ECDC4", "#45B7D1", "#FFA07A", "#98D8C8"],
            "symbols": ["🐱", "🐶", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🐨", "🐯", "🦁", "🐮", "🐷", "🐸", "🐵", "🐔", "🐧", "🐦", "🐤", "🦆", "🦅", "🦉", "🦇", "🐴", "🦄", "🐝", "🐛", "🦋", "🐌", "🐞", "🐜", "🦟"],
        },
        "sports": {
            "totalIcons": 32,
            "shapes": ["circle", "hexagon"],
            "colors": ["#E74C3C", "#3498DB", "#F39C12", "#27AE60", "#9B59B6"],
            "symbols": ["⚽", "🏀", "🏈", "⚾", "🥎", "🎾", "🏐", "🏉", "🥏", "🎳", "🏓", "🏸", "🏒", "🏑", "🥍", "🏏", "🥅", "⛳", "⛸️", "🎣", "🎽", "🎿", "⛷️", "🏂", "🪂", "🏋️", "🤼", "🤸", "⛹️", "🤺", "🤾", "🏌️"],
        },
        "fruits": {
            "totalIcons": 32,
            "shapes": ["circle", "oval", "hexagon"],
            "colors": ["#E84B3A", "#F4C430", "#6B4C3A", "#9B2E3A", "#2E8C3A"],
            "symbols": ["🍎", "🍊", "🍋", "🍌", "🍉", "🍇", "🍓", "🫐", "🍈", "🍒", "🍑", "🥭", "🍍", "🥥", "🥝", "🍅", "🍆", "🥑", "🥦", "🥬", "🥒", "🌶️", "🌽", "🥔", "🍠", "🥐", "🥯", "🍞", "🥖", "🥨", "🧀", "🥚"],
        },
    },
    "medium": {
        "flags": {
            "totalIcons": 32,
            "shapes": ["square", "rectangle", "trapezoid"],
            "colors": ["#FF0000", "#0000FF", "#FFFF00", "#00FF00", "#FF6600"],
            "symbols": ["🇺🇸", "🇬🇧", "🇮🇳", "🇨🇦", "🇦🇺", "🇯🇵", "🇰🇷", "🇫🇷", "🇩🇪", "🇮🇹", "🇪🇸", "🇲🇽", "🇧🇷", "🇳🇿", "🇸🇬", "🇻🇳", "🇹🇭", "🇬🇷", "🇵🇱", "🇳🇱", "🇸🇪", "🇨🇭", "🇧🇪", "🇦🇹", "🇩🇰", "🇫🇮", "🇮🇸", "🇳🇴", "🇵🇹", "🇨🇿", "🇭🇺", "🇷🇴"],
        },
        "vehicles": {
            "totalIcons": 32,
            "shapes": ["triangle", "hexagon", "circle"],
            "colors": ["#E74C3C", "#3498DB", "#2ECC71", "#F39C12", "#34495E"],
            "symbols": ["🚗", "🚕", "🚙", "🚌", "🚎", "🏎️", "🚓", "🚑", "🚒", "🚐", "🛻", "🚚", "🚛", "🚜", "🏍️", "🏎️", "🛵", "🚲", "🛴", "🛹", "🛼", "✈️", "🛩️", "🛫", "🛬", "🚁", "🛶", "⛵", "🚤", "🛳️", "⛴️", "🚢"],
        },
        "emojis": {
            "totalIcons": 32,
            "shapes": ["circle", "star", "heart"],
            "colors": ["#FFD700", "#FF69B4", "#1E90FF", "#00CED1", "#FF4500"],
            "symbols": ["😀", "😃", "😄", "😁", "😆", "😅", "🤣", "😂", "🙂", "🙃", "😉", "😊", "😇", "🥰", "😍", "🤩", "😘", "😗", "😚", "😙", "🥲", "😋", "😛", "😜", "🤪", "😌", "😔", "😑", "😐", "😶", "🙁", "☹️"],
        },
    },
    "hard": {
        "art": {
            "totalIcons": 32,
            "shapes": ["hexagon", "star"],
            "colors": ["#8B0000", "#4169E1", "#32CD32", "#FFD700", "#FF00FF"],
            "symbols": ["🎨", "🎭", "🎪", "🎬", "🎤", "🎧", "🎼", "🎹", "🎸", "🥁", "🎺", "🎻", "🎲", "🎯", "🎳", "🎮", "🎰", "👓", "⌚", "💍", "👑", "💄", "💋", "📿", "🎓", "🎩", "🧢", "✒️", "🖋️", "🖊️", "🖌️", "🖍️"],
        },
        "patterns": {
            "totalIcons": 32,
            "shapes": ["square", "hexagon"],
            "colors": ["#000000", "#FF00FF", "#00FFFF", "#FFFF00", "#FF0099"],
            "symbols": ["█", "▓", "▒", "░", "▀", "▄", "█", "▌", "▐", "◼", "◻", "◾", "◽", "⬛", "⬜", "🟫", "🟪", "🟦", "🟥", "🟩", "🟨", "*", "+", "×", "÷", "=", "≠", "≤", "≥", "±", "∞", "∆", "■"],
        },
    },
}


def generate_animal_icon(index, colors):
    """Generate diverse animal-themed icons"""
    color = colors[index % len(colors)]
    accent_color = colors[(index + 1) % len(colors)]
    
    animal_type = index % 8
    
    if animal_type == 0:  # Cat
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="55" r="30" fill="{color}"/>
            <polygon points="30,30 50,10 70,30" fill="{color}"/>
            <circle cx="40" cy="50" r="6" fill="white"/>
            <circle cx="60" cy="50" r="6" fill="white"/>
            <circle cx="40" cy="50" r="3" fill="black"/>
            <circle cx="60" cy="50" r="3" fill="black"/>
            <path d="M 50 65 L 50 72" stroke="black" stroke-width="2"/>
            <line x1="45" y1="68" x2="35" y2="65" stroke="black" stroke-width="1.5"/>
            <line x1="55" y1="68" x2="65" y2="65" stroke="black" stroke-width="1.5"/>
        </svg>'''
    elif animal_type == 1:  # Dog
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <ellipse cx="50" cy="60" rx="25" ry="28" fill="{color}"/>
            <circle cx="50" cy="30" r="22" fill="{color}"/>
            <ellipse cx="35" cy="25" rx="8" ry="12" fill="{color}"/>
            <ellipse cx="65" cy="25" rx="8" ry="12" fill="{color}"/>
            <circle cx="40" cy="35" r="5" fill="white"/>
            <circle cx="60" cy="35" r="5" fill="white"/>
            <circle cx="40" cy="35" r="2.5" fill="black"/>
            <circle cx="60" cy="35" r="2.5" fill="black"/>
            <circle cx="50" cy="48" r="3" fill="#FFB6C1"/>
        </svg>'''
    elif animal_type == 2:  # Fish
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <ellipse cx="55" cy="50" rx="28" ry="20" fill="{color}"/>
            <polygon points="80,50 95,40 95,60" fill="{color}"/>
            <circle cx="75" cy="50" r="5" fill="{accent_color}"/>
            <circle cx="70" cy="45" r="3" fill="white"/>
            <circle cx="70" cy="45" r="1.5" fill="black"/>
            <path d="M 40 35 L 30 25" stroke="{accent_color}" stroke-width="2"/>
            <path d="M 40 65 L 30 75" stroke="{accent_color}" stroke-width="2"/>
        </svg>'''
    elif animal_type == 3:  # Butterfly
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <ellipse cx="40" cy="40" rx="15" ry="20" fill="{color}"/>
            <ellipse cx="60" cy="40" rx="15" ry="20" fill="{color}"/>
            <ellipse cx="35" cy="65" rx="12" ry="18" fill="{accent_color}"/>
            <ellipse cx="65" cy="65" rx="12" ry="18" fill="{accent_color}"/>
            <line x1="50" y1="20" x2="50" y2="80" stroke="#333" stroke-width="1.5"/>
            <circle cx="40" cy="35" r="2" fill="white"/>
            <circle cx="60" cy="35" r="2" fill="white"/>
        </svg>'''
    elif animal_type == 4:  # Bird
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <ellipse cx="50" cy="55" rx="20" ry="18" fill="{color}"/>
            <circle cx="65" cy="40" r="16" fill="{color}"/>
            <polygon points="80,38 100,33 95,45" fill="{color}"/>
            <circle cx="75" cy="38" r="4" fill="{accent_color}"/>
            <circle cx="73" cy="36" r="1.5" fill="black"/>
            <line x1="45" y1="68" x2="40" y2="80" stroke="#FFA500" stroke-width="2"/>
            <line x1="55" y1="68" x2="60" y2="80" stroke="#FFA500" stroke-width="2"/>
        </svg>'''
    elif animal_type == 5:  # Turtle
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="28" fill="{color}"/>
            <circle cx="50" cy="50" r="24" fill="{accent_color}"/>
            <path d="M 30 50 L 20 50" stroke="{color}" stroke-width="4" stroke-linecap="round"/>
            <path d="M 70 50 L 80 50" stroke="{color}" stroke-width="4" stroke-linecap="round"/>
            <path d="M 50 30 L 50 20" stroke="{color}" stroke-width="4" stroke-linecap="round"/>
            <path d="M 50 70 L 50 80" stroke="{color}" stroke-width="4" stroke-linecap="round"/>
            <circle cx="50" cy="50" r="6" fill="white"/>
            <circle cx="50" cy="50" r="3" fill="black"/>
        </svg>'''
    elif animal_type == 6:  # Lion
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="55" r="22" fill="{color}"/>
            <circle cx="50" cy="50" r="32" fill="none" stroke="{color}" stroke-width="8"/>
            <circle cx="40" cy="45" r="5" fill="white"/>
            <circle cx="60" cy="45" r="5" fill="white"/>
            <circle cx="40" cy="45" r="2.5" fill="black"/>
            <circle cx="60" cy="45" r="2.5" fill="black"/>
            <polygon points="50,65 48,72 52,72" fill="{accent_color}"/>
        </svg>'''
    elif animal_type == 7:  # Rabbit
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="60" r="25" fill="{color}"/>
            <circle cx="50" cy="30" r="18" fill="{color}"/>
            <ellipse cx="42" cy="12" rx="6" ry="15" fill="{color}"/>
            <ellipse cx="58" cy="12" rx="6" ry="15" fill="{color}"/>
            <ellipse cx="42" cy="13" rx="3" ry="10" fill="{accent_color}"/>
            <ellipse cx="58" cy="13" rx="3" ry="10" fill="{accent_color}"/>
            <circle cx="43" cy="33" r="4" fill="white"/>
            <circle cx="57" cy="33" r="4" fill="white"/>
            <circle cx="43" cy="33" r="2" fill="black"/>
            <circle cx="57" cy="33" r="2" fill="black"/>
            <circle cx="50" cy="48" r="4" fill="#FFB6C1"/>
        </svg>'''
    
    return f'<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="40" fill="{color}"/></svg>'


def generate_sports_icon(index, colors):
    """Generate diverse sports equipment icons"""
    color = colors[index % len(colors)]
    accent_color = colors[(index + 1) % len(colors)]
    
    sport_type = index % 8
    
    if sport_type == 0:  # Soccer ball
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="35" fill="white" stroke="{color}" stroke-width="2"/>
            <polygon points="50,25 60,35 60,50 50,55 40,50 40,35" fill="{color}"/>
            <polygon points="50,50 60,50 65,60 60,70 50,75 40,70 35,60 40,50" fill="{color}"/>
            <path d="M 45 30 L 55 30 M 45 70 L 55 70 M 30 45 L 30 55 M 70 45 L 70 55" stroke="{accent_color}" stroke-width="1"/>
        </svg>'''
    elif sport_type == 1:  # Basketball
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="35" fill="{color}"/>
            <line x1="50" y1="15" x2="50" y2="85" stroke="white" stroke-width="2"/>
            <path d="M 30 50 Q 50 30 70 50" fill="none" stroke="white" stroke-width="2"/>
            <path d="M 30 50 Q 50 70 70 50" fill="none" stroke="white" stroke-width="2"/>
        </svg>'''
    elif sport_type == 2:  # Baseball
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="32" fill="white" stroke="{color}" stroke-width="2"/>
            <path d="M 30 45 Q 50 30 70 45" fill="none" stroke="{color}" stroke-width="2"/>
            <path d="M 30 55 Q 50 70 70 55" fill="none" stroke="{color}" stroke-width="2"/>
        </svg>'''
    elif sport_type == 3:  # Tennis racket
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="35" r="22" fill="none" stroke="{color}" stroke-width="3"/>
            <path d="M 50 52 Q 48 65 50 80" stroke="{color}" stroke-width="3" fill="none" stroke-linecap="round"/>
            <path d="M 30 35 L 70 35 M 35 25 L 65 25 M 35 45 L 65 45" fill="none" stroke="{accent_color}" stroke-width="1.5"/>
        </svg>'''
    elif sport_type == 4:  # Golf flag
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <rect x="45" y="30" width="3" height="50" fill="#8B4513"/>
            <polygon points="48,32 48,45 70,40" fill="{color}"/>
            <circle cx="50" cy="80" r="6" fill="{accent_color}"/>
            <circle cx="50" cy="80" r="3" fill="white"/>
        </svg>'''
    elif sport_type == 5:  # Cricket bat and ball
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <rect x="35" y="40" width="6" height="40" fill="{color}" transform="rotate(-20 38 60)"/>
            <circle cx="38" cy="35" rx="8" ry="12" fill="{color}" transform="rotate(-20 38 35)"/>
            <circle cx="65" cy="35" r="7" fill="{accent_color}"/>
            <path d="M 61 35 L 69 35 M 65 31 L 65 39" stroke="white" stroke-width="1"/>
        </svg>'''
    elif sport_type == 6:  # Bowling pins
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="30" r="6" fill="{color}"/>
            <circle cx="40" cy="42" r="6" fill="{color}"/>
            <circle cx="60" cy="42" r="6" fill="{color}"/>
            <circle cx="30" cy="54" r="6" fill="{color}"/>
            <circle cx="50" cy="54" r="6" fill="{color}"/>
            <circle cx="70" cy="54" r="6" fill="{color}"/>
            <circle cx="50" cy="70" r="8" fill="{accent_color}"/>
        </svg>'''
    elif sport_type == 7:  # Gymnast
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="25" r="8" fill="{color}"/>
            <line x1="50" y1="33" x2="50" y2="55" stroke="{color}" stroke-width="3"/>
            <line x1="50" y1="38" x2="30" y2="30" stroke="{color}" stroke-width="3"/>
            <line x1="50" y1="38" x2="70" y2="30" stroke="{color}" stroke-width="3"/>
            <line x1="50" y1="55" x2="35" y2="75" stroke="{color}" stroke-width="3"/>
            <line x1="50" y1="55" x2="65" y2="75" stroke="{color}" stroke-width="3"/>
        </svg>'''
    
    return f'<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="40" fill="{color}"/></svg>'


def generate_fruit_icon(index, colors):
    """Generate diverse fruit icons"""
    color = colors[index % len(colors)]
    accent_color = colors[(index + 1) % len(colors)]
    
    fruit_type = index % 8
    
    if fruit_type == 0:  # Apple
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="55" r="32" fill="{color}"/>
            <rect x="48" y="18" width="4" height="25" fill="#8B4513"/>
            <ellipse cx="62" cy="32" rx="8" ry="5" fill="#228B22"/>
            <circle cx="50" cy="45" r="4" fill="{accent_color}" opacity="0.6"/>
        </svg>'''
    elif fruit_type == 1:  # Banana
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <path d="M 25 70 Q 50 20 75 50" fill="{color}" stroke="{color}" stroke-width="18"/>
            <ellipse cx="25" cy="72" rx="6" ry="8" fill="#654321"/>
            <ellipse cx="75" cy="52" rx="6" ry="8" fill="#654321"/>
            <path d="M 30 65 L 70 45" stroke="{accent_color}" stroke-width="1" opacity="0.4"/>
        </svg>'''
    elif fruit_type == 2:  # Watermelon
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="35" fill="{color}"/>
            <circle cx="50" cy="50" r="30" fill="#FF69B4"/>
            <circle cx="40" cy="40" r="3" fill="#228B22"/>
            <circle cx="55" cy="45" r="3" fill="#228B22"/>
            <circle cx="50" cy="60" r="3" fill="#228B22"/>
            <circle cx="45" cy="50" r="3" fill="#228B22"/>
        </svg>'''
    elif fruit_type == 3:  # Lemon
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <ellipse cx="50" cy="52" rx="28" ry="32" fill="{color}"/>
            <ellipse cx="65" cy="35" rx="10" ry="12" fill="{accent_color}"/>
            <path d="M 65 35 L 75 25" stroke="#228B22" stroke-width="2"/>
            <ellipse cx="50" cy="50" rx="10" ry="12" fill="{color}" opacity="0.3"/>
        </svg>'''
    elif fruit_type == 4:  # Strawberry
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <polygon points="50,75 40,65 45,50 40,35 50,30 60,35 55,50 60,65" fill="{color}"/>
            <circle cx="45" cy="55" r="4" fill="#FFA500"/>
            <circle cx="55" cy="55" r="4" fill="#FFA500"/>
            <circle cx="50" cy="45" r="4" fill="#FFA500"/>
            <path d="M 48 28 L 45 20 M 50 28 L 50 18 M 52 28 L 55 20" stroke="#228B22" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
    elif fruit_type == 5:  # Orange
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="32" fill="{color}"/>
            <g opacity="0.3">
                <line x1="50" y1="20" x2="50" y2="80" stroke="white" stroke-width="1.5"/>
                <line x1="20" y1="50" x2="80" y2="50" stroke="white" stroke-width="1.5"/>
                <path d="M 30 30 Q 50 50 70 70" fill="none" stroke="white" stroke-width="1.5"/>
                <path d="M 70 30 Q 50 50 30 70" fill="none" stroke="white" stroke-width="1.5"/>
            </g>
            <path d="M 55 18 L 62 22" stroke="#228B22" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
    elif fruit_type == 6:  # Grapes
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="38" cy="32" r="10" fill="{color}"/>
            <circle cx="62" cy="32" r="10" fill="{color}"/>
            <circle cx="30" cy="48" r="10" fill="{color}"/>
            <circle cx="50" cy="48" r="10" fill="{color}"/>
            <circle cx="70" cy="48" r="10" fill="{color}"/>
            <circle cx="40" cy="62" r="10" fill="{color}"/>
            <circle cx="60" cy="62" r="10" fill="{color}"/>
            <path d="M 50 20 L 50 32 L 38 32" stroke="#228B22" stroke-width="2"/>
        </svg>'''
    elif fruit_type == 7:  # Pineapple
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <polygon points="50,30 65,65 50,75 35,65" fill="{color}"/>
            <g opacity="0.4" stroke="{accent_color}" stroke-width="1">
                <line x1="40" y1="45" x2="60" y2="45"/>
                <line x1="40" y1="55" x2="60" y2="55"/>
                <line x1="40" y1="65" x2="60" y2="65"/>
            </g>
            <path d="M 42 28 L 45 15 M 50 28 L 50 12 M 58 28 L 55 15" stroke="#228B22" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
    
    return f'<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="40" fill="{color}"/></svg>'


def generate_flag_icon(index, colors):
    """Generate diverse flag icons"""
    color1 = colors[index % len(colors)]
    color2 = colors[(index + 1) % len(colors)]
    color3 = colors[(index + 2) % len(colors)]
    
    flag_type = index % 8
    if flag_type == 0:  # Vertical stripes
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <rect x="20" y="25" width="15" height="50" fill="{color1}"/>
            <rect x="35" y="25" width="15" height="50" fill="{color2}"/>
            <rect x="50" y="25" width="15" height="50" fill="{color3}"/>
            <rect x="65" y="25" width="15" height="50" fill="{color1}"/>
            <rect x="10" y="73" width="70" height="4" fill="#333"/>
            <rect x="10" y="73" width="3" height="18" fill="#333"/>
        </svg>'''
    elif flag_type == 1:  # Horizontal stripes
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <rect x="20" y="25" width="60" height="12" fill="{color1}"/>
            <rect x="20" y="37" width="60" height="12" fill="{color2}"/>
            <rect x="20" y="49" width="60" height="12" fill="{color3}"/>
            <rect x="20" y="61" width="60" height="12" fill="{color1}"/>
            <rect x="10" y="75" width="3" height="16" fill="#333"/>
        </svg>'''
    elif flag_type == 2:  # Diagonal
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <polygon points="20,25 80,25 80,60 20,75" fill="{color1}"/>
            <polygon points="20,40 80,35 80,60 20,65" fill="{color2}"/>
            <line x1="20" y1="25" x2="80" y2="60" stroke="{color3}" stroke-width="3"/>
            <rect x="10" y="75" width="3" height="16" fill="#333"/>
        </svg>'''
    elif flag_type == 3:  # Quarter divided
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <rect x="20" y="25" width="30" height="25" fill="{color1}"/>
            <rect x="50" y="25" width="30" height="25" fill="{color2}"/>
            <rect x="20" y="50" width="30" height="25" fill="{color3}"/>
            <rect x="50" y="50" width="30" height="25" fill="{color1}"/>
            <rect x="10" y="75" width="3" height="16" fill="#333"/>
        </svg>'''
    elif flag_type == 4:  # Triangle split
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <polygon points="20,25 50,25 80,60 20,75" fill="{color1}"/>
            <polygon points="50,25 80,25 80,60 50,42" fill="{color2}"/>
            <polygon points="80,60 50,42 80,75" fill="{color3}"/>
            <rect x="10" y="75" width="3" height="16" fill="#333"/>
        </svg>'''
    elif flag_type == 5:  # Circular pattern
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <rect x="20" y="25" width="60" height="50" fill="{color1}"/>
            <circle cx="50" cy="50" r="15" fill="{color2}"/>
            <circle cx="50" cy="50" r="10" fill="{color3}"/>
            <circle cx="50" cy="50" r="5" fill="{color1}"/>
            <rect x="10" y="75" width="3" height="16" fill="#333"/>
        </svg>'''
    elif flag_type == 6:  # Checkered pattern
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <rect x="20" y="25" width="12" height="12" fill="{color1}"/>
            <rect x="32" y="25" width="12" height="12" fill="{color2}"/>
            <rect x="44" y="25" width="12" height="12" fill="{color3}"/>
            <rect x="56" y="25" width="12" height="12" fill="{color1}"/>
            <rect x="68" y="25" width="12" height="12" fill="{color2}"/>
            <rect x="20" y="37" width="12" height="12" fill="{color2}"/>
            <rect x="32" y="37" width="12" height="12" fill="{color3}"/>
            <rect x="44" y="37" width="12" height="12" fill="{color1}"/>
            <rect x="56" y="37" width="12" height="12" fill="{color2}"/>
            <rect x="68" y="37" width="12" height="12" fill="{color3}"/>
            <rect x="20" y="49" width="12" height="12" fill="{color3}"/>
            <rect x="32" y="49" width="12" height="12" fill="{color1}"/>
            <rect x="44" y="49" width="12" height="12" fill="{color2}"/>
            <rect x="56" y="49" width="12" height="12" fill="{color3}"/>
            <rect x="68" y="49" width="12" height="12" fill="{color1}"/>
            <rect x="20" y="61" width="12" height="12" fill="{color1}"/>
            <rect x="32" y="61" width="12" height="12" fill="{color2}"/>
            <rect x="44" y="61" width="12" height="12" fill="{color3}"/>
            <rect x="56" y="61" width="12" height="12" fill="{color1}"/>
            <rect x="68" y="61" width="12" height="12" fill="{color2}"/>
            <rect x="10" y="75" width="3" height="16" fill="#333"/>
        </svg>'''
    else:  # Wavy edges
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <path d="M 20 25 Q 30 20 40 25 T 80 25 L 80 65 Q 70 70 60 65 T 20 65 Z" fill="{color1}"/>
            <path d="M 20 45 Q 30 40 40 45 T 80 45 L 80 65 Q 70 70 60 65 T 20 65 Z" fill="{color2}"/>
            <rect x="10" y="75" width="3" height="16" fill="#333"/>
        </svg>'''
    
    return f'<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><rect x="20" y="25" width="60" height="50" fill="{color1}"/><rect x="10" y="75" width="3" height="16" fill="#333"/></svg>'


def generate_vehicle_icon(index, colors):
    """Generate diverse vehicle icons"""
    color = colors[index % len(colors)]
    accent_color = colors[(index + 1) % len(colors)]
    
    vehicle_type = index % 8
    
    if vehicle_type == 0:  # Car
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <rect x="20" y="50" width="60" height="18" fill="{color}" rx="3"/>
            <rect x="28" y="36" width="44" height="18" fill="{color}" rx="3"/>
            <circle cx="30" cy="70" r="8" fill="#333"/>
            <circle cx="70" cy="70" r="8" fill="#333"/>
            <rect x="35" y="40" width="9" height="10" fill="#87CEEB"/>
            <rect x="56" y="40" width="9" height="10" fill="#87CEEB"/>
        </svg>'''
    elif vehicle_type == 1:  # Bus
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <rect x="15" y="35" width="70" height="38" fill="{color}" rx="4"/>
            <rect x="22" y="40" width="11" height="12" fill="#87CEEB" stroke="white" stroke-width="0.5"/>
            <rect x="37" y="40" width="11" height="12" fill="#87CEEB" stroke="white" stroke-width="0.5"/>
            <rect x="52" y="40" width="11" height="12" fill="#87CEEB" stroke="white" stroke-width="0.5"/>
            <rect x="67" y="40" width="11" height="12" fill="#87CEEB" stroke="white" stroke-width="0.5"/>
            <circle cx="28" cy="76" r="7" fill="#333"/>
            <circle cx="72" cy="76" r="7" fill="#333"/>
            <rect x="28" y="65" width="44" height="2" fill="{accent_color}"/>
        </svg>'''
    elif vehicle_type == 2:  # Plane
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <ellipse cx="50" cy="40" rx="25" ry="12" fill="{color}"/>
            <rect x="48" y="35" width="4" height="40" fill="{color}"/>
            <rect x="25" y="48" width="50" height="3" fill="{color}"/>
            <polygon points="48,75 45,85 52,85" fill="{color}"/>
            <circle cx="72" cy="40" r="6" fill="{accent_color}"/>
        </svg>'''
    elif vehicle_type == 3:  # Motorcycle
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="30" cy="65" r="10" fill="none" stroke="{color}" stroke-width="2"/>
            <circle cx="70" cy="65" r="10" fill="none" stroke="{color}" stroke-width="2"/>
            <polygon points="45,45 60,35 70,70 40,70" fill="{color}"/>
            <circle cx="55" cy="40" r="5" fill="{accent_color}"/>
            <line x1="30" y1="55" x2="30" y2="50" stroke="{color}" stroke-width="2"/>
        </svg>'''
    elif vehicle_type == 4:  # Train
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <rect x="15" y="35" width="20" height="25" fill="{color}"/>
            <rect x="35" y="40" width="15" height="20" fill="{color}"/>
            <rect x="50" y="40" width="15" height="20" fill="{color}"/>
            <rect x="65" y="40" width="15" height="20" fill="{color}"/>
            <circle cx="22" cy="65" r="7" fill="#333"/>
            <circle cx="42" cy="65" r="7" fill="#333"/>
            <circle cx="57" cy="65" r="7" fill="#333"/>
            <circle cx="72" cy="65" r="7" fill="#333"/>
            <polygon points="15,35 10,25 25,25" fill="{accent_color}"/>
        </svg>'''
    elif vehicle_type == 5:  # Helicopter
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <rect x="35" y="50" width="30" height="20" fill="{color}" rx="3"/>
            <rect x="48" y="30" width="4" height="20" fill="{color}"/>
            <ellipse cx="50" cy="20" rx="20" ry="4" fill="{accent_color}"/>
            <ellipse cx="50" cy="20" rx="15" ry="2" fill="white"/>
            <circle cx="40" cy="60" r="4" fill="#333"/>
            <circle cx="60" cy="60" r="4" fill="#333"/>
            <path d="M 50 46 L 45 35 M 50 46 L 55 35" stroke="{color}" stroke-width="1"/>
        </svg>'''
    elif vehicle_type == 6:  # Ship
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <polygon points="25,65 75,65 80,75 20,75" fill="{color}"/>
            <polygon points="40,65 60,65 55,50 45,50" fill="{accent_color}"/>
            <rect x="48" y="40" width="4" height="25" fill="#8B4513"/>
            <polygon points="48,38 40,32 56,32" fill="white" stroke="{accent_color}" stroke-width="1"/>
            <circle cx="50" cy="50" r="2" fill="white"/>
        </svg>'''
    elif vehicle_type == 7:  # Rocket
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <polygon points="50,20 65,60 50,50 35,60" fill="{color}"/>
            <rect x="45" y="50" width="10" height="35" fill="{color}"/>
            <polygon points="42,82 35,90 40,85" fill="{accent_color}"/>
            <polygon points="58,82 65,90 60,85" fill="{accent_color}"/>
            <polygon points="45,75 50,85 55,75" fill="white"/>
            <circle cx="50" cy="65" r="3" fill="white"/>
        </svg>'''
    
    return f'<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><rect x="20" y="40" width="60" height="30" fill="{color}"/><circle cx="35" cy="70" r="8" fill="#333"/><circle cx="65" cy="70" r="8" fill="#333"/></svg>'


def generate_emoji_icon(index, colors):
    """Generate diverse emoji/emotion face icons"""
    color = colors[index % len(colors)]
    emotion = index % 8
    
    if emotion == 0:  # Happy/Smiling
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="38" fill="{color}"/>
            <circle cx="38" cy="40" r="6" fill="black"/>
            <circle cx="62" cy="40" r="6" fill="black"/>
            <path d="M 38 60 Q 50 72 62 60" stroke="black" stroke-width="3" fill="none" stroke-linecap="round"/>
        </svg>'''
    elif emotion == 1:  # Surprised
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="38" fill="{color}"/>
            <circle cx="38" cy="40" r="7" fill="white" stroke="black" stroke-width="1.5"/>
            <circle cx="62" cy="40" r="7" fill="white" stroke="black" stroke-width="1.5"/>
            <circle cx="38" cy="40" r="3" fill="black"/>
            <circle cx="62" cy="40" r="3" fill="black"/>
            <circle cx="50" cy="65" r="6" fill="black"/>
        </svg>'''
    elif emotion == 2:  # Sad
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="38" fill="{color}"/>
            <circle cx="38" cy="38" r="5" fill="black"/>
            <circle cx="62" cy="38" r="5" fill="black"/>
            <path d="M 38 65 Q 50 55 62 65" stroke="black" stroke-width="3" fill="none" stroke-linecap="round"/>
            <path d="M 35 35 L 38 30" stroke="black" stroke-width="2" stroke-linecap="round"/>
            <path d="M 65 35 L 62 30" stroke="black" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
    elif emotion == 3:  # Winking
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="38" fill="{color}"/>
            <circle cx="38" cy="40" r="6" fill="black"/>
            <path d="M 60 38 L 68 38 M 60 42 L 68 42" stroke="black" stroke-width="1.5" stroke-linecap="round"/>
            <circle cx="62" cy="40" r="4" fill="white" stroke="black" stroke-width="1"/>
            <path d="M 38 62 Q 50 70 62 62" stroke="black" stroke-width="3" fill="none" stroke-linecap="round"/>
        </svg>'''
    elif emotion == 4:  # Angry
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="38" fill="{color}"/>
            <path d="M 32 35 L 42 42" stroke="black" stroke-width="2" stroke-linecap="round"/>
            <path d="M 42 35 L 32 42" stroke="black" stroke-width="2" stroke-linecap="round"/>
            <path d="M 58 35 L 68 42" stroke="black" stroke-width="2" stroke-linecap="round"/>
            <path d="M 68 35 L 58 42" stroke="black" stroke-width="2" stroke-linecap="round"/>
            <line x1="30" y1="65" x2="70" y2="65" stroke="black" stroke-width="3" stroke-linecap="round"/>
        </svg>'''
    elif emotion == 5:  # Cool/Sunglasses
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="38" fill="{color}"/>
            <rect x="28" y="38" width="12" height="12" fill="black"/>
            <rect x="60" y="38" width="12" height="12" fill="black"/>
            <rect x="41" y="42" width="18" height="2" fill="black"/>
            <circle cx="50" cy="62" r="5" fill="black"/>
            <path d="M 50 67 L 48 73 M 50 67 L 52 73" stroke="black" stroke-width="1.5" stroke-linecap="round"/>
        </svg>'''
    elif emotion == 6:  # Thinking
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="38" fill="{color}"/>
            <path d="M 35 35 Q 28 32 25 38" stroke="black" stroke-width="2" fill="none" stroke-linecap="round"/>
            <circle cx="38" cy="42" r="5" fill="black"/>
            <circle cx="62" cy="42" r="5" fill="black"/>
            <path d="M 38 62 L 35 72 M 62 62 L 65 72" stroke="black" stroke-width="2" stroke-linecap="round"/>
            <path d="M 38 62 Q 50 72 62 62" stroke="black" stroke-width="1.5" fill="none"/>
        </svg>'''
    elif emotion == 7:  # Heart eyes/Love
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="38" fill="{color}"/>
            <path d="M 33 35 L 38 30 L 43 35 L 38 40 Z" fill="red"/>
            <path d="M 57 35 L 62 30 L 67 35 L 62 40 Z" fill="red"/>
            <path d="M 40 65 Q 50 75 60 65" stroke="black" stroke-width="2.5" fill="none" stroke-linecap="round"/>
            <line x1="45" y1="50" x2="45" y2="60" stroke="black" stroke-width="1"/>
            <line x1="55" y1="50" x2="55" y2="60" stroke="black" stroke-width="1"/>
        </svg>'''
    
    return f'<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="40" fill="{color}"/><circle cx="38" cy="40" r="5" fill="black"/><circle cx="62" cy="40" r="5" fill="black"/></svg>'


def generate_art_icon(index, colors):
    """Generate diverse art/abstract icons"""
    color = colors[index % len(colors)]
    accent_color = colors[(index + 1) % len(colors)]
    
    pattern_type = index % 8
    
    if pattern_type == 0:  # Concentric circles
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="5" fill="{color}"/>
            <circle cx="50" cy="50" r="12" fill="none" stroke="{color}" stroke-width="2"/>
            <circle cx="50" cy="50" r="22" fill="none" stroke="{accent_color}" stroke-width="2"/>
            <circle cx="50" cy="50" r="32" fill="none" stroke="{color}" stroke-width="2"/>
        </svg>'''
    elif pattern_type == 1:  # Star burst
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <line x1="50" y1="20" x2="50" y2="80" stroke="{color}" stroke-width="2"/>
            <line x1="20" y1="50" x2="80" y2="50" stroke="{accent_color}" stroke-width="2"/>
            <line x1="25" y1="25" x2="75" y2="75" stroke="{color}" stroke-width="2"/>
            <line x1="75" y1="25" x2="25" y2="75" stroke="{accent_color}" stroke-width="2"/>
            <circle cx="50" cy="50" r="6" fill="{color}"/>
        </svg>'''
    elif pattern_type == 2:  # Grid pattern
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <pattern id="grid" width="15" height="15" patternUnits="userSpaceOnUse">
                    <rect x="0" y="0" width="15" height="15" fill="white" stroke="{color}" stroke-width="1"/>
                </pattern>
            </defs>
            <rect x="20" y="20" width="60" height="60" fill="url(#grid)"/>
            <circle cx="50" cy="50" r="8" fill="{accent_color}"/>
        </svg>'''
    elif pattern_type == 3:  # Spiral
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <path d="M 50 50 Q 60 40 70 50 T 90 70 Q 80 80 70 70 T 50 60 Q 40 55 30 65 T 20 85" fill="none" stroke="{color}" stroke-width="2.5"/></path>
            <circle cx="50" cy="50" r="3" fill="{accent_color}"/>
        </svg>'''
    elif pattern_type == 4:  # Geometric triangles
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <polygon points="50,20 30,70 70,70" fill="{color}"/>
            <polygon points="50,35 38,60 62,60" fill="{accent_color}"/>
            <polygon points="50,45 44,58 56,58" fill="{color}"/>
        </svg>'''
    elif pattern_type == 5:  # Interlocking shapes
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="35" cy="35" r="18" fill="{color}" opacity="0.7"/>
            <circle cx="65" cy="35" r="18" fill="{accent_color}" opacity="0.7"/>
            <circle cx="50" cy="65" r="18" fill="{color}" opacity="0.7"/>
            <circle cx="50" cy="50" r="8" fill="white" stroke="{color}" stroke-width="1.5"/>
        </svg>'''
    elif pattern_type == 6:  # Linear gradient effect
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" style="stop-color:{color};stop-opacity:1" />
                    <stop offset="100%" style="stop-color:{accent_color};stop-opacity:1" />
                </linearGradient>
            </defs>
            <rect x="20" y="20" width="60" height="60" fill="url(#grad)"/>
            <circle cx="50" cy="50" r="12" fill="white" opacity="0.3"/>
        </svg>'''
    elif pattern_type == 7:  # Abstract waves
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <path d="M 20 40 Q 30 20 40 40 T 60 40 T 80 40" fill="none" stroke="{color}" stroke-width="3"/>
            <path d="M 20 55 Q 30 35 40 55 T 60 55 T 80 55" fill="none" stroke="{accent_color}" stroke-width="3"/>
            <path d="M 20 70 Q 30 50 40 70 T 60 70 T 80 70" fill="none" stroke="{color}" stroke-width="3"/>
        </svg>'''
    
    return f'<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="40" fill="{color}"/></svg>'


def generate_pattern_icon(index, colors):
    """Generate diverse pattern icons"""
    color = colors[index % len(colors)]
    accent_color = colors[(index + 1) % len(colors)]
    
    pattern_type = index % 8
    
    if pattern_type == 0:  # Dots
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="25" cy="25" r="8" fill="{color}"/>
            <circle cx="75" cy="25" r="8" fill="{accent_color}"/>
            <circle cx="50" cy="50" r="8" fill="{color}"/>
            <circle cx="25" cy="75" r="8" fill="{accent_color}"/>
            <circle cx="75" cy="75" r="8" fill="{color}"/>
            <circle cx="50" cy="30" r="5" fill="{accent_color}"/>
            <circle cx="30" cy="50" r="5" fill="{color}"/>
            <circle cx="70" cy="50" r="5" fill="{color}"/>
            <circle cx="50" cy="70" r="5" fill="{accent_color}"/>
        </svg>'''
    elif pattern_type == 1:  # Vertical stripes
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <rect x="20" y="20" width="8" height="60" fill="{color}"/>
            <rect x="35" y="20" width="8" height="60" fill="{accent_color}"/>
            <rect x="50" y="20" width="8" height="60" fill="{color}"/>
            <rect x="65" y="20" width="8" height="60" fill="{accent_color}"/>
        </svg>'''
    elif pattern_type == 2:  # Checkerboard
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <rect x="20" y="20" width="12" height="12" fill="{color}"/>
            <rect x="32" y="20" width="12" height="12" fill="{accent_color}"/>
            <rect x="44" y="20" width="12" height="12" fill="{color}"/>
            <rect x="56" y="20" width="12" height="12" fill="{accent_color}"/>
            <rect x="68" y="20" width="12" height="12" fill="{color}"/>
            <rect x="20" y="32" width="12" height="12" fill="{accent_color}"/>
            <rect x="32" y="32" width="12" height="12" fill="{color}"/>
            <rect x="44" y="32" width="12" height="12" fill="{accent_color}"/>
            <rect x="56" y="32" width="12" height="12" fill="{color}"/>
            <rect x="68" y="32" width="12" height="12" fill="{accent_color}"/>
            <rect x="20" y="44" width="12" height="12" fill="{color}"/>
            <rect x="32" y="44" width="12" height="12" fill="{accent_color}"/>
            <rect x="44" y="44" width="12" height="12" fill="{color}"/>
            <rect x="56" y="44" width="12" height="12" fill="{accent_color}"/>
            <rect x="68" y="44" width="12" height="12" fill="{color}"/>
            <rect x="20" y="56" width="12" height="12" fill="{accent_color}"/>
            <rect x="32" y="56" width="12" height="12" fill="{color}"/>
            <rect x="44" y="56" width="12" height="12" fill="{accent_color}"/>
            <rect x="56" y="56" width="12" height="12" fill="{color}"/>
            <rect x="68" y="56" width="12" height="12" fill="{accent_color}"/>
            <rect x="20" y="68" width="12" height="12" fill="{color}"/>
            <rect x="32" y="68" width="12" height="12" fill="{accent_color}"/>
            <rect x="44" y="68" width="12" height="12" fill="{color}"/>
            <rect x="56" y="68" width="12" height="12" fill="{accent_color}"/>
            <rect x="68" y="68" width="12" height="12" fill="{color}"/>
        </svg>'''
    elif pattern_type == 3:  # Wavy lines
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <path d="M 20 30 Q 30 25 40 30 T 60 30 T 80 30" fill="none" stroke="{color}" stroke-width="2.5"/>
            <path d="M 20 50 Q 30 45 40 50 T 60 50 T 80 50" fill="none" stroke="{accent_color}" stroke-width="2.5"/>
            <path d="M 20 70 Q 30 65 40 70 T 60 70 T 80 70" fill="none" stroke="{color}" stroke-width="2.5"/>
        </svg>'''
    elif pattern_type == 4:  # Diamond pattern
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <polygon points="50,20 65,35 50,50 35,35" fill="{color}"/>
            <polygon points="50,50 65,65 50,80 35,65" fill="{accent_color}"/>
            <polygon points="20,50 35,65 20,80 5,65" fill="{color}"/>
            <polygon points="80,50 95,65 80,80 65,65" fill="{accent_color}"/>
            <polygon points="50,50 50,50 50,50 50,50" fill="{color}"/>
        </svg>'''
    elif pattern_type == 5:  # Circles
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="30" cy="30" r="12" fill="none" stroke="{color}" stroke-width="2"/>
            <circle cx="70" cy="30" r="12" fill="none" stroke="{accent_color}" stroke-width="2"/>
            <circle cx="50" cy="50" r="12" fill="none" stroke="{color}" stroke-width="2"/>
            <circle cx="30" cy="70" r="12" fill="none" stroke="{accent_color}" stroke-width="2"/>
            <circle cx="70" cy="70" r="12" fill="none" stroke="{color}" stroke-width="2"/>
        </svg>'''
    elif pattern_type == 6:  # Cross/Plus pattern
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <g stroke="{color}" stroke-width="3" stroke-linecap="round">
                <line x1="50" y1="20" x2="50" y2="35"/>
                <line x1="50" y1="65" x2="50" y2="80"/>
                <line x1="20" y1="50" x2="35" y2="50"/>
                <line x1="65" y1="50" x2="80" y2="50"/>
            </g>
            <g stroke="{accent_color}" stroke-width="2" stroke-linecap="round">
                <line x1="30" y1="30" x2="40" y2="40"/>
                <line x1="60" y1="60" x2="70" y2="70"/>
                <line x1="70" y1="30" x2="60" y2="40"/>
                <line x1="40" y1="60" x2="30" y2="70"/>
            </g>
        </svg>'''
    elif pattern_type == 7:  # Hexagon grid
        return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <polygon points="30,25 40,20 50,25 45,35 35,35" fill="none" stroke="{color}" stroke-width="1.5"/>
            <polygon points="60,25 70,20 80,25 75,35 65,35" fill="none" stroke="{accent_color}" stroke-width="1.5"/>
            <polygon points="30,55 40,50 50,55 45,65 35,65" fill="none" stroke="{accent_color}" stroke-width="1.5"/>
            <polygon points="60,55 70,50 80,55 75,65 65,65" fill="none" stroke="{color}" stroke-width="1.5"/>
            <circle cx="50" cy="50" r="4" fill="{color}"/>
        </svg>'''
    
    return f'<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><rect x="20" y="20" width="60" height="60" fill="{color}"/></svg>'


def generate_icon(category, subcategory, index):
    """Generate SVG icon based on category"""
    total_icons = CATEGORIES[category][subcategory]["totalIcons"]
    colors = CATEGORIES[category][subcategory]["colors"]
    
    generators = {
        ("easy", "animals"): generate_animal_icon,
        ("easy", "sports"): generate_sports_icon,
        ("easy", "fruits"): generate_fruit_icon,
        ("medium", "flags"): generate_flag_icon,
        ("medium", "vehicles"): generate_vehicle_icon,
        ("medium", "emojis"): generate_emoji_icon,
        ("hard", "art"): generate_art_icon,
        ("hard", "patterns"): generate_pattern_icon,
    }
    
    generator = generators.get((category, subcategory))
    if generator:
        return generator(index, colors)
    
    return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <circle cx="50" cy="50" r="40" fill="#999"/>
    </svg>'''


def main():
    """Generate all icons"""
    print("🎨 Generating Memory Game Icons...\n")
    
    total_generated = 0
    
    for category in CATEGORIES:
        for subcategory in CATEGORIES[category]:
            directory = BASE_PATH / category / subcategory
            directory.mkdir(parents=True, exist_ok=True)
            
            total_icons = CATEGORIES[category][subcategory]["totalIcons"]
            
            for i in range(total_icons):
                svg_content = generate_icon(category, subcategory, i)
                file_path = directory / f"{i + 1}.svg"
                
                with open(file_path, "w") as f:
                    f.write(svg_content)
                
                total_generated += 1
            
            print(f"✅ {category}/{subcategory}: {total_icons} icons")
    
    print(f"\n🎉 Total Icons Generated: {total_generated}")
    print("✅ Icon generation complete!")


if __name__ == "__main__":
    main()
