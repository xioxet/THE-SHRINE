# Assesments

- lab quiz: 30
>- lab 2: 5%
>- lab 3 5%
>- final quiz (timed): 20%
- project: 20% (week 7-12)
- quizzes: 20%
>- quiz 1 (Computer architecture): 10%
>- quiz 2 (Computer organisation): 10%
- final exam: 30%

# ict 1011 pre req for

- inf 2004
- ict 2215
- ict 3125
- ict 3213

# Labs
One lab every 2 weeks, CHECK SCHEDULE

pre req: code composer software by Texas Instruments

lab 1 (Week 3/4) MSP430 (microprocessor)
lab 2 (Week 5/6) address mode & data storage
> Lab 2 quiz due week 7
lab 3 (week 8/9) assembly instructions
> lab 3 quiz due week 10
lab 4 (week 10/11)project familiarisation

# Project

Come up with project for tiny screen smart watch kit
Teams of 6
Choose own team mate by week 5 or get auto assigned

# Computer Architecture
vvv
## Fundamentals of Computer Architecture (Chpt 1)

- History and Evolution of Computers
>- 1834, Cambridge, UK
>>- Built by Charles Babbage
>>- Designs: Difference Engine (Subtractor), Analytical Diffrence Engine
>>- Mechanical

>- 1940, Germany
>>- Built by Konrad Zuse
>>- used electrical relays


Major leap during ww2 (1940s)
Research funded mainly by the War Department
Looked to solve problems related to balistics calculations or cryptography over telegram

>- 1943, Bletchley Park, UK
>>- Built by: Tommy Flowers, Alan Turing
>>- Designs: Colossus (Code breaker)
>>- 10 seperate copies, electronic and programable.

>- 1944, USA
>>- Built by:
>>- Designs: ENIAC(Code beraker)
>>- Similar to Colossus

>- ????, Princeton University
>>- Built By: John Von Neumann
>>- Design: Stored Program Concept (Architecture)
>>- Purpose: To create a way to allow the samee machine to run different programs, no longer purpose built computers

>- 1948, Manchester
>>- Design: SSEM (Baby)
>>- First Stored program Computer

>- 1953, Manchester
>>- Transistor computer

>- 1951, USA
>>- MIT (Massachusetts Institute of Technology)
>>- First real time computer

>- 1964, USA
>>- release of IBM System/360

>- 1971, California, USA
>>- Intel releases the Intel 4004 mass-market single
chip CPU
>>- descendants: 8008, 8080, 8080, 8085, 8086, 8088, 80186, 80286, 80386, 80486, Pentium, Pentium II, Pentium III ,Pentium IV, Celeron, Core, Atom...

>- 1977, Massachusetts, USA
>>- Digital Equipment Corporation release the VAX11/780 Mainframe computer

>- Post 1977
>>- Rise of home computers, followed by mobile age and wearables and IOT etc.

> Year | Floating point operations per second, FLOPS
>>- 1941 | 1
>>- 1945 | 100
>>- 1949 | 1,000 (1 KiloFLOPS, kFLOPS)
>>- 1951 | 10,000
>>- 1961 | 100,000
>>- 1964 | 1,000,000 (1 MegaFLOPS, MFLOPS)
>>- 1968 | 10,000,000
>>- 1975 | 100,000,000
>>- 1987 | 1,000,000,000 (1 GigaFLOPS, GFLOPS)
>>- 1992 | 10,000,000,000
>>- 1993 | 100,000,000,000
>>- 1997 | 1,000,000,000,000 (1 TeraFLOPS, TFLOPS)
>>- 2000 | 10,000,000,000,000
>>- 2007 | 478,000,000,000,000 (478 TFLOPS)
>>- 2009 | 1,100,000,000,000,000 (1.1 PetaFLOPS)

- Computer Hardware Decomposition
>- Basic req:
>> a Unit that proccesses numbers (brains)
>> a mains power suply or battery (power for brains)
>> memory (memory for brains)
>> an input device (sensor)
>> an output device (display. speakers)

- Clasess of commputers
Considered loose categories, may chage in future as tech gets better
>- Supercomputer
>- microcomputer (multichip)
>- embedded computer (single chip)

>>- Embedded computers:
>>- Compact, usually single chip, generally not obvious that microprocessor is present, still contains processing unit, memory and peripherals

>>>- System-On-Chip (SOC)
>>>- A microcontroller integrated with other interfacee systems into a single chip.
>>>- e.g. MSP430, contains microcontroller, RF transceiver, Intelligent Peripherals (100-nA comparator, 12bit ADC, 96 segment LCD controller, 128-bit AES processor)

