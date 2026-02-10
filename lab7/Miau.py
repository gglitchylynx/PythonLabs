import tkinter as tk
from tkinter import ttk
import requests
from io import BytesIO
from PIL import Image, ImageTk
import random

class SimpleCatGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор котиков")
        self.root.geometry("400x500")
        
        self.cat_urls = [
            'https://cataas.com/cat',
            'https://cataas.com/cat/cute',
            'https://cataas.com/cat/says/Meow',
            'https://cataas.com/cat/says/Hello',
            'https://cataas.com/cat/gif',
        ]
        
        self.setup_ui()
        
        self.get_new_cat()
    
    def setup_ui(self):
        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=20)
        
        self.button = ttk.Button(
            self.root,
            text="Новый котик",
            command=self.get_new_cat,
            width=20
        )
        self.button.pack(pady=10)
        
        self.status_label = tk.Label(
            self.root,
            text="Готов к работе",
            font=('Arial', 10)
        )
        self.status_label.pack(pady=5)
    
    def get_new_cat(self):
        self.status_label.config(text="Загрузка...", fg='orange')
        self.button.config(state='disabled')
        self.root.update()
        
        try:
            url = random.choice(self.cat_urls)
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                image_data = Image.open(BytesIO(response.content))
                image_data.thumbnail((350, 350), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(image_data)
                self.image_label.config(image=photo)
                self.image_label.image = photo
                
                self.status_label.config(text="Готово!", fg='green')
            else:
                self.status_label.config(text=f"Ошибка: {response.status_code}", fg='red')
                
        except Exception as e:
            self.status_label.config(text=f"Ошибка: {str(e)[:30]}...", fg='red')
        
        finally:
            self.button.config(state='normal')

def main():
    root = tk.Tk()
    app = SimpleCatGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()