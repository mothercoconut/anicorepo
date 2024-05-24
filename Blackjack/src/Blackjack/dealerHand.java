package Blackjack;

public class dealerHand extends Player {
    private boolean hideFirstCard;

    public dealerHand() {
        hideFirstCard = true;
    }

    @Override
    public String printHand() {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        if (hideFirstCard) {
            sb.append("X, ");
            sb.append(hand.get(1));
        } else {
            for (int i = 0; i < hand.size(); i++) {
                if (i > 0) sb.append(", ");
                sb.append(hand.get(i));
            }
        }
        sb.append("]");
        return sb.toString();
    }

    public int compare(userHand playerHand) {
        int dealerSum = handSum();
        int playerSum = playerHand.handSum();

        if (dealerSum > 21 && playerSum > 21) {
            return 0; // Both hands bust, tie
        } else if (dealerSum > 21) {
            return -1; // Dealer busts, player wins
        } else if (playerSum > 21) {
            return 1; // Player busts, dealer wins
        } else if (dealerSum > playerSum) {
            return 1; // Dealer has higher sum, dealer wins
        } else if (playerSum > dealerSum) {
            return -1; // Player has higher sum, player wins
        } else {
            return 0; // Sums are equal, tie
        }
    }

    public void revealFirstCard() {
        hideFirstCard = false;
    }
}