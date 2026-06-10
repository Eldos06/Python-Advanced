# 📖 Speed Reading & Mental Agility App

> **Based on the book:** _"Эффективное скорочтение. 60-дневный 2-е издание" (2nd Edition) [Инна Владимировна Каулина]
> ![[Pasted image 20260609100213.png]]
> This app is a 60-day daily training assistant designed to improve reading speed, peripheral vision, cognitive flexibility, and mental math skills.

## 🚀 Project Overview

The goal of this project is to build an interactive daily trainer. Users will log in each day and complete a circuit of **4 main exercises**. The app tracks their daily progress, completion time, and accuracy over a 60-day period.

### 🛠 Core Modules to Build:

1. **Schulte Tables** (Таблицы Шульте) — Expand peripheral vision.
    
2. **60-Day Arithmetic** (60-дневная арифметика) — Fast-paced basic math sprints.
    
3. **Stroop Tests** (Тесты Струпа) — Cognitive flexibility and focus.
    
4. **Mental Math** (Устный счет) — Stopwatch-style mental counting speed test.
    

## 🧩 Detailed Module Breakdown

### 1. Schulte Tables (Работа с таблицами Шульте)

A grid of randomly distributed numbers. The user must look at the center of the grid and find all numbers in ascending order (1 to 25) using _only_ their peripheral vision.

- **How it works:** * Generate a $5 \times 5$ grid containing random numbers from 1 to 25.
    
    - Start a timer automatically when the screen loads.
        
    - The user must click numbers from 1 to 25 sequentially.
        
    - If they click the wrong number, show a brief visual error (e.g., red flash).
    ![[Pasted image 20260609101223.png]]
        
- **Developer Notes:** * Keep track of the total time taken to complete the grid.
    
    - _Feature idea:_ Add grid sizes ($3 \times 3$, $4 \times 4$, $5 \times 5$) for difficulty levels.
        

### 2. 60-Day Arithmetic (60-дневная арифметика)

A high-speed math sprint designed to "warm up" the brain before reading practices.

- **How it works:**
    
    - The user is presented with simple, rapid-fire equations (e.g., $7 + 4 = ?$, $12 - 5 = ?$, $3 \times 6 = ?$).
        
    - They have a fixed time limit (e.g., 1 or 2 minutes) to solve as many as possible.
    ![[photo_2026-06-09_10-08-44.jpg]]
        
- **Developer Notes:**
    
    - Generate simple operations ($+$, $-$, $\times$, $\div$).
        
    - Track **Total Attempted** vs. **Correct Answers** within the time limit.
        

### 3. Stroop Test (Тесты Струпа)

This test demonstrates the interference in reaction time of a task. Words representing colors are printed in a color not denoted by the name (e.g., the word "RED" printed in blue ink).

- **How it works:**
    
    - Display a color name text on the screen (e.g., **"GREEN"**).
        
    - Render that text in a different font color (e.g., Red ink).
        
    - Ask the user: _"What is the COLOR of the text?"_ or _"What is the WORD?"_.
        
    - Provide buttons for selection.
	![[Pasted image 20260609101352.png]]
        
- **Developer Notes:**
    
    - Randomize both the string value and the CSS color property.
        
    - Measure reaction time in milliseconds for each answer to calculate average focus speed.