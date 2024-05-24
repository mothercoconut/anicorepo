This is a simple blackjack game I created, it was for an assignment/grade, however I did put in my own effort and had my own motives to complete the code and make it work properly.

The only requirement for this assignment was that it had to be loosely based on a custom basicgraphics package that was supplied to us, and there were really no other limitations.

The blackjack game runs as a standard casino would play it, howver it does not have betting nor does it allow you to split aces if you get doubles.

##BlackjackGame.java
The BlackjackGame class sets the overall methods for game 'events' such as starting a new game, when the play makes a choice, or when the game ends. 

##BlackjackGameScreen.java
The BlackjackGameScreen class configures the actuals screen layout of the blackjack game and configures button actions, borders, etc...

##BlackjackMenu.java
The menu class serves as a little 'prescreen' to the game giving you the option to play or quit, nothing more.

##Card.java
This sets up and configures how each card in the game works; it allows for face cards and aces to have a dynamic value.

##ControlPanel.java
The control panel is the setup and initialization for all of the buttons and adds methods to control the visibility of the buttons.

##dealerHand.java
The dealerHand class is a structure that defines the dealer's hand, such as only displaying the second card until the player stands, and serves a comparison class to compare the hands.

##GamePanel.java
GamePanel acts as the section in the GameScreen that displays the hand amounts for each player.

##Player.java
Player is an abstract that defines some core needs of the player's hand's abilities such as adding cards, emptying the hand, etc...

##ScorePanel.java
Score panel creates the panel at the top of the screen that displays the score of the player and dealer.

##userHand.java
Simply stores and returns the hand value as a stringbuilder string.