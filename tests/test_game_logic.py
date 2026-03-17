# from logic_utils import check_guess

# def test_winning_guess():
#     # If the secret is 50 and guess is 50, it should be a win
#     result = check_guess(50, 50)
#     assert result == "Win"

# def test_guess_too_high():
#     # If secret is 50 and guess is 60, hint should be "Too High"
#     result = check_guess(60, 50)
#     assert result == "Too High"

# def test_guess_too_low():
#     # If secret is 50 and guess is 40, hint should be "Too Low"
#     result = check_guess(40, 50)
#     assert result == "Too Low"
# tests/test_game_logic.py

import pytest
from logic_utils import check_guess

# ---------------------------
# Original tests (fixed tuple)
# ---------------------------

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

# ---------------------------------
# New test: simulate attempt counting
# ---------------------------------

def test_attempt_limit_behavior():
    """
    Simulate a small game with a fixed attempt limit.
    We check that after 'attempt_limit' guesses, the attempts
    counter matches the limit and no extra guesses would be allowed.
    """
    secret = 10
    attempt_limit = 3
    attempts = 0
    history = []

    # Make 3 guesses
    for guess in [1, 5, 10]:
        outcome, message = check_guess(guess, secret)
        history.append(guess)
        attempts += 1
        if attempts >= attempt_limit:
            status = "lost" if guess != secret else "won"
            break
        else:
            status = "playing"

    assert attempts == attempt_limit
    assert len(history) == attempt_limit
    # Last guess should win the game here
    assert status == "won"
