# Test Question 4 from J interview
# inputs = [60, 8, 2, 4, 5]
# output = 860542 (the max integer that can be formed by the numbers in inputs)


class Number:
    def __init__(self, value):
        # self.value = value
        self.strr = str(value)  # string representation
        self.length = len(self.strr)  # total number of digits

    def __lt__(self, other):
        count = min(self.length, other.length)

        for i in range(count):
            if self.strr[i] < other.strr[i]:
                return True  # e.g. 60 < 8

        if self.strr[:count] == other.strr[:count]:
            if self.length > other.length \
                    and self.strr[count] < other.strr[0]:
                return True  # e.g. 605 < 60

            if self.length < other.length \
                    and self.strr[0] <= other.strr[count]:
                return True  # e.g. 60 < 608

        return False

    def __str__(self):
        return self.strr

    def __repr__(self):
        return self.strr


def main():
    inputs = [60, 608, 8, 605, 606]
    numbers = []

    print("inputs = {}".format(inputs))

    for item in inputs:
        numbers.append(Number(item))

    # sort in ascending order
    numbers.sort(reverse=True)
    
    print("sorted = {}".format(numbers))

    result = ""

    for item in numbers:
        result = result + item.strr

    print("result = {}".format(result))

    return int(result)


if __name__ == "__main__":
    main()

