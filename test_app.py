import sys
import pyqt5_app
from PyQt5.QtWidgets import QApplication

class TestPyQT():

    def start_test(self):
        test_num = sys.argv[2]
        for m in dir(self):
            if m == "test" + str(test_num):
                print("method name : ",m)
                func = self.__getattribute__(m)
                print(func.__doc__)
                func()
                break
        
    def activate_gui(self):
        app = QApplication(sys.argv)
        ex = pyqt5_app.App()
        sys.exit(app.exec_())

    def set_text(self,path):
        with open(path, "r") as f: 
            s = f.read()
        with open("text.txt","w") as f: 
            f.write(s)

        print("# loaded file content")
        print(s) 

    def test1(self): 
        """Set first text.
        """
        self.set_text("test_texts/test_text1.txt")
        self.activate_gui()

    def test2(self): 
        """long text.
        """
        self.set_text("test_texts/test_text2.txt")
        self.activate_gui()

if __name__ == '__main__':
    print("#"*30)
    if len(sys.argv) != 3: 
        print(f"usage : python {sys.argv[0]} --case/-c <test-number>")
        sys.exit()
    test = TestPyQT()
    test.start_test()
