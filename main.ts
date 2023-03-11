grove.onGesture(GroveGesture.Down, function on_gesture_down() {
    music.startMelody(music.builtInMelody(Melodies.Wedding), MelodyOptions.Once)
})
grove.onGesture(GroveGesture.Up, function on_gesture_up() {
    music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
})
input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    music.ringTone(349)
})
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    music.playTone(262, music.beat(BeatFraction.Whole))
})
basic.forever(function on_forever() {
    
})
