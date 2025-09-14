### **Q1: desktop with i7 intel processor in flynn's taxonomy?**

- **ans:** mimd (multiple instruction, multiple data)
- **slide 53:** mimd = multiple instructions on multiple data at same time. i7 is multi-core = mimd

### **Q2: word = 1234h at 3000h in msp430 (little endian). byte at 3000h?**

- **ans:** 34h
- **slide 16:** little endian = LSB at lowest addr. 1234h: '34' is LSB at 3000h, '12' at 3001h

### **Q3: cpu with 16-bit addr bus means?**

- **ans:** max mem size = 65536 bytes
- **slide 15 & 38:** mem size = 2^n bytes (n=addr lines). 16-bit = 2^16 = 65536 addr

### **Q4: 16-bit cpu means?**

- **ans:** can compute 16-bit nums at once
- **slide 38:** cpu bit width = internal bus width = bits processed per cycle. 16-bit = 16 bits/cycle

### **Q5: cpu repeatedly performs which ops?**

- **ans:** fetch, decode, execute
- **slide 23 & 44:** cpu does fetch-decode-execute cycle over & over

### **Q6: rank memory by speed (1=fastest, 4=slowest)**

- **ans:**
  1.  reg
  2.  cache
  3.  main mem
  4.  secondary mem
- **slide 14:** mem hierarchy (fast to slow): reg > cache > main mem > secondary mem

### **Q7: cpu with 16-bit data bus means?**

- **ans:** can transfer 16 bits to main mem in 1 cycle
- **slide 38:** data bus width = bits transferred per cycle. 16-bit bus = 16 bits/cycle
