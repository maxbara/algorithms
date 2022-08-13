
def count_to(count):
    '''Iterator implementation'''

    numbers_in_german = ['eins', 'zwei', 'drei', 'vier', 'funf']

    iterator = zip(range(count), numbers_in_german)

    for position, number in iterator:
        
        #Returns a 'generator' containing numbers in German
        yield number

for num in count_to(3):
    print(num)

for num in count_to(5):
    print(num)