#QISKit dependencies
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import qiskit_ibm_runtime
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime.executor_sampler import Sampler
from qiskit.quantum_info import SparsePauliOp
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

#QISKit code

def qkc():
    qc = QuantumCircuit(3, 3)

    #put 3 qubits into equal superposition
    qc.h([0, 1, 2])

    #put all qubits into 3 classical bit string
    qc.measure([0, 1, 2], [0, 1, 2])

    print(qc.draw())

    #run simulation
    backend = AerSimulator()
    result = backend.run(qc, shots=1).result()

    #get the single 3-bit outcome
    bitstring = list(result.get_counts().keys())[0]

    #lookup table: bitstring determines pitch properties
    PITCH_TABLE = {
        '000': {'type':   "curvierball", 'speed': 2}, #wonky
        '001': {'type':   "curvierball", 'speed': 1},
        '010': {'type':   "curveball", 'speed': 1}, #less curved
        '011': {'type':   "curveball", 'speed': 2},
        '100': {'type':   "curvsirball", 'speed': 3}, #curved
        '101': {'type':   "curvsirball", 'speed': 1},
        '110': {'type':   "nongball", 'speed': 1}, #straight
        '111': {'type':   "nongball", 'speed': 3},
    }

    #     4. Look up the pitch 
    pitch = PITCH_TABLE[bitstring]
    return pitch
#end QISKit code

#game dependencies
import pygame
import time
running = True

def INC(x, max, mult):
    return x + mult if x < max else 1

SCOREBOARD = 0
HIT_TIMER = 0

IDLE_index = 1
IDLE_max = 5
hit = False
BALL_frame = 15
swing_index = 1
swing_max = 3
throw = {"speed": 0,"type": 0}

#game logic
def int_main():
    #do game stuff
    global IDLE_index
    global BALL_frame
    global hit
    global swing_index
    global running
    global SCOREBOARD
    global HIT_TIMER
    global throw
    #ball code
    if HIT_TIMER == 0:
        throw = qkc()
        print(repr(throw))
        HIT_TIMER = throw['speed']*15+14
    else:
        HIT_TIMER = INC(HIT_TIMER, HIT_TIMER + 1, -1)
    
    print(HIT_TIMER)

    BALL_frame = min(14, max(0, INC(BALL_frame, 14, throw['speed']) if HIT_TIMER <= 14 else (14 if BALL_frame >= 14 else 0)))   
    ballmg = pygame.image.load(throw['type'] + str(BALL_frame).zfill(4) + ".jpg")
    print("ball" + str(BALL_frame))
    #end ball code
    screen.blit(ballmg, (0,0))
    if not hit:
        tpmg = pygame.image.load("IDLE_" + str(IDLE_index) + ".png").convert_alpha()
        IDLE_index = INC(IDLE_index, IDLE_max, 1)

        #draw commands
        screen.blit(tpmg, (0, 0))
    else:
        tpmg = pygame.image.load("HIT_" + str(swing_index) + ".jpg")
        swing_index = swing_index + 1
        if swing_index >= swing_max:
            hit = False
            swing_index = 1

        #draw
        screen.blit(tpmg, (0,0))
    

    #xinput
    for ev in pygame.event.get():

        # Keyboard
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_SPACE:
                print("Space pressed!")
                hit = True
            if ev.key == pygame.K_TAB:
                running = False
        # Mouse
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:   # 1 = left click
                print(f"Clicked at {ev.pos}")
                
#########

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("QBall")

while running:
    # boilerplate code
    time.sleep(0.125)
    screen.fill(( 3, 3, 3)) 
    int_main()
    #end boilerplate code
    pygame.display.flip()
pygame.quit()