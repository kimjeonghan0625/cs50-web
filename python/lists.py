# Define a list of names
names = []

names.append("Miso")
names.append("JeongHan")
names.append("Ellie")
print(names)  # ['Miso', 'JeongHan', 'Ellie']
deleted_name = names.pop()
# names.sort()
print(names)  # ['Miso', 'JeongHan']
print(f"삭제된 요소는 {deleted_name}입니다")  # 삭제된 요소는 Ellie입니다
