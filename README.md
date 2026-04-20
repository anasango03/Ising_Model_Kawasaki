# Ising Model: Kawasaki Dynamics

This project contains a Python implementation to simulate the Ising model using **Kawasaki dynamics** (spin exchange with magnetization conservation). The code computes thermodynamic observables and visualizes phase transitions.

## Project Structure

The software features a modular design to separate the simulation logic from data generation and analysis:

* **`1_kawasaki.py`**: Core module containing the Metropolis algorithm logic and the main simulation function.
* **Execution Scripts (`2_dens_kawa.py` to `6_suscep_kawa.py`)**: These scripts import functions from the core module to sample data for energy, magnetization, specific heat, and magnetic susceptibility. The results are automatically exported to `.txt` files.
* **`graphs`**: Jupyter Notebooks that processes the generated data files to perform statistical analysis and graphical representation of the results.
* **`kawasaki.pdf`**: Detailed scientific report covering the theoretical framework and a comprehensive discussion of the obtained results.

## Requirements

* Python 3.x
* Libraries: `numpy`, `matplotlib`, `scipy`
* Jupyter Notebook (for data visualization)

## How to Run

1. Execute the numbered scripts (2-6) to generate the necessary data files.
2. Open `graphs` to visualize the phase transitions and thermal observables.
