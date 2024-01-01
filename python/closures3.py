def create_counter(count):
    count = count

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter_from_10 = create_counter(10)
print(counter_from_10())  # 11
print(counter_from_10())  # 12
