text = 'A0 B1 C2 D3 E4 F5 G6 H7 I8 J9'

SUP = str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹')
SUB = str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉')

print(text.translate(SUP))
print()
print(text.translate(SUB))
