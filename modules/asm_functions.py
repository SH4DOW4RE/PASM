class ASMFunctions:
    def __init__(self) -> None:
        self.header = 'format ELF64 executable\n\nsegment readable executable\nentry main\n\nhex_table db "0123456789abcdef"\n\nmain:\n'
        self.var_header = 'segment readable writeable\n'
        self.var = [' db ', ', 10\n']
        self.exit = '; exit with code 0\nmov rax, 60\nmov rdi, 0\nsyscall\n\n'
        self.print_reg_function = "; ---------- Section to print a register ----------\nprint_hex16:\n;rax = value\npush rbx rax rcx rdx\nmov ecx, 16\nlea rbx, [hex_table]\n.next_nibble:\nrol rax, 4\nmov edx, eax\nand edx, 0xf\nmov dl, [rbx + rdx]\ncall print_char\ndec ecx\njnz .next_nibble\npop rdx rcx rax rbx\nret\n\nprint_char:\n;dl = character\npush rsi rdi rax rcx r11 rdx\nmov rsi, rsp\nmov edx, 1\nmov eax, 1\nmov edi, 1\nsyscall\npop rdx r11 rcx rax rdi rsi\nret\n; ------ End of Section to print a register ------\n\n"
        self.print_reg = [
            '; print register to console\nmov rax, ',
            '\ncall print_hex16\n\n'
        ]
        self.functions = {
            'print': [
                    '; print to console\nmov rax, 1\nmov rdi, 1\nmov rsi, ',
                    '\nmov rdx, ',
                    '\nsyscall\n\n'
                ],
            'epoch': '; puts epoch into rdi\nmov rax, 201\nxor rdi, rdi\nsyscall\nmov rbp, rdi\n\n'
        }
