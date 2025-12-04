"""Graphical User Interface (GUI) for RSA text encryption and decryption.

This module provides:
- A simple GUI to load text from a file, encrypt it using RSA, and decrypt it back.
- Buttons to perform actions and display results in a text area.
"""

import tkinter as tk
from tkinter.ttk import Button

from rsa_core import generate_keys
from utils import (
    chiffre_text_rsa,
    dechiffre_text_rsa,
    load_file_to_canvas,
    load_public_key,
    load_secret_key,
    save_public_key,
    save_secret_key,
)


class RsaGui:
    """Graphical interface for RSA text encryption and decryption."""

    def __init__(self) -> None:  # noqa: D107
        self.screen = tk.Tk()
        self.screen.title("RSA - Encryption / Decryption")

        # Text zone
        self.cnv = tk.Text(self.screen, width=60, height=20, bg="ivory")
        self.cnv.pack(side=tk.TOP, padx=5, pady=5)

        # Buttons
        Button(self.screen, text="Load File", command=self.load_file).pack(side=tk.LEFT, padx=5, pady=5)

        Button(self.screen, text="Encryption", command=self.encrypt).pack(side=tk.LEFT, padx=5, pady=5)

        Button(self.screen, text="Decryption", command=self.decrypt).pack(side=tk.LEFT, padx=5, pady=5)

        self.screen.resizable(width=False, height=False)

        #Variables to hold keys
        self.public_key: tuple[int, int] = None
        self.private_key: tuple[int, int] = None


    def load_file(self) -> None:
        """Load a text file into the canvas."""
        load_file_to_canvas(self.cnv)


    def get_keys(self) ->  tuple[tuple[int, int], tuple[int, int]]:
        """Load keys if available, else generate new ones."""
        if self.public_key and self.private_key:
            return self.public_key, self.private_key

        public_key = load_public_key()
        private_key = load_secret_key()

        if public_key is None or private_key is None:
            e, d, n = generate_keys(1024)

            save_public_key(e, n)
            save_secret_key(d, n)

            public_key = (e, n)
            private_key = (d, n)

        self.public_key = public_key
        self.private_key = private_key
        return public_key, private_key

    def encrypt(self) -> None:
        """Encrypt the text in the canvas using RSA."""
        public_key, _ = self.get_keys()
        e, n = public_key

        message = self.cnv.get("1.0", tk.END).rstrip("\n")

        encrypted = chiffre_text_rsa(message, e, n)

        self.cnv.delete("1.0", tk.END)

        self.cnv.insert(tk.END, " ".join(encrypted))

    def decrypt(self) -> None:
        """Decrypt the text in the canvas using RSA."""
        _, private_key = self.get_keys()
        d, n = private_key

        encrypted_text = self.cnv.get("1.0", tk.END).strip()

        decrypted_text = dechiffre_text_rsa(encrypted_text, d, n)

        self.cnv.delete("1.0", tk.END)
        self.cnv.insert(tk.END, decrypted_text)

    def run(self) -> None:
        """Run the GUI main loop."""
        self.screen.mainloop()

