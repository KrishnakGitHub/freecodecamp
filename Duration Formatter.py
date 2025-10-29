"""
Daily Coding Challenge: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-26
"""
def format(seconds):
    h, seconds = divmod(seconds, 3600)
    m, s = divmod(seconds, 60)
    return f"{h}:{m:02}:{s:02}" if h else f"{m}:{s:02}"
