# solution by Roman Frolov 2017
FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    number = str(number)
    index, ind = len(number), 0
    string = ""
    for num in number:
        if ind is not 0 and num is not '0':
            string += ' '
        num = int(num)
        if index == 3:
            string += FIRST_TEN[num-1] + ' ' + HUNDRED
        elif index == 2 and num is 0:
            index -= 1
            ind += 1
            continue
        elif index == 2 and num is not 1:
            string += OTHER_TENS[num-2]
        elif index == 2 and num == 1:
            string += SECOND_TEN[int(number[ind+1])]
            break
        elif index == 1:
            if num == 0:
                break
            else:
                string += FIRST_TEN[num-1]
        index -= 1
        ind += 1
    print(string)
    return string

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    assert checkio(999) == 'nine hundred ninety nine'