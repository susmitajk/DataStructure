def manacher(s: str) -> str:
    # Transform the string
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    P = [0] * n
    C = R = 0  # Center and Right boundary of the current rightmost palindrome

    for i in range(n):
        mirror = 2 * C - i  # Mirror of i around C

        if i < R:
            P[i] = min(R - i, P[mirror])

        # Expand around center i
        while i + P[i] + 1 < n and i - P[i] - 1 >= 0 and t[i + P[i] + 1] == t[i - P[i] - 1]:
            P[i] += 1

        # Update the center and right boundary
        if i + P[i] > R:
            C, R = i, i + P[i]

    # Find the maximum element in P and its index
    max_len = max(P)
    center_index = P.index(max_len)

    # Extract the longest palindromic substring from the original string
    start = (center_index - max_len) // 2  # Start index in the original string
    return s[start:start + max_len]

# Example usage:
print(manacher("babad"))  # Output: "bab" or "aba"
print(manacher("cbbd"))   # Output: "bb"