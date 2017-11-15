# use QISKit.org
from qiskit import QuantumProgram

# useful additional packages
from qiskit.tools.visualization import plot_histogram

# Creating Programs create your first QuantumProgram object instance.
Q_program = QuantumProgram()

# Creating Registers create your first Quantum Register called "qr" with 2 qubits
qr = Q_program.create_quantum_register("qr", 2)
# create your first Classical Register called "cr" with 2 bits
cr = Q_program.create_classical_register("cr", 2)
# Creating Circuits create your first Quantum Circuit called "qc" involving your Quantum Register "qr"
# and your Classical Register "cr"
qc = Q_program.create_circuit("superposition", [qr], [cr])

# add the X gate in the Qubit 0, we put this Qubit in superposition
qc.x(qr[0])

# add measure to see the state
qc.measure(qr, cr)

# Compiled  and execute in the local_qasm_simulator
result = Q_program.execute(["superposition"], backend='local_qasm_simulator', shots=1024)

# Show the results
plot_histogram(result.get_counts("superposition"))
