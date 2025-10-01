define f = Character("Faye", color="#e24034")

image faye small:
    "faye.png"
    zoom 0.75
    yalign 0.21

image bg small:
    "smol light bg.png"
    zoom 1.5
    yalign 0.55

label start:

    scene bg small

    show faye small

    f "e"

    return
