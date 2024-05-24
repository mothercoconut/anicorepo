package Blackjack;

import javax.swing.*;
import java.awt.*;

public class BlackjackGameScreen extends JPanel {
    private BlackjackGame game;
    private GamePanel gamePanel;
    private ControlPanel controlPanel;
    private ScorePanel scorePanel;

    public BlackjackGameScreen() {
        game = new BlackjackGame();
        initComponents();
        startNewGame();
    }

    private void initComponents() {
        setLayout(new BorderLayout());

        gamePanel = new GamePanel();
        add(gamePanel, BorderLayout.CENTER);

        controlPanel = new ControlPanel(this);
        add(controlPanel, BorderLayout.SOUTH);

        scorePanel = new ScorePanel();
        add(scorePanel, BorderLayout.NORTH);

        setPreferredSize(new Dimension(400, 300));
    }

    public void startNewGame() {
        game.startNewGame();
        controlPanel.gameButtonMethod(false);
        controlPanel.toggleButtons(true);
        scorePanel.setGameResult("");
        updateDisplay();
    }

    public void hitButtonClicked() {
        game.playerHit();
        if (game.checkGameOver()) {
            endGame();
        }
        updateDisplay();
    }

    public void standButtonClicked() {
        controlPanel.toggleButtons(false);
        game.getDealerHand().revealFirstCard();
        game.playerStand();
        updateDisplay();
        if (game.checkGameOver()) {
            endGame();
        }
    }

    private void endGame() {
        controlPanel.gameButtonMethod(true);
        controlPanel.toggleButtons(false);
        game.getDealerHand().revealFirstCard();
        scorePanel.setGameResult(game.getGameResult());
        updateDisplay();
    }

    public void quitGame() {
        System.exit(0);
    }

    private void updateDisplay() {
        gamePanel.updateDisplay(game);
        scorePanel.updateScores(BlackjackGame.playerScore, BlackjackGame.dealerScore);
    }
}