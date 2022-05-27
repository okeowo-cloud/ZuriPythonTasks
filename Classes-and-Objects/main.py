class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, name):
        self.name = name

    def change_age(self, age):
        self.age = age

    def add_track(self, track):
        return self.tracks.append(track)

    def get_score(self):
        return self.score


Bob = Student("Bob", 26, ["FE", "BE"], 20.90)

print("::: before change :::")
print(Bob.name)
print(Bob.age)
print(Bob.tracks)
print(Bob.get_score())

# Expected methods
print("::: after change :::")
Bob.change_name("Peter")
print(Bob.name)
Bob.change_age(34)
print(Bob.age)
Bob.add_track("UI/UX")
print(Bob.tracks)
print(Bob.get_score())
