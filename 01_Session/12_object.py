import os
os.system('clear')

#클래스 선언
class Dog:
  name = 'default'
  gender = 'Male/Female'
  owner = 'default name'

  def Bark(self):
    print(self.name + ': 명령')

#객체 생성과 사용법
dog = Dog()
dog.name = "이창수엘라"
dog.gender = "Male"
dog.owner = "세시두분"
dog.Bark()