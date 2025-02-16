def palindrome(s):
    count1 = {}
    for simvol in s:
        if simvol in count1:
            count1[simvol] += 1
        else:
            count1[simvol] = 1

    count2 = 0
    simvols = ''
    palindromes = ''

    for simvol in count1:
        if count1[simvol] % 2 != 0:
            count2 += 1
            if count2 > 1:
                return "Невозможно сформировать палиндром из данного слова."
            else:
                simvols = simvol

        for _ in range(count1[simvol] // 2):
            palindromes += simvol

    return palindromes + simvols + palindromes[::-1]

a = input()
print(palindrome(a))
