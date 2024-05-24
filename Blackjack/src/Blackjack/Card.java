package Blackjack;

public class Card {
    private int value;

    public Card(int value) {
        this.value = value;
    }

    public int getValue() {
        if (value > 10) {
            return 10;
        } else if (value == 1) {
            return 11;
        } else {
            return value;
        }
    }

    @Override
    public String toString() {
        return switch (value) {
            case 1 -> "A";
            case 11 -> "J";
            case 12 -> "Q";
            case 13 -> "K";
            default -> String.valueOf(value);
        };
    }
}