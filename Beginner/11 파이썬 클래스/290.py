# 290.py
class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()
    # 같은 이름이 있으면 부모 class가 override
    # 명시적으로 호출하고 싶으면 super 활용하기

나 = 자식() # "자식생성"
            # "부모생성"