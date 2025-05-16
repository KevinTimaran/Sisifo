from gui import MissileSimulationApp
import tkinter as tk

def main():
    root = tk.Tk()
    app = MissileSimulationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()