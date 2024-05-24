package Blackjack;
import java.util.ArrayList;
import java.util.List;

public abstract class Player {
    protected List<Card> hand;

    public Player() {
        hand = new ArrayList<>();
    }

    public void addCard(Card card) {
        hand.add(card);
    }

    public void resetHand() {
        hand.clear();
    }

    public int handSum() {
        int sum = 0;
        int numAces = 0;

        for (Card card : hand) {
            sum += card.getValue();
            if (card.getValue() == 11) {
                numAces++;
            }
        }

        while (sum > 21 && numAces > 0) {
            sum -= 10;
            numAces--;
        }

        return sum;
    }

    public abstract String printHand();
}
