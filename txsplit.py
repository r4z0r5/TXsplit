import random


def num_after_point(x):
    s = str(x)
    if '.' not in s:
        return 0
    return len(s) - s.index('.') - 1


def splitter(tx, nofp):
    '''

    :param tx: The total amount of funds being sent, float with 10 digits after point
    :param nofp: Nubmer of parts to split the sum into
    :return: Returns a list of values (sum of each part of the sum), must be unequal and pass the tests!
    '''
    left = tx
    parts = []  # all subtractions are recorded to make sure not a bitcent is lost :)
    nap = num_after_point(txsum)  # get the number of digits after the decimal point in TX sum
    while nofp > 0:
        part = round((random.uniform(0, round(float(left), nap))), nap)
        left -= part
        left = round(left, 10)
        nofp -= 1
        parts.append(part)
        if nofp == 1 and sum(parts) != txsum:
            parts.append(round(txsum - sum(parts), 10))
            break
    return parts


def test_equality(parts):
    if sum(parts) == txsum:
        print("[+] {} equals {}".format(sum(parts), txsum))
        return True
    else:
        print("[-] {} is not equal to {}".format(sum(parts), txsum))
        return False


def nap_test(parts):  # Makes sure that all numbers got >= digits after point to fit the Bitcoin specification
    for each in parts:
        if num_after_point(each) > 10:
            print('[-] Failed the digit after point test at {}'.format(each))
            return False
        else:
            print('[+] Everything is fine with those digits after point.')
            return True


if __name__ == '__main__':
    txsum = float(input('Total sum being sent: '))  # total transaction sum
    nofparts = int(input('Amount of parts to split the sum into: '))  # number of parts
    parts = splitter(txsum, nofparts)
    print(parts, '\n')
    if test_equality(parts) and nap_test(parts):
        print('[+] Tests passed! Use the generated data for tx splitting.')
    else:
        print('[-] Something went wrong, what a pity!')
