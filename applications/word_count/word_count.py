def word_count(s):
    string = s.lower().split(' ')
    ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&', '\\', ' ']
    solution = {}
    
    for c in s:
        if c in ignore:
            s = s.replace(c, ' ')

    # join the words back together, then remove spaces created by replacment, then split works on the spaces
    s = ' '.join(s.split())

    # makes string a list
    new_string = s.split()

    for c in new_string:
        c = c.lower() #ignore case
        if c in solution:
            solution[c] += 1
        else:
            solution[c] = 1

    return solution

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('Hello, my cat.  And my cat doesn\'t say "hello" back.'))