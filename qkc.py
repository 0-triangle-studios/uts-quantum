from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import qiskit_ibm_runtime
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime.executor_sampler import Sampler
from qiskit.quantum_info import SparsePauliOp
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

# ─── 1. Build the circuit ─────────────────────────────────────────────
qc = QuantumCircuit(3, 3)

# Put all 3 qubits into equal superposition
qc.h([0, 1, 2])

# Measure all qubits → 3-bit string
qc.measure([0, 1, 2], [0, 1, 2])

print(qc.draw())

# ─── 2. Run the simulation ────────────────────────────────────────────
backend = AerSimulator()
result = backend.run(qc, shots=1).result()

# Extract the single 3-bit outcome (e.g. '101')
bitstring = list(result.get_counts().keys())[0]
print(f"Measured bitstring: {bitstring}")

# ─── 3. Lookup table: bitstring → pitch properties ────────────────────
PITCH_TABLE = {
    '000': {'direction':   0, 'speed': 140, 'description': 'Centre, medium'},
    '001': {'direction':   0, 'speed': 160, 'description': 'Centre, fast'},
    '010': {'direction': -15, 'speed': 140, 'description': 'Left, medium'},
    '011': {'direction': -15, 'speed': 160, 'description': 'Left, fast'},
    '100': {'direction':  15, 'speed': 140, 'description': 'Right, medium'},
    '101': {'direction':  15, 'speed': 160, 'description': 'Right, fast'},
    '110': {'direction': -30, 'speed': 130, 'description': 'Far left, slow'},
    '111': {'direction':  30, 'speed': 130, 'description': 'Far right, slow'},
}

# ─── 4. Look up the pitch ─────────────────────────────────────────────
pitch = PITCH_TABLE[bitstring]
print(f"\nPitch: {pitch['description']}")
print(f"  Direction: {pitch['direction']}* from centre")
print(f"  Speed:     {pitch['speed']} km/h")   