# Multi-System Power Transmission Calculator

This Python project simulates power transmission through a combination of gears and pulleys. It calculates the final output speed and power after passing through multiple stages, accounting for efficiency losses.

## 🚀 Features

- Models mechanical power transmission systems
- Supports both gear and pulley stages
- Handles speed ratios and efficiency percentages
- Provides detailed breakdown of speed and power after each stage
- Implemented using Python Object-Oriented Programming (OOP)

## 🛠 How It Works

The user is prompted to enter:
- Initial motor speed (RPM)
- Initial power (Watts)
- Number of stages
- For each stage: type (`gear` or `pulley`), speed ratio, and efficiency (%)

The program then:
1. Processes each stage
2. Applies ratio and efficiency
3. Displays output speed and power after each stage
4. Prints the final output speed and power

## 🧠 OOP Structure

- `Stage` class:
  - Stores type, ratio, and efficiency
  - Contains a `process()` method to compute output speed and power

- `TransmissionSystem` class:
  - Holds initial values and a list of stages
  - Computes total output using `calculate()` method

## 📥 Sample Input

