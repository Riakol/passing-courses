def remove_marks(text, marks):
    remove_marks.__dict__.setdefault('count', 0)
    remove_marks.count += 1
    for letter in text:
        if letter in marks:
            text = text.replace(letter, '')
    return text
