# -*- coding: utf-8 -*-
"""A Simple Visual Window.
"""

from psychopy import visual, core

if __name__ == '__main__':
    # Create a visual window with size 800*600 on your primary screen,
    # change glfw to pyglet backend if the program crashes.
    win = visual.Window(
        size=(800, 600),
        screen=0,
        winType='glfw',
        units='height'
    )

    # Create and draw a white circle
    stim = visual.Circle(win, radius=0.1, pos=(0, 0), fillColor='white')
    stim.draw()

    # Flip the hidden buffer
    win.flip()

    # Wait 5 seconds, close the window and quit the program
    core.wait(5)
    win.close()
    core.quit()
