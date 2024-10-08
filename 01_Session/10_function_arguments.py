# *arguments는 가변인자(variable argument): 별 한개면 리스트
# **keywords는 가변인자(keyword argument): 별 한개면 딕셔너리

def caffe(beverage, *arguments, **keywords):
    print("Do you have any", beverage, "?")
    for arg in arguments:
      print(arg)
    print("*****")
    for kw in keywords:
      print(kw, ":", keywords[kw])

caffe("coffee", "it's yummy, sir.", "Would you try",
      barista = "gumin",
      client = "bssm",
      cup = "venti")