- Basic operations and requirements
>- 3 actions
>- Store/retrieve values
>- Transform values
>- transfer value from one place to another

>- Difference between each computer
>- Where values are stored
>- What type of processing can be done
>- Where can the ddata be transferred from or to.
>- other less important considerations: Speed, accuracy, data size, cost, power consumption, physical size, programmability, ease of debugging, memory size, input & output capabilities.

- Components inside a Computer
>- IC chip (Integrated Circuit Chip) Contains
>- CPU
>- Peripherals Connections
>- Built in memory (ROM & RAM)
>- Internal Host Busses (On-Chip)
>- External Memory Busses (Wires to Off-Cip devices)

>- ROM holds the *program*
>- RAM holds *variables* and *data*
>- ALU (in the CPU) proccesses the data i.e. runs the program
>- ports for input/output

>- The Clock
>- Current Computers are synchornus
>- all actions occur at the rising edge or falling edge
>- this is what *clockspeed* is about
>- complex modern CPUs have 1 master clock and use deviders or multipliers to devrive different clock speeds
>- component closer to chip = faster, component further away from chip = slower
>- clockspeed not the most important. Depends on other factors like transfer rate.
>- 16 bit/cycle at 3 GHz vs 64bit/cycle at 2Ghz
>- = 48GBi/s vs 128GB/s

>- The Reset
>- logic bits stored s voltage, in flip-flop circuits, latches and as electronic charge in capacitive cell (capacitor)
>- circuits do not discharge at the same rate, changing the start state at every shutdown and startup
>- reset charges all logic gates in CPU which resets them, resets program counter in CPU
>- provides reliable and predictable startup sequence
>- hardware reset physically discharges circuit and empties primary memory
>- software reset changes memory to zero AND changes program ccounter to 0
>- PARTIAL software reset only changes the program counter tto 0 to restart the boot process. Means memory still exists in primary memory

>- Memory
>- Non-volatile, retains when power is turned off, can be programable(flash, EEPROM, EPROM) or fixed (ROM) 
>- Volatile, wiped when power is turned off. (SRAM, DRAM, SDRAM, DDR etc)
>>- SPEED
>>- Register > Cache > Main/Primary memory > secondary memory
>>- Registers: Super fast, small, limited in number, is within CPU, operates on CPU clock rate (size: 2-128 registers)
>>- Cache: Fast, static RAM, outside of CPU but close by, Typical Access Time ~ 8-35nS (Size: 1kB - 512kB)
>>- Main/ Primary Memory: Dynamic RAM or ROM (for programable storage). Further from CPU than chache, usually on a peripheral RAM card. Typical Access time: 20-100nS (Size: 1kB-1GB)
>>- Secondary Memory: Not always RAM, Non-volatile. May be magnetic or flash. Typical Access time: 5-20Ms (Size: 1MB-80GB)

- Example-Register to Register data transfer
lets define a register as 8-bits for now.
Lable it as R0 for now.
each bit is a "Room" with 2 doors
>- the room:
>- input > latch input (entry door) > memory cell (room) > enable output(exit door) > output
input and output lines are called the *data line*
latch input and enable output controls are the *control line*

to write data (1) to r0[0]:
>- energize input data line with HIGH Signal voltage
>- enable(energize) latch input control line
>- memory cell is energized by input data line
>- disable(discharge) latch input control line

to write data (0) to r0[0]:
>- energize input data line with LOW Signal voltage
>- enable(energize) latch input control line
>- memory cell is energized by input data line
>- disable(discharge) latch input control line

apply this to each bit to copy data to registers
read from R0[0] by enabling enable output control line
write to R1[0] by enabling latch input control line

>- Tristate buffers: ----------????
>- 3 states are: HIGH, LOW, OFF
>- allows multiple registers to use the same bus to convey data

>- Over clocking and registers:
>- circuits take time to charge or discharge and are affeted by length heat and other things.
>- it is possible to clock faster than you circuits charge or discharge. meaning the computer attempts to read memory from register but opens and closes the latches too quickly to properly energize the circuit.
>- This mmay happen even as the computer attempts to step to the next instruction and may result in incorrect values or crashes.


## The CPU (Chpt 2)

![program_development_process](.\jacob-images\program_development_process.png)

Hardware programming:  
> actual electric voltage in wire  
> Sequence of Arithmetic and logic functions by logic gates and chips  
> result

