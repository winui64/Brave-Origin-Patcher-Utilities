import os
import json
import tkinter as tk
from tkinter import messagebox
from pathlib import Path

BASE_DIR_NAMES = [
    "brave-origin",
    "brave-origin-beta",
    "brave-origin-nightly",
]

def patch_brave_origin_for_base(base_dir_name):
    # macOS path: ~/Library/Application Support/BraveSoftware/
    home = Path.home()
    base = home / "Library" / "Application Support" / "BraveSoftware" / base_dir_name / "User Data"
    
    state_file = base / "Local State"

    if not state_file.exists():
        return False, f"Local State file not found at {state_file}"

    try:
        data = json.loads(state_file.read_text(encoding="utf-8"))
    except Exception as e:
        return False, f"Failed to read JSON: {e}"

    # Update brave.origin
    brave_cfg = data.get("brave", {})
    brave_cfg["origin"] = {"purchase_validated": True}
    data["brave"] = brave_cfg

    # Update skus
    sku_payload = {
        "credentials": {
            "items": {
                "dobrylicka": "1"
            }
        }
    }
    data["skus"] = {
        "state": {
            "1": json.dumps(sku_payload, separators=(",", ":"))
        }
    }

    try:
        state_file.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    except Exception as e:
        return False, f"Failed to save file: {e}"

    return True, "Done"

def run_patch(selected_bases, output_widget):
    output_widget.delete("1.0", tk.END)
    any_selected = False
    for base_name, var in selected_bases.items():
        if var.get():
            any_selected = True
            success, msg = patch_brave_origin_for_base(base_name)
            status = "SUCCESS" if success else "FAIL"
            output_widget.insert(tk.END, f"{base_name}: {status} - {msg}\n")
    if not any_selected:
        messagebox.showinfo("No selection", "Please select at least one base to patch.")

def create_gui():
    root = tk.Tk()
    root.title("Patch Brave Origin (macOS)")

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(fill="both", expand=True)

    tk.Label(frame, text="Select which version of Brave Origin you wish to patch:").pack(anchor="w")

    selected_vars = {}
    for name in BASE_DIR_NAMES:
        var = tk.BooleanVar(value=False)
        cb = tk.Checkbutton(frame, text=name, variable=var)
        cb.pack(anchor="w")
        selected_vars[name] = var

    btn_frame = tk.Frame(frame, pady=8)
    btn_frame.pack(fill="x")

    output = tk.Text(frame, height=8, width=60)
    output.pack(fill="both", expand=True)

    run_btn = tk.Button(btn_frame, text="Patch Selected", command=lambda: run_patch(selected_vars, output))
    run_btn.pack(side="left")

    close_btn = tk.Button(btn_frame, text="Close", command=root.destroy)
    close_btn.pack(side="right")

    root.mainloop()

if __name__ == "__main__":
    create_gui()
