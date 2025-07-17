import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from ciphers.caesar import CaesarCipher
from ciphers.vigenere import VigenereCipher
from ciphers.playfair import PlayfairCipher
from ciphers.substitution import SubstitutionCipher
from ciphers.hill import HillCipher
from ciphers import InvalidKeyError
import numpy as np

CIPHERS = {
    'Caesar': CaesarCipher(),
    'Vigenère': VigenereCipher(),
    'Playfair': PlayfairCipher(),
    'Substitution': SubstitutionCipher(),
    'Hill': HillCipher(),
}

KEY_HINTS = {
    'Caesar': 'Integer (e.g., 3)',
    'Vigenère': 'Alphabetic (e.g., key)',
    'Playfair': 'Alphabetic (e.g., keyword)',
    'Substitution': '26-letter mapping (e.g., QWERTY...)',
    'Hill': 'Perfect square length (e.g., 4, 9, 16) alphabetic',
}

BG_COLOR = '#232946'
HEADER_COLOR = '#121629'
ACCENT_COLOR = '#eebbc3'
TEXT_COLOR = '#fffffe'
ENTRY_BG = '#393d5b'
BTN_COLOR = '#eebbc3'
BTN_TEXT = '#232946'
FONT = ('Segoe UI', 12)
HEADER_FONT = ('Segoe UI', 18, 'bold')
HIST_FONT = ('Segoe UI', 10)

class CipherGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Classical Ciphers Explorer')
        self.geometry('900x540')
        self.resizable(False, False)
        self.configure(bg=BG_COLOR)
        self.history = []
        self.create_widgets()

    def create_widgets(self):
        # Header
        header = tk.Frame(self, bg=HEADER_COLOR, height=60)
        header.pack(fill='x')
        tk.Label(header, text='Classical Ciphers Explorer', bg=HEADER_COLOR, fg=ACCENT_COLOR, font=HEADER_FONT, pady=10).pack()

        # Main content frame
        main = tk.Frame(self, bg=BG_COLOR)
        main.pack(side='left', fill='both', expand=True, padx=30, pady=20)

        # Cipher selection
        tk.Label(main, text='Cipher:', bg=BG_COLOR, fg=TEXT_COLOR, font=FONT).grid(row=0, column=0, sticky='w', pady=(0, 10))
        self.cipher_var = tk.StringVar(value='Caesar')
        cipher_menu = ttk.Combobox(main, textvariable=self.cipher_var, values=list(CIPHERS.keys()), state='readonly', font=FONT, width=18)
        cipher_menu.grid(row=0, column=1, sticky='w', pady=(0, 10))
        cipher_menu.bind('<<ComboboxSelected>>', self.update_key_hint_and_visual)

        # Mode selection (custom highlight)
        self.mode_var = tk.StringVar(value='Encrypt')
        mode_frame = tk.Frame(main, bg=BG_COLOR)
        mode_frame.grid(row=1, column=0, columnspan=2, pady=(0, 10), sticky='w')
        self.encrypt_btn = tk.Label(mode_frame, text='Encrypt', font=FONT, bg=ACCENT_COLOR, fg=BTN_TEXT, bd=2, relief='solid', padx=18, pady=4, cursor='hand2')
        self.decrypt_btn = tk.Label(mode_frame, text='Decrypt', font=FONT, bg=BG_COLOR, fg=TEXT_COLOR, bd=2, relief='solid', padx=18, pady=4, cursor='hand2')
        self.encrypt_btn.pack(side='left', padx=10)
        self.decrypt_btn.pack(side='left', padx=10)
        self.encrypt_btn.bind('<Button-1>', lambda e: self.set_mode('Encrypt'))
        self.decrypt_btn.bind('<Button-1>', lambda e: self.set_mode('Decrypt'))
        self.update_mode_buttons()

        # Text input
        tk.Label(main, text='Text:', bg=BG_COLOR, fg=TEXT_COLOR, font=FONT).grid(row=2, column=0, sticky='nw')
        self.text_entry = tk.Text(main, height=4, width=40, bg=ENTRY_BG, fg=TEXT_COLOR, font=FONT, insertbackground=ACCENT_COLOR, bd=0, relief='flat')
        self.text_entry.grid(row=2, column=1, pady=5, sticky='w')
        tk.Button(main, text='Load from File', command=self.load_text_file, bg=BTN_COLOR, fg=BTN_TEXT, font=('Segoe UI', 10), bd=0, relief='flat', padx=10, pady=2, cursor='hand2').grid(row=2, column=2, padx=10)

        # Key input
        tk.Label(main, text='Key:', bg=BG_COLOR, fg=TEXT_COLOR, font=FONT).grid(row=3, column=0, sticky='w')
        self.key_entry = tk.Entry(main, width=30, bg=ENTRY_BG, fg=TEXT_COLOR, font=FONT, insertbackground=ACCENT_COLOR, bd=0, relief='flat')
        self.key_entry.grid(row=3, column=1, pady=5, sticky='w')
        self.key_hint_var = tk.StringVar(value=KEY_HINTS['Caesar'])
        tk.Label(main, textvariable=self.key_hint_var, bg=BG_COLOR, fg=ACCENT_COLOR, font=('Segoe UI', 10, 'italic')).grid(row=4, column=1, sticky='w')

        # Action button
        self.action_btn = tk.Button(main, text='Run', command=self.run_cipher_action, bg=BTN_COLOR, fg=BTN_TEXT, font=FONT, activebackground=ACCENT_COLOR, activeforeground=BTN_TEXT, bd=0, relief='flat', padx=20, pady=5, cursor='hand2')
        self.action_btn.grid(row=5, column=0, columnspan=2, pady=20)

        # Output
        tk.Label(main, text='Result:', bg=BG_COLOR, fg=TEXT_COLOR, font=FONT).grid(row=6, column=0, sticky='nw')
        self.result_text = tk.Text(main, height=4, width=40, bg=ENTRY_BG, fg=ACCENT_COLOR, font=FONT, state='disabled', bd=0, relief='flat')
        self.result_text.grid(row=6, column=1, pady=5, sticky='w')
        tk.Button(main, text='Copy to Clipboard', command=self.copy_result, bg=BTN_COLOR, fg=BTN_TEXT, font=('Segoe UI', 10), bd=0, relief='flat', padx=10, pady=2, cursor='hand2').grid(row=6, column=2, padx=10)
        tk.Button(main, text='Save Result to File', command=self.save_result_file, bg=BTN_COLOR, fg=BTN_TEXT, font=('Segoe UI', 10), bd=0, relief='flat', padx=10, pady=2, cursor='hand2').grid(row=7, column=2, padx=10)

        # Visualization panel
        self.visual_panel = tk.Frame(main, bg=BG_COLOR, bd=1, relief='flat')
        self.visual_panel.grid(row=7, column=1, pady=10, sticky='w')
        self.visual_label = tk.Label(self.visual_panel, text='', bg=BG_COLOR, fg=ACCENT_COLOR, font=('Segoe UI', 11, 'bold'))
        self.visual_label.pack()
        self.visual_matrix = tk.Text(self.visual_panel, height=7, width=30, bg=BG_COLOR, fg=TEXT_COLOR, font=('Consolas', 12), bd=0, relief='flat', state='disabled')
        self.visual_matrix.pack()

        # History panel
        hist_frame = tk.Frame(self, bg=BG_COLOR, bd=1, relief='flat')
        hist_frame.pack(side='right', fill='y', padx=(0, 10), pady=20)
        tk.Label(hist_frame, text='History', bg=BG_COLOR, fg=ACCENT_COLOR, font=('Segoe UI', 13, 'bold')).pack(pady=(0, 5))
        self.history_list = tk.Listbox(hist_frame, width=40, height=25, font=HIST_FONT, bg=ENTRY_BG, fg=TEXT_COLOR, bd=0, relief='flat', selectbackground=ACCENT_COLOR, selectforeground=BTN_TEXT)
        self.history_list.pack(fill='y', expand=True)

    def set_mode(self, mode):
        self.mode_var.set(mode)
        self.update_mode_buttons()

    def update_mode_buttons(self):
        if self.mode_var.get() == 'Encrypt':
            self.encrypt_btn.config(bg=ACCENT_COLOR, fg=BTN_TEXT, bd=3, relief='solid')
            self.decrypt_btn.config(bg=BG_COLOR, fg=TEXT_COLOR, bd=2, relief='solid')
        else:
            self.encrypt_btn.config(bg=BG_COLOR, fg=TEXT_COLOR, bd=2, relief='solid')
            self.decrypt_btn.config(bg=ACCENT_COLOR, fg=BTN_TEXT, bd=3, relief='solid')

    def update_key_hint_and_visual(self, event=None):
        cipher = self.cipher_var.get()
        self.key_hint_var.set(KEY_HINTS.get(cipher, ''))
        self.update_visualization()

    def run_cipher_action(self):
        cipher = self.cipher_var.get()
        mode = self.mode_var.get()
        text = self.text_entry.get('1.0', 'end').strip()
        key = self.key_entry.get().strip()
        if not text:
            messagebox.showwarning('Input Required', 'Please enter text to process.')
            return
        if not key:
            messagebox.showwarning('Key Required', 'Please enter a key.')
            return
        result = self.run_cipher(cipher, mode, text, key)
        self.result_text.config(state='normal')
        self.result_text.delete('1.0', 'end')
        self.result_text.insert('1.0', result)
        self.result_text.config(state='disabled')
        self.add_history(cipher, mode, text, key, result)
        self.update_visualization()

    def run_cipher(self, cipher_name, mode, text, key):
        cipher = CIPHERS[cipher_name]
        try:
            if mode == 'Encrypt':
                return cipher.encrypt(text, key)
            else:
                return cipher.decrypt(text, key)
        except InvalidKeyError as e:
            messagebox.showerror('Invalid Key', str(e))
            return ''
        except Exception as e:
            messagebox.showerror('Error', str(e))
            return ''

    def copy_result(self):
        result = self.result_text.get('1.0', 'end').strip()
        if result:
            self.clipboard_clear()
            self.clipboard_append(result)
            messagebox.showinfo('Copied', 'Result copied to clipboard!')

    def load_text_file(self):
        path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
        if path:
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.text_entry.delete('1.0', 'end')
                self.text_entry.insert('1.0', content)
            except Exception as e:
                messagebox.showerror('File Error', f'Could not read file: {e}')

    def save_result_file(self):
        result = self.result_text.get('1.0', 'end').strip()
        if not result:
            messagebox.showwarning('No Result', 'No result to save.')
            return
        path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
        if path:
            try:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(result)
                messagebox.showinfo('Saved', 'Result saved to file!')
            except Exception as e:
                messagebox.showerror('File Error', f'Could not save file: {e}')

    def add_history(self, cipher, mode, text, key, result):
        entry = f'{cipher} | {mode} | Text: {text[:20]}... | Key: {key} | Result: {result[:20]}...'
        self.history.insert(0, (cipher, mode, text, key, result))
        self.history_list.insert(0, entry)
        if self.history_list.size() > 50:
            self.history_list.delete(50, 'end')
            self.history = self.history[:50]

    def update_visualization(self):
        cipher = self.cipher_var.get()
        key = self.key_entry.get().strip()
        self.visual_label.config(text='')
        self.visual_matrix.config(state='normal')
        self.visual_matrix.delete('1.0', 'end')
        if cipher == 'Playfair' and key:
            try:
                pf = CIPHERS['Playfair']
                square = pf._generate_square(key)
                self.visual_label.config(text='Playfair 5x5 Grid:')
                grid_str = '\n'.join(' '.join(row) for row in square)
                self.visual_matrix.insert('1.0', grid_str)
            except Exception:
                self.visual_label.config(text='Invalid key for Playfair grid.')
        elif cipher == 'Hill' and key:
            try:
                hc = CIPHERS['Hill']
                matrix = hc._key_to_matrix(key)
                self.visual_label.config(text=f'Hill Matrix ({matrix.shape[0]}x{matrix.shape[1]}):')
                mat_str = '\n'.join(' '.join(f'{int(num):2d}' for num in row) for row in matrix)
                self.visual_matrix.insert('1.0', mat_str)
            except Exception:
                self.visual_label.config(text='Invalid key for Hill matrix.')
        self.visual_matrix.config(state='disabled')

if __name__ == '__main__':
    app = CipherGUI()
    app.mainloop()