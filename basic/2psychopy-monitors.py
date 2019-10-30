# -*- coding: utf-8 -*-
"""Create Monitors.
"""
from psychopy import monitors


if __name__ == '__main__':
    # Create my primary monitor
    mon = monitors.Monitor(
        'monitor1',
        width=53.704,  # width of the monitor in cm
        distance=114,  # distance from viewer to the screen in cm
        notes="This is my primary monitor")

    mon.setSizePix((1920, 1080))  # set pixel size of the monitor
    mon.save()  # save the monitor information to disk

    # Create my second monitor
    mon = monitors.Monitor(
        'monitor2',
        width=41.6,
        distance=114,
        notes="This is my second monitor"
    )

    mon.setSizePix((1600, 900))
    mon.save()

    # Reuse my primary monitor
    mon = monitors.Monitor('monitor1')
    # Change the distance from viewer to the screen
    mon.setDistance(200)
