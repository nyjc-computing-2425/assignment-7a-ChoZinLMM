NUM_WORD = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}

def text_numeral(num):
    """
    Takes in a number between 1 to 99 inclusive and returns the value in text.
  
    Parameters
    ----------
    num: int
        a number between 1 to 99 inclusive
  
    Returns
    -------
    str
        a string of the number in text
    """
    if num > 90:
      fir_dig = int(num) - 90
      sec_dig = 90
      return(f'{NUM_WORD.get(sec_dig)} {NUM_WORD.get(fir_dig)}')
      
    elif (num < 20) or (str(num/10)[2] == '0'):
      return(f'{NUM_WORD.get(int(num))}')

    else :
      first, second = divmod(num, 10)
      return(f'{NUM_WORD.get(first * 10)} {NUM_WORD.get(second)}')