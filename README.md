# GoodOrBadSVM

## Personal Project

### Name
Good Player or Bad Player SVM Model

### Year
2019

### Overview
This project introduces a Support Vector Machine (SVM) model designed to classify online game players as "Good" or "Bad" based on their weekly time commitment to playing and learning about the game.

### Features
- **Player Classification**: Utilizes the SVM algorithm to categorize players.
- **Time Commitment Analysis**: Considers the number of hours spent playing and learning about the game as key metrics for classification.

### Functionality
By analyzing the hours dedicated by players both to playing the game and to acquiring game-related knowledge each week, the SVM model effectively distinguishes between good and bad players. This approach provides insights into how time investment correlates with player performance and skill development.

### How It Works
The SVM model takes as input the quantitative data regarding each player's weekly hours spent on gaming and learning activities. Through the application of machine learning techniques, it classifies players into two categories, offering a predictive tool to gauge player potential based on their engagement levels.

![alt text](https://github.com/filipenovais/GoodOrBadSVM/blob/master/SVM_Hyperplane.png)

- Testing the model with Python function: *goodorbad(PlayingTime, LearningTime)*

  In [1]: goodorbad(6.0,2.0)
  
  Out [1]: You're looking at a Good Player!

![alt text](https://github.com/filipenovais/GoodOrBadSVM/blob/master/SVM_Classification.png)

Credit to: https://github.com/adashofdata
