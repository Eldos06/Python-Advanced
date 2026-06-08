def process_grades(records: list[str]) -> dict:
    valid_count = 0
    skipped = 0
    total_score = 0
    passed_names = set() # To avoid duplicate last names

    for record in records:
        if not record or ':' not in record:
            skipped += 1
            continue

        try:
            name, grade_str = record.split(':', 1)
            name = name.strip()
            grade_str = grade_str.strip()

            if not name or not grade_str:
                skipped += 1
                continue

            grade = int(grade_str)

            if not (0 <= grade <= 100):
                skipped += 1
                continue

            valid_count += 1
            total_score += grade

            if grade >= 60:
                passed_names.add(name)

        except ValueError:
            skipped += 1
            continue

    if valid_count == 0:
        average = 0.0
        passed_list = []
    else:
        average = round(round(total_score / valid_count, 1))
        passed_list = sorted(list(passed_names))

    return {
        'valid_count': valid_count,
        'average': average,
        'passed': passed_list,
        'skipped': skipped,
    }

# if __name__ == '__main__':
#     data = [
#         "Yeldos: 89",
#         "Dosimzhan: 23",
#         "Veshislav: asdf",
#         ":32",
#         "Yeldos: 80",
#     ]
#
#     result = process_grades(data)
#     print(result)

def longest_increasing_streak(nums: list[int]) -> dict:
    if not nums:
        return {'length': 0, 'streak': []}

    max_streak = []
    current_streak = []

    for num in nums:
        if not current_streak or num > current_streak[-1]:
            current_streak.append(num)
        else:
            if len(current_streak) > len(max_streak):
                max_streak = current_streak
            current_streak = [num]

    if len(current_streak) > len(max_streak):
        max_streak = current_streak

    if len(max_streak) < 2:
        return {'length': 0, 'streak': []}

    return {'length': len(max_streak), 'streak': max_streak}

if __name__ == '__main__':
    print(longest_increasing_streak([1, 3, 2, 5, 8, 4, 7]))
    print(longest_increasing_streak([]))
    print(longest_increasing_streak([7]))
    print(longest_increasing_streak([5, 5, 5]))
    print(longest_increasing_streak([9, 5, 4, 3, 1]))
    print(longest_increasing_streak([1, 2, 0, 6, 2]))
