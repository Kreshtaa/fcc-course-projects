def verify_card_number(string):
    digit_list = []
    for number in string:
        if number in "1234567890":
            digit_list.append(int(number))
    
    checklist = digit_list[-2::-1]

    for i in range(0, len(checklist), 2):
        doubled = checklist[i] * 2
        checklist[i] = doubled - 9 if doubled > 9 else doubled
    checklist.insert(0, digit_list[-1])
    if sum(checklist) % 10 == 0:
        return "VALID!"
    if sum(checklist) % 10 != 0:
        return "INVALID!"
