![Intro scenery: the wooden mallet landed at the left of the green fairground board as one plush mole drops flat back into its hole in the foreground and the next mole just begins to rise two holes away, gold prize ribbons hanging at the stall posts](intro-banner.png)

# Wack-A-Mole

![Wordmark banner: a fairground whack game board with nine green holes rimmed in red, two plush brown moles up and the rest down, a wooden mallet caught mid swing over the board and gold prize ribbons hanging at the stall posts](banner.png)

<p align="center"><img src="logo.png" alt="Wack-A-Mole logo: one round brown plush mole popping out of a red rimmed hole in a green fairground game board, its paws on the rim and a wooden mallet raised above it" width="200"></p>

![Animated scene: steam over the bowls, a spoon gliding bowl to bowl, one pale bean lifted to the rejected pile](scene.svg)



A single-file whack-a-mole game: open `Wack.html` in a browser and play.
Nine holes, 30 seconds, one point per whack; the pace of the moles is
random, between half a second and a second and a half up at a time.

![Separator](sep-light.svg)

> The animal shown is a hedgehog, chosen because it reads well at that size, while the class name in the code stayed mole. Scripted clicks are refused, because the game checks that each click came from a real press.

The high score board is optional. The page looks for Firebase
configuration supplied by its hosting environment (`__firebase_config`
and friends); when none is present, which is the case for the plain file
served on its own, the game runs the same but scores are not saved
anywhere.

![Separator](sep-heavy.svg)

> The score board is conditional. Scores are saved only when Firebase configuration, sign in, and the database are all present, and only the best score per player is kept.
