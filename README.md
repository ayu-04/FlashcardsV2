# Flashcard app

Flashcard app is an application used for testing and improving memory through practiced information retrieval. Flashcards are typically two-sided, with the prompt on one side and the information about the prompt on the other.

## Run the app

To run the backend install all the dependencies and run main.py
To run the frontend run the following command - $npm run serve

## Usage

You will see a login page.

If you are running this application for the first time you will want to sign up.
To do so click on the 'Sign up' button. You will be redirected to a sign up page.
Enter desired email id, username and password-there are no character limits or restrictions.
Click on 'OK'.

If you already have an account enter your username and password. Click 'OK'.

You will be redirected to your dashboard.

## Dashboard

Every new account will, by default, have 3 decks of Spanish-English cards named 'SPANISH 1', 'SPANISH 2' and 'SPANISH 3'. These will be available in the 'Try something new' section.

Once you play a deck, that deck will appear under the 'Play again' section with your recent score for that deck and last played time.

### Play a deck

To play a deck, click on the title of the deck.
You will be redirected to a card page.

The question will appear in the main section.

To see the answer, move the pointer over the card. The card will filp on-hover.

The back of the card will reveal the answer and give you options about the correctness of your answer. Select the appropriate option based on how difficult you found the card. The score will be updated accordingly.

+10 for easy

+5 for medium

+3 for hard

+0 for incorrect

You can see your updated score on the left.

To go to the next card, click on 'Next'.

Clicking on 'Retry' will redirect you to the first card and reset your score to 0.

Clicking on 'Exit' will redirect you to the dashboard and save the score for the cards you have attempted so far.

If you finish playing the deck you will be redirected to the gameover page which will show your total score for the deck.

### Logout

The Logout button is on the top right corner of the dashboard.

### Create a deck

Apart from the default decks, you can also create your own deck. To do this click on the 'Create a deck' button on the right in the dashboard.

This will redirect you to a form asking you the title of the deck and number of cards in the deck. A user cannot have multiple decks with the same title.Click on 'Create'.

Next enter the question and answer pairs you want in your deck one by one. The counter on the top right corner will show you the number of cards left.

### Delete a deck

To delete a deck, click on the 'Delete a deck' button on the right in the dashboard.

This will redirect you to a list of all the decks you own.

Select the deck you want to delete.

### Edit a deck

To edit a deck click on the 'Edit a deck' button on the right in the dashboard.

This will redirect you to a list of all the decks you own.

Click on the deck you want to edit. You will be redirected to a list of all the cards in that deck. Below each card is an 'Update' and a 'Delete' button. Clicking on 'Update' will show you form to edit the card. Clicking on 'Delete'
will delete the card form the deck.

You can also add more cards to the deck by clicking the 'Add card' button on the top of the page.

### Export a deck

You can also download a deck as a csv file with 'question, answer' in each line. To do this click on the 'Export a deck' button on the right in the dashboard.

This will redirect you to a list of all the decks you own.

Click on the deck you want to export. You will get an alert saying that your deck has been exported.

## Scheduled jobs

### Email reminder

In addition to being able to play, create, update, delete and export decks, you will also receive email reminders everyday at 3 PM if you have not played any deck that day.

### Email report

This app will also mail to you a report on the 30th of every month. This report will contain the titles, scores, and, performance of the decks you've played. It will also list the titles of the decks you haven't played.