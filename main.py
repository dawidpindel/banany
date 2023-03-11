def on_gesture_down():
    music.start_melody(music.built_in_melody(Melodies.WEDDING), MelodyOptions.ONCE)
grove.on_gesture(GroveGesture.DOWN, on_gesture_down)

def on_gesture_up():
    music.start_melody(music.built_in_melody(Melodies.DADADADUM),
        MelodyOptions.ONCE)
grove.on_gesture(GroveGesture.UP, on_gesture_up)

def on_pin_pressed_p2():
    music.ring_tone(349)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_pin_pressed_p1():
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_forever():
    pass
basic.forever(on_forever)
