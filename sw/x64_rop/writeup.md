## Titti

The challenge introduces to basic ROP chain crafting to be able to bypass canary and ASLR trough leaks, in a multi stage exploit scenario.

A quick `checksec` on the binary gives:

``` bash
 Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

### Bug

The bug is easy to spot, at line 25 a leading zero in the reading length permits a buffer overflow for the `cmd` buffer. 
```c
read(STDIN_FILENO, cmd, 0x320);
``` 

### Exploitation

We have a buffer overflow that permits us to overwrite the return address. But the problem is that in overriding the return address, we would also override the canary, which doesn't permit us to simply reach the `ret` instruction at the exit from the main loop. 

Therefore we have to leak the canary in some way. The trick is leveraging the `printf("THIS is the answer, simply %s\n", cmd);` call at line 34, under the hidden option `Beer`, that would print stack content until a null byte is found. Since to reach the function the `strncmp(cmd, "Beer", 4) == 0` check is limited to only 4 chars, without including the leading null byte, we can write more than the 4 `"Beer"` bytes to reach the canary and print it. 

So sending `“Beeraaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n“` will fill the stack until the canary, also overriding the leading zero of the canary itself, and the print call will then leak it. 

Once leaked the canary we can override the return address. Now we have two possibilities, either we craft a ROP chain, implementing `execve("/bin/sh", NULL, NULL);`, or we try to find a so called magic gadget in the standard library (https://github.com/david942j/one_gadget). A magic gadget is a location where to jump, that directly implements `execve("/bin/sh", NULL, NULL);` given some simple preconditions, like having some null bytes at far offset in the stack, that are usually met. To know how to locate a magic gadget in the libc we have to break ASLR that randomizes library location. 

We can implement a simple ROP chain to print the address of a function in the libc, and then obtain the base address subtracting the function offset in the library. 

``` python
rop = ''
rop += p64(pop_rdi_ret)
rop += p64(elf.got["puts"])
rop += p64(elf.plt["puts"])
rop += p64(elf.symbols["main"])
```

sending `"aaaa" + "a"*36 + canary + "a"*8 + rop` lets us hit the default branch and the `ret` instruction. The ROP chain simply pops the address of `puts` that is found in the GOT, and calls the `puts` function leveraging the PLT to print the address in the libc of the function itself. At the end it returns to `main` so we can keep control.

Once gathered the puts address, and identified the libc base address, the last step is identifying the magic gadget through the one_gadget tool (https://github.com/david942j/one_gadget) and returning to it, sending:

```
"aaaa" + "a"*36 + canary + "a"*8 + p64(libc.address + 0x4f2c5)
```

where 0x4f2c5 is the offset of the identified magic gadget that will pop the shell.

Full exploit [here](exploit.py)

*Writeup Author: Pietro Borrello*