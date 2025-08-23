#!/usr/bin/env python3
"""
Dice Rolling Simulator
- Enter dice like: d6, 2d6, 3d20, 4d8, etc.
- Press Enter for a default roll of d6.
- Commands:
    stats   -> show average and history
    clear   -> clear history
    help    -> show help
    quit/q  -> exit
"""

import random
import re
import time

DICE_RE = re.compile(r"^\s*(\d*)\s*[dD]\s*(\d+)\s*$")

history = []  # store (notation, rolls_list, total)

def parse_dice(s: str):
    if not s.strip():
        return 1, 6  # default: 1d6
    m = DICE_RE.match(s)
    if not m:
        raise ValueError("Invalid format. Use NdS like 2d6 or d20.")
    n = int(m.group(1)) if m.group(1) else 1
    sides = int(m.group(2))
    if n < 1 or sides < 2 or n > 1000 or sides > 1000000:
        raise ValueError("Out of range. 1–1000 dice, each with 2–1,000,000 sides.")
    return n, sides

def roll_dice(n: int, sides: int):
    return [random.randint(1, sides) for _ in range(n)]

def show_help():
    print(__doc__)

def show_stats():
    if not history:
        print("No rolls yet.")
        return
    totals = [t for _, _, t in history]
    avg = sum(totals) / len(totals)
    print(f"\n--- Stats ---")
    print(f"Rolls: {len(totals)}  |  Average total: {avg:.2f}")
    print("Last 10 rolls:")
    for notation, rolls, total in history[-10:]:
        print(f"{notation:>6}: {rolls}  =>  {total}")
    print("-------------\n")

def main():
    print("🎲 Dice Rolling Simulator — type 'help' for commands.")
    while True:
        try:
            user = input("Roll (e.g., 2d6, d20) > ").strip().lower()
            if user in ("q", "quit", "exit"):
                print("Goodbye!")
                break
            if user in ("help", "?"):
                show_help()
                continue
            if user == "stats":
                show_stats()
                continue
            if user == "clear":
                history.clear()
                print("History cleared.")
                continue

            n, sides = parse_dice(user)
            notation = f"{n}d{sides}"
            print(f"Rolling {notation} ...")
            time.sleep(0.1)  # tiny pause for feel
            rolls = roll_dice(n, sides)
            total = sum(rolls)
            history.append((notation, rolls, total))
            if n == 1:
                print(f"➡️  You rolled: {rolls[0]}")
            else:
                print(f"➡️  Rolls: {rolls}   Total: {total}")

        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nInterrupted. Type 'quit' to exit.")
        except EOFError:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
