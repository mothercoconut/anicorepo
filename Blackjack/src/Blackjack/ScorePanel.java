package Blackjack;

import javax.swing.*;
import java.awt.*;

public class ScorePanel extends JPanel {
    private JLabel scoreLabel;
    private JLabel gameResultLabel;

    public ScorePanel() {
        setLayout(new GridLayout(2, 1));

        scoreLabel = new JLabel();
        add(scoreLabel);

        gameResultLabel = new JLabel();
        add(gameResultLabel);
    }

    public void updateScores(int playerScore, int dealerScore) {
        scoreLabel.setText("Player: " + playerScore + " | Dealer: " + dealerScore);
    }

    public void setGameResult(String result) {
        gameResultLabel.setText(result);
    }
}