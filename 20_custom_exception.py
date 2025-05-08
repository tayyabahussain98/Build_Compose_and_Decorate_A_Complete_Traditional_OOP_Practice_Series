class InvalidAgeError(Exception):
    pass

def check_age(age: int):
    if age < 18:
        raise InvalidAgeError('Age must be 18+')
    return True

if __name__ == '__main__':
    try:
        user_input: int = int(input('Enter your age: '))
        if check_age(user_input):
            print('You are eligible.')

    except InvalidAgeError as e:
        print(f'Error: {e}')

    except ValueError:
        print('Please enter a valid age.')