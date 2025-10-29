"""
Daily Coding Challenge: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-29
"""
def sort(emails):
    emails = sorted(emails, key = lambda email: email.lower().split('@')[::-1])
    return emails
