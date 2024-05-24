package Blackjack;

import javax.swing.*;
import java.awt.*;

public class GamePanel extends JPanel {
    private JLabel playerHandLabel;
    private JLabel dealerHandLabel;
    private JLabel playerHandValueLabel;
    private JLabel dealerHandValueLabel;

    public GamePanel() {
        setLayout(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();

        playerHandLabel = new JLabel();
        gbc.gridx = 0;
        gbc.gridy = 0;
        add(playerHandLabel, gbc);

        playerHandValueLabel = new JLabel();
        gbc.gridx = 1;
        add(playerHandValueLabel, gbc);

        dealerHandLabel = new JLabel();
        gbc.gridx = 0;
        gbc.gridy = 1;
        add(dealerHandLabel, gbc);

        dealerHandValueLabel = new JLabel();
        gbc.gridx = 1;
        add(dealerHandValueLabel, gbc);
    }

    public void updateDisplay(BlackjackGame game) {
        playerHandLabel.setText("Player: " + game.getPlayerHand().printHand());
        playerHandValueLabel.setText("(" + game.getPlayerHand().handSum() + ")");
        dealerHandLabel.setText("Dealer: " + game.getDealerHand().printHand());
        if (game.getDealerHand().handSum() <= 21) {
            dealerHandValueLabel.setText("(" + game.getDealerHand().handSum() + ")");
        } else {
            dealerHandValueLabel.setText("(Bust)");
        }
    }
}