package Blackjack;

import java.util.Random;

public class BlackjackGame {
    private userHand playerHand;
    private dealerHand dealerHand;
    public static int dealerScore = 0;
    public static int playerScore = 0;
    public static boolean playerStand = false;
    private Random random;

    public BlackjackGame() {
        playerHand = new userHand();
        dealerHand = new dealerHand();
        random = new Random();
    }

    public void startNewGame() {
        playerHand.resetHand();
        dealerHand.resetHand();

        playerHand.addCard(generateRandomCard());
        playerHand.addCard(generateRandomCard());
        dealerHand.addCard(generateRandomCard());
        dealerHand.addCard(generateRandomCard());

        playerStand = false;
    }

    public void playerHit() {
        playerStand = false;
        playerHand.addCard(generateRandomCard());
    }

    public void playerStand() {
        playerStand = true;
        while (dealerHand.handSum() < 17) {
            dealerHand.addCard(generateRandomCard());
        }
    }

    public boolean checkGameOver() {
        return checkHand(playerHand) || checkHand(dealerHand) || (playerStand && dealerHand.handSum() > 16);
    }

    private boolean checkHand(Player hand) {
        return hand.handSum() > 21;
    }

    public String getGameResult() {
        if (checkHand(playerHand)) {
            dealerScore++;
            return checkHand(dealerHand) ? "Both players bust! House wins." : "Player busts! Dealer wins.";
        } else if (checkHand(dealerHand)) {
            playerScore++;
            return "Dealer busts! Player wins.";
        } else {
            int result = dealerHand.compare(playerHand);
            if (result == 1) {
                dealerScore++;
                return "Dealer wins!";
            } else if (result == -1) {
                playerScore++;
                return "Player wins!";
            } else {
                return "It's a tie!";
            }
        }
    }

    public userHand getPlayerHand() {
        return playerHand;
    }

    public dealerHand getDealerHand() {
        return dealerHand;
    }

    private Card generateRandomCard() {
        int value = random.nextInt(13) + 1;
        return new Card(value);
    }
}