Software programming:  
> actual electric voltage in wire  
> Sequence of Arithmetic and logic functions by logic gates and chips  
> result

![(Hardware_vs_software_programming](.\jacob-images\Hardware_vs_software_programming.png)  

e.g.  
![](.\jacob-images\Hardware_vs_software_eg.png)

### The von Neuman Architecture  

Most modern day computers are based on von Neuman's stored program concept
1. Both data and program are stored in same memory
2. Contents of memory are addressable by location, without regard to data type
3. Execution occurs sequentially (unless explicitly modified)

### Components of Microcomputer

- Processor  
- Memory  
- I/O interfaces

all connected by bus structure  
Binary info can be transfered in parallel

### Main memory

- Fix-sized  
- high-speed  
- accessed in any order (i.e. RAM)  

each byte-sized location has **unique address** and is accessed by specifying its binary pattern on the **address bus**  

Address Bus size can be found out through the manufacturer who will declare it through the chip specs

Main memory size is dependant on number of lines (n) in the address bus. (memory size = $2^n$ bytes)  
1 line = 1 bit = 2 address  
2 lines = 2 bits = 4 address  
etc.

Memory stores both **data** and **instructiions**.  
e.g.  
> 0000 : + (instruction)  
> 0001 : B (data)  
> 0010 : C (data)  

If size > 8 bit, **consecutive locations** are used

32-bit data how to store?  
01234567 89ABCDEF GHIJKLMN OPQRSTUV, 0 is MSB, V is LSB  
Big Edian (e.g. H*S, MAC, Sun, Motorola):  
> N+0 : 01234567   
> N+1 : 89ABCDEF  
> N+2 : GHIJKLMN  
> N+3 : OPQRSTUV  

Little Endian (e.g Intel, MSP430):
> N+0 : OPQRSTUV   
> N+1 : GHIJKLMN  
> N+2 : 89ABCDEF  
> N+3 : 01234567  

### Instruction in Memory:  
Instructions are stored as an **OP-code** followed by **Operands data**  

it tells CPU what action to take (i.e **executable**)  

**Op-Code** tells CPU which **operation to do** (e.g. add/subtract)  

rest of operands data specifies the **data / location of the data** to be used in the operation.

### Memory Map:  
is a visual means to show contents of some consecutive address space  
Generally drawn as byte-sized or word-sized  
Address and data represented in **Hexadecimal**
Byte:
> H'000000 : H'AB   
> H'000001 : H'CD  
> H'000002 : H'12  
> H'000003 : H'34

Word:
> H'000000 : H'ABCD   
> H'000002 : H'1234  
> H'000004 : H'0000  
> H'000006 : H'67B5  

NOTE: each memory space still only store 1 byte. So word representation addess is 2 per memory  

for H'000002 : H'1234, H'000003 contents depends on Endian  

Big Endian:  
H'000002 : H'12,  
H'000003 : H'34  

Little Endian:  
H'000002 : H'34,  
H'000003 : H'12


### Input Output (IO) Interfaces

2 ways to connect:
Loosely coupled: not always connected  
e.g.  
- via external bus - USB, SCSI, $I^2C$, Firewire  
- via network - Ethernet, ATM, airport (wireless)  
- via port - serial (RS232), parallel, P2S

Tightlly coupled: fixed onto computer - via fast internal bus - graphics & hard-disk controllers

peripherals still generally communicate with CPU the same way, thorugh I/O Interfaces:  
CPU -> Address Bus & Data Bus -> I/O INterface (CPU side) -> I/oInterface (Peropheral side) -> network/bus -> Peripheral device  

SSD/HDD are on motherboard but go through its own interface on motherboard. Because of the interface, SSD/HDD is much slower than primary memory. SSD/HDD also not dependant on address bus size, dependant on interface. Thus SSD/HDD are secondary memory.

types of I/O interface:
1. Parallel
2. Serial

### The CPU

Role:  
- Fetch: CPU fetch/read instruction from memory, CPU fetch/read data from memory after decoing what instruction needs  
- Decode instruction  
- Execute: Execute instruction (arithmetic or logic) on fetched data  
- Write: result may need to be written to temp register or to memory

Register Section  
ALU Section  
Control Section  

CPU as a whole accesses Control, Data and Address busses

## Register Section:  
Where all the registers are stored
- Visible General user registers(User Programs can read or write to)
- - Data registers: hold data temporarily during CPU operations
- - Address registers: holds addresses of operands in memory
- - Stack pointer: special register to manage stack in memory  
- Special user visible registers  
- - Status Register: current status of CPU and set of 1-bit flags that indicates outcome of ALU operations. Flags known as Condition Code Register **(CCR)**
- - Program Counter: address of next instruction to be executed, PC automatically increments after the execution of current instruction. (Important for security, if can control this, can jump to arbitrary code)
- Non-Visible user registers (User program cannot access)  
- - Instruction register - holds op-code of current instruction to be executed  
- - Temporary or buffer register:: holds address/data internally during intermediate stage of CPU op/instruction execution. (e.g. arithmetic op, I/O, interrupt, etc.)

Common Condition Code Flags
- Negative (N) - flag set whenever MSB of result is 1  
- Zero (Z) - flag set whenever result is zero (all bits 0)  
- Overflow (V) - flag et whenevver result cannot be represented by the 2' complement range of number representation. e.g. 16bit num + 16 bit num store into 16 bit register, if return 17bit number, flg will set  
- Carry (C) - flag set when result of addition causes a carry at MSB or subtraction causes a borrow at the MSB.  

Carry flag and overflow very different.  
Carry is for borrow or carry over, result may not overflow as logic may still be ok.

Overflow (V) in Arithmetic Ops:  
Addition: e.g.A+B=C
- set if $(A_{Sign}=B_{Sign} \neq C_{Sign})$, e.i. A MSB = B MSB but both != C MSB
- Why? Pos + Pos cannot be Neg

Subtraction: e.g.A-B=C
- set if $(C_{Sign}=B_{Sign} \neq A_{Sign})$, e.i. A MSB = B MSB but both != C MSB
- Why? Neg - Pos cannot be Pos OR Pos - Neg cannot be Neg

## ALU Section:  
performs arithmetic and logical ops specified by instruction.  
ALU takes input from Internal bus, outputs to internal bus and Condition Code Register

Number of lines on internal bus is found based on specifications of CPU e.g. 32-bit CPU means internal bus got 32-bits  
Also tells us how big the register is, 32bit CPU, 32bit register

ALU contains its own buffer register for temp storage of input operands and result

Arithmetic: + - * /  
logic: and, or, xor  
shifter: shift left, shift right, rotate

Control unit tells alu what to do in each cycle

Many ops will influence N,Z,V,C flags

## Control Unit:
Roles:
- Decodes instruction: decode opcode into internal and external control signals needed for execution  
- Activates ALU functions based on decoded instructions  
- Controls movemeent of data between memory-register or internally between registers  
- Handles external signals like interupt/reset

## Control and sequnencing:

Operations synchronised by master clock  
CPU can be seen as a sequential state machine  
each instruction has a number of micro operations. Each operation is perfomed at state change of CPU clock  
frequency can range from MHz-GHz


### Impact of Bus width

- CPU internal Bus: impacts number of bits CPU can process in one cycle  
- Data Bus: How much data can be transfered in one cycle. (speed of data transfer) e.g. 8-bit bus, want to store 16-bit, need 2 cycle  
- Address Bus: how large address space is, defined by manufaturer in specs (size of possible storage space)

MSB430 is 16bit data bus, memory size is 8bit. limitation is when retrieving 16bit data, can only retrieve from even addresses due to the hardwiring of the 16bit bus

### Execution cycle

add.w #3, R1  
add word, value 3 to R1

Execution Cycle: Instruction  
> 1. fetch: program counter puts address of instruction on address bus,
> 2. Control unit generates read signal
> 3. CPU reads instruction fro memory to Instruction register over data bus  
> 4. Control unit decode instruction

Execution cycle: Operand
> 1. Program counter send address of operand on address bus  
> 2. Control unit generate read signal  
> 3. Operand #3 fetched from memory to Buffer Register  

Execution cycle: Add  
> 1. Control Unit sends ALU signals to add Buffer register and R1  
> 2. result of addition is returned to R1, replacing original content.
> 3. any flags from the operation are set as well


Execution flowchart:  
**What we doing** - fetch, read and decode address of op/instruction  
**What we doing it to** - generate address, fetch and read data+operand  
**DO IT** - execute instruction,  
**Send it back** - write back data if needed  
**Run it back** - update program counter and go next

### Limitations of program execution on Von Neuman systems:

- Execution of single instruction may need multiple access to memory, meaning multiple clock cycles  
- External bus speed slower than internal bus. Performance limited by bandwidth between CPU and memory **(von Neuman Bottleneck)**
- Keeping regularly used operands in CPU registaer helps reduce memory access  
- Keeping instruction and data in seperte memories **(Harvrd architecture)** can help make instructions execute in more regular cycles, improving performance


## Other architecture

Harvard:  
has 2 type of data bus.  
has 2 type of memory.

1 bus and memmory for program  
1 bus and memory for data

If instruction memory and data memory share data bus, still considered Harvard architecture - Prof Kong Peng-Yong

means can concurrently fetch next instruction and read/write from/to data memory at the same time

Harvard architecture not common since cost expensive and space expensive (more bus and memory = more wire and space)

still is useful in specific cases

## Flynn's Taxonomy

4 classifications based on:
1. number ofconcurrent instruction (or control)  
2. data streams availale in the architecture

Single instruction single data

single instruction multiple data
(carry out one operation on multiple sets of data, e.g. A+B and C+B concurrently)

Multiple instruction single data
(generally used for redundancy)
Multiple operations on same data.
2 CPU doing different things.
Can compare results between CPU

Multiple instruction Multiple data
(Multi-core processors) 
Each processor can do different operation on different set of data

### RISC and CISC

CISC: Complex Instruction Set Computer (e.g Intel processors up to Pentium)  
One instruction requiers CPU to perform multiple complex ops  

Characteristics: Complex instruction-decoding logic, driven by the need for a single instruction to support multiple addressing modes  
instructions which requier multiple clock cycles to complete

RISC: Reduced Instruction Set Computer
Characteristics: Reduced instruction set (Number of op-codes supported)  
Less complex instructions  
Hardwired control unit and machne instructions  
Few addressing schemes or modes for memory operands with 2 basic instructions (LOAD and STORE)

Now modern processors use hybrid model (CISC like model running ISC instructions)

## Program Development process

Program can be written on a completely different computer than the target system.  
E.g. code in C, compile to Assembly, Link obj with library and data with linker, Download data to target machine, execute on target system  

thus if MSP430 hang, restart computer wont help since the execution is on MSP430 processor and memory


## Instruction Set Architecture (Chpt 3)

## Low-level programming (Chpt 4-6)


# Computer Organisation

## Input / Output Techniques (Chpt 7)

## Primary Memory Subsystems (Chpt 8)

## Secondary Memory Subsystems (Chpt 9)



# Tutorials

## Tut 1

Q1a: CISC, since is 2 ops in 1 instruction   
Q1b: CISC, since is multi op in 1 instruction  
Q1c: RISC, since is 1 instruction  
Q1d: CISC, since is multi clock in 1 instruction

Q2a: SISD  
Q2b: SIMD  
Q2c: MIMD  

Q3:

Rating 1,2,3 - 1 best, 3 worst

CPU A:  
- Von Neuman  
- System cost

CPU B:  
- Harvard

CPU C:  
- Harvard

Q4a: Arch 1 since have 22 parallel busses  
Q4b: none. need 1 clock to read info, and 1 clock to store info assuming no need clock cycle to process  
Q4c: Arch 3, can read output in one cycle rather than write back to registers and read again from registers like arch 1 and 2

ANS KEY:
Q1: CISC, CISC, RISC, CISC
Q2: SISD, SIMD, MIMD
Q3:  
Q3:

Rating 1,2,3 - 1 best, 3 worst

System cost: based on num buses and separate meory spaces
Device cost: approx system cost
Ease of programming: von Neuman, no separation of memory space/unique memory address. Easier to fetch next instruction if all in same memory.
Pin count: tied to number of buses
Performance, Pure harvard is faster since instruction and data can be fetched separately in one cycle

CPU A:  
- Von Neuman  
- System cost 1=cheap: 1
- Device cost 1=cheap: 1
- Ease of programming 1=easiest: 1
- Pin count 1=lowest: 1
- performance 1=best: 2

CPU B:  
- Harvard
- System cost 1=cheap: 2
- Device cost 1=cheap: 2
- Ease of programming 1=easiest: 2
- Pin count 1=lowest: 1
- performance 1=best: 2

CPU C:  
- Harvard
- System cost 1=cheap: 3
- Device cost 1=cheap: 3
- Ease of programming 1=easiest: 2
- Pin count 1=lowest: 2
- performance 1=best: 1

Q3 Extension: Arch CPU C

Q4:
Arch 1: 2 bus to ALU, results can be sent back using both
Arch 2 one bus for all inputs and all outputs 
Arch 3: one bus for all input and output. ALU has a bus from output back to one input

4a : Arch 1
4b : None
4c : Arch 3 has dedicated bus for this but arch 1 is almost the same. Arch 2 is less effecient than both
