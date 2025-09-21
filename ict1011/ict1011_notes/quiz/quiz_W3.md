### **question 1: please select all the possible length of a msp430 instruction.**

- **ans:** 2 bytes, 4 bytes, 6 bytes
- **slide 23:** this slide directly states the answer. it says, "each instruction uses an even number of bytes (2, 4, or 6)...".
- the base instruction is always 2 bytes. it can be extended to 4 or 6 bytes if it needs extra words for memory offsets or immediate values.

### **question 2: after the instruction "mov.b r9, r10" is executed, what is the value in r10 assuming that r9=0x1234 and r10=0x6789 initially?**

- **ans:** 0x0034
- **slide 29:** this slide shows a byte operation (`add.b`) where a register is the destination. it gives a specific rule: "meanwhile, the most significant byte of register r5 is set to zero;".
- applying this rule: `mov.b` is a byte operation, so it copies the least significant byte of r9 (`0x34`) into the least significant byte of r10. then, the most significant byte of r10 is cleared to `0x00`.

### **question 3: which of the following is true about the msp430 microcontroller?**

- **ans:** it has a 16-bit risc cpu.
- **slide 18:** the first point under "main characteristics" is "**16-bit risc cpu**".
- **slide 15:** the block diagram also clearly labels a "**risc cpu 16-bit**".

### **question 4: in a msp430 application, a word with value of 1234h is stored at a location 2000h. what is the value of the byte stored at address 2001h?**

- **ans:** 12h
- **slide 32:** this slide explains that the msp430 is little-endian. the rule is: "the low byte of a word is always an even address. the high byte is at the next odd address."
- for the word `1234h`, the low byte (`34h`) is stored at the low address (`2000h`), and the high byte (`12h`) is stored at the next address (`2001h`).

### **question 5: the current stack pointer is at address 1234h. after the instruction "push #1000h" is executed, what is the value of register r1?**

- **ans:** 1232h
- **slide 22 & 24:** slide 22 identifies r1 as the stack pointer (sp). slide 24 explains the stack uses a "**pre-decrement**" scheme for push operations.
- `push` defaults to a word (2 bytes). so, the sp is decremented by 2 *before* the value is stored. `1234h - 2 = 1232h`.

### **question 6: what register r0 is used for in the msp430?**

- **ans:** program counter
- **slide 22:** the diagram and the list on this slide explicitly state: "**r0 = program counter (pc)**".

### **question 7: what is the machine code for the instruction mov.b r10,r11? give your answer in hexidecimal.**

- **ans:** 0x4a4b
- **slide 42:** this uses format i for double operand instructions.
- we assemble the bits: op-code for mov is `0100` (slide 37). s-reg (r10) is `1010`. d-reg (r11) is `1011`. ad is `0` and as is `00` for register mode (slide 53). b/w is `1` for a byte op (slide 42).
- the full binary is `0100 1010 0100 1011`, which is `4a4b` in hex.

### **question 8: which of the following is true about the msp430f5529 microcontroller?**

- **ans:** it has a 16-bit data bus.
- **slide 13:** this slide states, "the msp430 has a 16-bit internal architecture, a **16-bit external data bus**."
- **slide 19:** this slide also confirms a "**16-bit data bus (mdb)**".