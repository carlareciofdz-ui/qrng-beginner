#Quantum Random Number Generator
This project implements a Quantum Random Number Generator (QRNG) using Qiskit. It uses quantum superposition and measurement to produce random numbers.

#How It Works
- n qubits are put into superposition using Hadamard gates.
- Measurement collapses each qubit to 0 or 1 randomly.
- The bitstring is converted to a number in the range \[ 0, 2ⁿ-1 \].

#Requirements
qiskit>=1.0
qiskit-aer>=0.13

Install with:
pip install -r requirements.txt

#Usage
from qrng import generate_random_number

print("Random number:", generate_random_number(num_qubits=3))

#Project Structure
qrng-beginner/
├── README.md
├── requirements.txt
└── qrng.py