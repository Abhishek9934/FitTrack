#!/usr/bin/env python3
"""
Generate PWA icons using SVG
This script creates app icons in various sizes for the PWA
"""

def create_fitness_icon_svg():
    """Create a fitness-themed SVG icon"""
    svg_content = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="512" height="512" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#FF6B6B;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#FF8E53;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="weight" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#4ECDC4;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#44A08D;stop-opacity:1" />
    </linearGradient>
  </defs>
  
  <!-- Background circle -->
  <circle cx="256" cy="256" r="240" fill="url(#bg)" />
  
  <!-- Dumbbell -->
  <g transform="translate(256,256)">
    <!-- Left weight -->
    <rect x="-180" y="-60" width="60" height="120" rx="30" fill="url(#weight)" />
    <!-- Right weight -->
    <rect x="120" y="-60" width="60" height="120" rx="30" fill="url(#weight)" />
    <!-- Bar -->
    <rect x="-140" y="-15" width="280" height="30" rx="15" fill="#2C3E50" />
    <!-- Grips -->
    <rect x="-80" y="-20" width="160" height="40" rx="20" fill="#34495E" />
    
    <!-- Progress chart symbol -->
    <g transform="translate(0,-120)">
      <polyline points="-60,40 -30,20 0,30 30,10 60,0" 
                stroke="white" stroke-width="8" fill="none" 
                stroke-linecap="round" stroke-linejoin="round"/>
      <circle cx="-60" cy="40" r="6" fill="white"/>
      <circle cx="-30" cy="20" r="6" fill="white"/>
      <circle cx="0" cy="30" r="6" fill="white"/>
      <circle cx="30" cy="10" r="6" fill="white"/>
      <circle cx="60" cy="0" r="6" fill="white"/>
    </g>
  </g>
  
  <!-- Shadow effect -->
  <circle cx="256" cy="256" r="240" fill="none" stroke="rgba(0,0,0,0.1)" stroke-width="8" />
</svg>'''
    
    return svg_content

def save_svg_icon():
    """Save the SVG icon"""
    svg_content = create_fitness_icon_svg()
    with open('icon.svg', 'w') as f:
        f.write(svg_content)
    print("Created icon.svg")

if __name__ == "__main__":
    save_svg_icon()
    print("Run: rsvg-convert -w 512 -h 512 icon.svg -o icon-512x512.png")
    print("Then create other sizes: 72, 96, 128, 144, 152, 192, 384")