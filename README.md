![Banner](banner.png)

# Wack-A-Mole

A single-file whack-a-mole game: open `Wack.html` in a browser and play.
Nine holes, 30 seconds, one point per whack; the pace of the moles is
random, between half a second and a second and a half up at a time.

The high score board is optional. The page looks for Firebase
configuration supplied by its hosting environment (`__firebase_config`
and friends); when none is present, which is the case for the plain file
served on its own, the game runs the same but scores are not saved
anywhere.
