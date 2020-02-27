nums = [{'name': 'r', 'number': 123}, {'name': 's', 'number': 345}, {'name': 'L', 'number': 123}, {'name': 'l', 'number':456}]


def return_numbers(contacts):
    numbers = []
    for a_contact in contacts:
        if a_contact['name'][0].casefold() == 'l':
            numbers.append(a_contact['number'])
    return numbers


print(return_numbers(nums))
