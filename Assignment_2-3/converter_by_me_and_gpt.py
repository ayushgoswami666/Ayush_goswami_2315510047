import os
import nbformat
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell
from tkinter import filedialog, Tk

def convert_py_to_ipynb(folder_path, output_path):
    notebook = new_notebook()
    notebook_cells = []

    # Sort .py files alphabetically
    py_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".py")])

    if not py_files:
        print("No .py files found in the folder.")
        return

    for file_name in py_files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
        
        # Add a markdown header and code cell
        notebook_cells.append(new_markdown_cell(f"### 🔹 File: `{file_name}`"))
        notebook_cells.append(new_code_cell(code))

    notebook.cells = notebook_cells

    # Write to .ipynb file
    with open(output_path, "w", encoding="utf-8") as f:
        nbformat.write(notebook, f)
    
    print(f"✅ Notebook saved to: {output_path}")

# GUI file picker
if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory(title="Select Folder with .py Files")
    
    if folder_selected:
        output_file = os.path.join(folder_selected, "merged_notebook.ipynb")
        convert_py_to_ipynb(folder_selected, output_file)
    else:
        print("❌ No folder selected.")
