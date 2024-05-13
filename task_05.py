import tkinter
import random

tk = tkinter.Tk()
c = tkinter.Canvas(tk, width=500, height=500, bg='#e6fff2')
c.pack()


class Molecule:
    x_dir = 30
    y_dir = 15

    def __init__(self, color, radius, speed):
        self.color = color
        self.radius = radius
        self.speed = speed
        x_start = random.randint(10, 450)
        y_start = x_start
        self.object = c.create_oval(x_start, y_start, radius + x_start, radius + y_start, fill=color)

    def move_molecule(self):
        x1, y1, x2, y2 = c.coords(self.object)
        if x1 <= 0 or x2 >= 500:
            Molecule.x_dir *= -1
        if y1 <= 0 or y2 >= 500:
            Molecule.y_dir *= -1

        c.move(self.object, Molecule.x_dir, Molecule.y_dir)

        c.after(self.speed, self.move_molecule)


molecule1 = Molecule('#B0C4DE', 60, 100)
molecule1.move_molecule()
molecule2 = Molecule('#B0E0E6', 50, 60)
molecule2.move_molecule()
molecule3 = Molecule('#4682B4', 40, 20)
molecule3.move_molecule()
molecule4 = Molecule('#ADD8E6', 50, 30)
molecule4.move_molecule()
molecule5 = Molecule('#87CEFA', 60, 50)
molecule5.move_molecule()
molecule6 = Molecule('#B0C4DE', 60, 100)
molecule6.move_molecule()
molecule7 = Molecule('#B0E0E6', 50, 60)
molecule7.move_molecule()
molecule8 = Molecule('#4682B4', 40, 20)
molecule8.move_molecule()
molecule9 = Molecule('#ADD8E6', 50, 30)
molecule9.move_molecule()
molecule10 = Molecule('#87CEFA', 60, 50)
molecule10.move_molecule()
molecule11 = Molecule('#B0C4DE', 60, 100)
molecule11.move_molecule()
molecule12 = Molecule('#B0E0E6', 50, 60)
molecule12.move_molecule()
molecule13 = Molecule('#4682B4', 40, 20)
molecule13.move_molecule()
molecule14 = Molecule('#ADD8E6', 50, 30)
molecule14.move_molecule()
molecule15 = Molecule('#87CEFA', 60, 50)
molecule15.move_molecule()
molecule16 = Molecule('#B0C4DE', 60, 100)
molecule16.move_molecule()
molecule17 = Molecule('#B0E0E6', 50, 60)
molecule17.move_molecule()
molecule18 = Molecule('#4682B4', 40, 20)
molecule18.move_molecule()
molecule19 = Molecule('#ADD8E6', 50, 30)
molecule19.move_molecule()
molecule20 = Molecule('#87CEFA', 60, 50)
molecule20.move_molecule()

tkinter.mainloop()


