# qrng.py
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

def generate_random_number(num_qubits=3):
    if not isinstance(num_qubits, int) or num_qubits <= 0:
        raise ValueError("The number of qubits must be a positive integer.")

    try:
        # Creation of a quantum circuit
        qc = QuantumCircuit(num_qubits, num_qubits)

        # Hadamard
        qc.h(range(num_qubits))

        # Measure
        qc.measure(range(num_qubits), range(num_qubits))

        # Aer simulator
        backend = Aer.get_backend('qasm_simulator')

        transpiled_circuit = transpile(qc, backend)
        job = backend.run(transpiled_circuit, shots=1)
        result = job.result()

        counts = result.get_counts()
        bitstring = list(counts.keys())[0]

        # Transform bitstring to number
        return int(bitstring, 2)

    except Exception as e:
        print("An error occurred while trying to generate a random quantum number:")
        print(e)
        return None
