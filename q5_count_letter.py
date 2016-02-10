def count_letter(string, ch):
    if len(string) == 1:
        if string == ch:
            return 1
        else:
            return 0
    else:
        if string[-1] == ch:
            return count_letter(string[:-1], ch) + 1
        else:
            return count_letter(string[:-1], ch)

print(count_letter("Welcome","e"))
