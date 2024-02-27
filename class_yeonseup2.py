class Gibucheonsa:
    these = "are all yours"


pupil1_greedy = Gibucheonsa()
pupil2_thoughtful = Gibucheonsa()
pupil1_greedy.these = "are mine"

print(Gibucheonsa.these)
# are all yours

print(pupil1_greedy.these)
# are mine

print(pupil2_thoughtful.these)
# are all yours

# ================================================================================
# print(Gibucheonsa.__dict__)
# # {'__module__': '__main__',
# # 'these': 'are all yours',
# # '__dict__': <attribute '__dict__' of 'Gibucheonsa' objects>,
# # '__weakref__': <attribute '__weakref__' of 'Gibucheonsa' objects>,
# # '__doc__': None}


# print(pupil1_greedy.__dict__)
# # {'these': 'are mine'}

# print(pupil2_thoughtful.__dict__)
# # {}

# print(dir())
# # ['Gibucheonsa',      <<< 클래스
# # '__annotations__',
# # '__builtins__',
# # '__cached__',
# # '__doc__',
# # '__file__',
# # '__loader__',
# # '__name__',
# # '__package__',
# # '__spec__',
# # 'pupil1_greedy',      <<< 인스턴트1
# # 'pupil2_thoughtful']  <<< 인스턴트2