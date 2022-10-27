import os
import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color




Path = "/home/ctoic/Downloads/Fourth Semester/Algorithms/WordSearchEngine/DataFiles"
os.chdir(Path)

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

for f in os.listdir():
    if f.endswith('.txt'):
        file_path = f"{Path}/{f}"

    read_text_file(file_path)

print("\n")