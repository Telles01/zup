def reverso(s):
    return s[::-1]

def ePalindromo(s):
    rev = reverso(s)

    if (s == rev):
        return True
    return False

s = input()
ans = ePalindromo(s)

if ans == 1:
    print("Palindromo")
else:
    print("Não é Palindromo")
