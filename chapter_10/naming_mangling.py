class Duck():
    def __init__(self, input_name):
        self.__name = input_name
        # __ 던더(더블언더바)를 통해 name을 클래스 외부에서 볼 수 없도록 설정한 것 같은 효과를 본다. 네이밍 컨벤션
    
    @property
    def name(self):
        print("inside the getter")
        return self.__name
    
    @name.setter
    def name(self, input_name):
        print("inside the setter")
        self.__name = input_name

fowl = Duck("Howard")
print(fowl.name)

fowl.name = "Donald"
print(fowl.name)

print(fowl.__name)
# __name 에 직접 접근하려하면 error가 발생한다.