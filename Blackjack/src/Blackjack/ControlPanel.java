package Blackjack;

import javax.swing.*;
import java.awt.*;

public class ControlPanel extends JPanel {
    private JButton hitButton;
    private JButton standButton;
    private JButton newGameButton;
    private JButton quitButton;

    public ControlPanel(BlackjackGameScreen gameScreen) {
        setLayout(new GridLayout(1, 4));

        hitButton = new JButton("Hit");
        hitButton.addActionListener(e -> gameScreen.hitButtonClicked());
        add(hitButton);

        standButton = new JButton("Stand");
        standButton.addActionListener(e -> gameScreen.standButtonClicked());
        add(standButton);

        newGameButton = new JButton("New Game");
        newGameButton.addActionListener(e -> gameScreen.startNewGame());
        add(newGameButton);

        quitButton = new JButton("Quit");
        quitButton.addActionListener(e -> gameScreen.quitGame());
        add(quitButton);
    }

    public void toggleButtons(boolean enable) {
        hitButton.setEnabled(enable);
        standButton.setEnabled(enable);
    }

    public void gameButtonMethod(boolean enable) {
        newGameButton.setEnabled(enable);
    }
}