package Blackjack;

import basicgraphics.BasicFrame;

import javax.swing.*;
import java.awt.*;

public class BlackjackMenu extends BasicFrame {
    private JLabel titleLabel;
    private JButton playButton;
    private JButton quitButton;

    public BlackjackMenu() {
        super("Blackjack Menu");
        initComponents();
    }

    private void initComponents() {
        titleLabel = new JLabel("Blackjack");
        titleLabel.setFont(new Font("Arial", Font.BOLD, 24));
        titleLabel.setHorizontalAlignment(JLabel.CENTER);

        playButton = new JButton("Play");
        playButton.addActionListener(e -> playGame());

        quitButton = new JButton("Quit");
        quitButton.addActionListener(e -> quitGame());

        String[][] layout = {
            {"title"},
            {"play"},
            {"quit"}
        };
        setStringLayout(layout);
        add("title", titleLabel);
        add("play", playButton);
        add("quit", quitButton);
    }

    private void playGame() {
        JDialog gameDialog = new JDialog(this.jf, "Blackjack Game", true);
        gameDialog.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);

        BlackjackGameScreen gameScreen = new BlackjackGameScreen();
        gameDialog.getContentPane().add(gameScreen);

        gameDialog.pack();
        gameDialog.setLocationRelativeTo(this.jf);
        gameDialog.setVisible(true);
    }

    void quitGame() {
        System.exit(0);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            BlackjackMenu menu = new BlackjackMenu();
            menu.show();
        });
    }
}