package Blackjack;

public class userHand extends Player {
    @Override
    public String printHand() {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        for (int i = 0; i < hand.size(); i++) {
            if (i > 0) sb.append(", ");
            sb.append(hand.get(i));
        }
        sb.append("]");
        return sb.toString();
    }
}
