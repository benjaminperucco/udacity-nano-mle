# -----------------------------------------------------------------------------
# Optimizing code: Common books
# -----------------------------------------------------------------------------
# Here's the code your coworker wrote to find the common book ids in
# `books_published_last_two_years.txt` and `all_coding_books.txt`
# to obtain a list of recent coding books.
# -----------------------------------------------------------------------------
import time
import numpy as np

# -----------------------------------------------------------------------------
# Define user parameters
# -----------------------------------------------------------------------------
root_path = 'C:/Users/Benjamin/Development/' \
            + 'Nanodegree Machine Learning Engineer/' \
            + '2 Software Engineering Fundamentals'

# -----------------------------------------------------------------------------
# Read files
# -----------------------------------------------------------------------------
with open(root_path + '/Data/books_published_last_two_years.txt') as f:
    recent_books = f.read().split('\n')

with open(root_path + '/Data/all_coding_books.txt') as f:
    coding_books = f.read().split('\n')

# -----------------------------------------------------------------------------
# Run inadequate solution
# -----------------------------------------------------------------------------
start = time.time()
recent_coding_books = []

for book in recent_books:
    if book in coding_books:
        recent_coding_books.append(book)

time_duration_version_1 = time.time() - start
print('Number of recent coding books: {}\nDuration: {} seconds'.
        format(len(recent_coding_books), time_duration_version_1)
      )

# -----------------------------------------------------------------------------
# Tip 1: Use vector operations over loops when possible.
# Use numpy `intersect1d` method to get the intersection of the `recent_books`
# and `coding_books` arrays.
# -----------------------------------------------------------------------------
start = time.time()
recent_coding_books = np.intersect1d(recent_books, coding_books)
time_duration_version_2 = time.time() - start
print('Number of recent coding books: {}\nDuration: {} seconds'.
        format(len(recent_coding_books), time_duration_version_2)
      )

# -----------------------------------------------------------------------------
# Tip 2: Know your data structures and which methods are faster.
# Use the set's `intersection` method to get the common elements in
# `recent_books` and `coding_books`.
# -----------------------------------------------------------------------------
start = time.time()
recent_coding_books = set(recent_books).intersection(coding_books)
time_duration_version_3 = time.time() - start
print('Number of recent coding books: {}\nDuration: {} seconds'.
        format(len(recent_coding_books), time_duration_version_3)
      )
