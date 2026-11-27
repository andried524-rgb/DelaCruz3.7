def clean_letters(full_name):
    """Keep letters only (symbols, digits and spaces are excluded),
    uppercase them, and discard duplicate letters."""
    unsorted_arr = []
    for ch in full_name.upper():
        if ch.isalpha() and ch not in unsorted_arr:
            unsorted_arr.append(ch)
    return unsorted_arr


def insertion_sort(arr):
    """Return a sorted copy using insertion sort."""
    result = arr.copy()
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


def main():
    full_name = input("Enter your full name: ")

    unsorted_arr = clean_letters(full_name)
    sorted_arr = insertion_sort(unsorted_arr)

    print("Unsorted array:", unsorted_arr)
    print("Sorted array:  ", sorted_arr)


if __name__ == "__main__":
    main()
