# Tic-Tac-Toe Implementation Plan

## Context
`tic_tac_toe.py` has 7 skeleton functions (`print_board`, `choose_player`, `ask_move`,
`check_winner`, `check_draw`, `switch_player`, `main`) that all `pass`. `pseudocode.md`
describes the intended game, including a "play again?" loop. The goal is a working
2-player command-line game, built in 5 stages, one stage at a time, with a review stop
after each stage.

**Rules for all code**
- Keep the existing function names and signatures.
- Every function has a docstring.
- Each function body is 4–10 lines (docstring not counted).
- Beginner-friendly Python: lists, `for`/`while`, `if`, f-strings, `input()`. No classes,
  no `try/except` tricks, no imports needed.
- Leave the `if __name__ == "__main__":` block as it is.

**Design decisions**
- Board = a list of 9 strings, `" "` means empty. Squares are numbered 1–9 for the player
  (index = number − 1).
- Small helper functions are added (new names, needed to keep `main` under 10 lines):
  `create_board()`, `play_game()`, `game_over(board, player)`, `play_turn(board, player)` (added in Stage 3 to keep `play_game` short).
- `WINNING_LINES` = a module-level list of the 8 index triples.

Final layout of the file (top to bottom): `WINNING_LINES`, `create_board`, `print_board`,
`choose_player`, `ask_move`, `check_winner`, `check_draw`, `switch_player`, `game_over`,
`play_game`, `main`.

---

## Stage 1 — Board + display (✅ done)
- `create_board()` → returns `[" "] * 9`.
- `print_board(board)` → loops over 3 rows, prints `" X | O |  "` with a
  `"---+---+---"` separator between rows.
- `main()` (temporary) → prints a welcome line, shows a square-number guide by reusing
  `print_board([str(n) for n in range(1, 10)])`, then prints an empty board.

**Check:** `uv run python tic_tac_toe.py` shows the numbered guide and an empty grid.

## Stage 2 — Turn-taking (✅ done, plus q to quit)
- `choose_player()` → `input("Player 1, choose X or O: ").upper()` and return it
  (no validation yet).
- `ask_move(board, player)` → asks `"Player X, choose a square (1-9): "`, converts to
  `int`, writes `player` into `board[move - 1]` (no validation yet).
- `switch_player(player)` → returns `"O"` if player is `"X"`, else `"X"`.
- `play_game()` → create board, show guide/board, choose player, then loop:
  ask move → print board → switch player (temporarily `for` 9 turns so it ends).
- `main()` → calls `play_game()`.

**Check:** two players can alternate placing X and O on the board.

## Stage 3 — Win detection (✅ done)
- Add `WINNING_LINES` (3 rows, 3 columns, 2 diagonals).
- `check_winner(board)` → for each line, if all three squares are the same and not `" "`,
  return `True`; after the loop return `False` (uses `all()` as the assignment suggests,
  or a simple `==` chain).
- `game_over(board, player)` → if `check_winner` → print `"Player X wins!"`, return `True`;
  otherwise return `False`.
- `play_game()` → switch to `while True`; after each move, `break` if `game_over(...)`.

**Check:** play a row, a column and a diagonal — each ends the game with the right winner.

## Stage 4 — Draw detection + play again (✅ done)
- `check_draw(board)` → return `" " not in board` (written as a short loop/if for
  readability if preferred, staying within 4–10 lines).
- `game_over()` → also checks `check_draw` and prints `"It's a draw!"`.
  Winner is checked first, so a full board with a winner counts as a win.
- `main()` → loop: `play_game()`, then ask `"Play again? (y/n): "`; stop unless `"y"`
  (matches step 7 of the pseudocode).

**Check:** fill the board with no winner → "It's a draw!"; answer `y` starts a fresh
board, `n` exits.

## Stage 5 — Input validation (✅ done early, together with Stage 2)
- `choose_player()` → `while True` loop: strip + upper the input; return it if it is
  `"X"` or `"O"`, otherwise print `"Invalid input, please type X or O"`.
- `ask_move()` → `while True` loop following pseudocode step 3:
  - not a digit or not 1–9 → `"Please enter a number from 1 to 9"`
  - square already taken → `"That square is taken, choose another"`
  - else place the symbol and `return`.
  Uses `move.isdigit()` instead of `try/except` to stay beginner-friendly.

**Check:** type `a`, `0`, `10`, empty input and an occupied square — each re-prompts
without crashing; `x` (lowercase) is accepted for player choice.

---

## Process
1. On approval: copy this plan into the repo as `PLAN.md`, then implement **Stage 1 only**.
2. Run `uv run python tic_tac_toe.py` to verify, then stop and wait for review.
3. Repeat for stages 2–5, one at a time, each only after the previous is approved.
4. No commits unless asked.

## Verification (end-to-end, after stage 5)
`uv run python tic_tac_toe.py` and play: a row win, a column win, a diagonal win, a draw,
invalid inputs, and the play-again prompt. Also confirm every function has a docstring
and a 4–10 line body.
