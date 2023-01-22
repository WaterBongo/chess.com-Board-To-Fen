# Chess.com Board Recognizer

Uses a convolutional neural network to recognize the positions of pieces and translate it into FEN format.

If you have an image of a chess.com board as chessboard.png

![Example ChessBoard](./readme/chessboard.png)

Run recognizer.py

`python3 recognizer.py chessboard.png`

The Computer will return a link to view the board, accuracy and the FEN format

`Confidence: 99.53%`

`PQpQqrbr/B1brrqrK/NN1nBrPR/NbqPKkPn/bqPBNbKN/1bBNPPnR/BbpnQKpn/bBN1BnPk`

`https://lichess.org/editor/PQpQqrbr/B1brrqrK/NN1nBrPR/NbqPKkPn/bqPBNbKN/1bBNPPnR/BbpnQKpn/bBN1BnPk`

## Sample results

Randomly generated 32 piece game

![example1](./readme/example1.png)

Predicted `2r5/PP1K1b1Q/2N1B1n1/1pkPpppp/Rp1b2P1/2PPR1N1/1PpP3p/1qr3Bn`

Confidence `97.75%`

Accuracy `100%`
