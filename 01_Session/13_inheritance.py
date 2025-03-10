class Parent:
  num = 0
  #생성자
  def __init__(self, num) -> None:
    self.num = num
    print('부모클래스 생성자 소환')

class Child(Parent):
  #생성자
  def __init__(self, num) -> None:
    super().__init__(num)
    print('자식클래스 생성자 소환')
  
  def displayValue(self):
    print('num: ', self.num)

cd = Child(20)
cd.displayValue()