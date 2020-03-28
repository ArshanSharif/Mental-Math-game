from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
import random
from kivy.uix.popup import Popup
points = 3
level = 1
realpoints = 0
class StartWindow(Screen):
    def start(self):



        answers_w = open("answer.txt", "w")
        answers_w.write("2")
        answers_w.close()
        points_w = open("points.txt", "w")
        points_w.write("0")
        points_w.close()

class PlayWindow(Screen):


    def display_points(self):

        self.points.text = "Lives: " + str(points)


    def random_problem(self):
        global answer
        global points
        global level
        global realpoints
        symlist1 = [" + ", " - "]
        symlist2 = [" + ", " - "," x "]
        symlist3 = [" + ", " - "," x "," ÷ "]
        answers_r = open("answer.txt","r")
        answers = answers_r.read().splitlines()

        if str(self.main_text.text) in answers:
            answers_r.close()



            if level == 1:
                realpoints += 1
                symbol = random.choice(symlist1)
                if symbol == " + ":
                    num1 = random.randint(0, 12)
                    num2 = random.randint(0, 12)
                    answer = num1+num2
                    answer = str(answer)
                    print(answer)
                    answers_w = open("answer.txt","w")
                    answers_w.write(answer)
                    answers_w.close()
                    self.problems.text = str(num1) + str(symbol) + str(num2) + " = ? "

                if symbol == " - ":
                    num1 = random.randint(0, 12)
                    num2 = random.randint(0, 12)
                    num1 = num1+num2
                    answer = num1 - num2
                    answer = str(answer)
                    print(answer)
                    answers_w = open("answer.txt", "w")
                    answers_w.write(answer)
                    answers_w.close()
                    self.problems.text = str(num1) + str(symbol) + str(num2) + " = ? "
            if level == 2:
                realpoints += 2
                symbol = random.choice(symlist2)
                if symbol == " + ":
                    num1 = random.randint(1, 30)
                    num2 = random.randint(1, 30)
                    answer = num1+num2
                    answer = str(answer)
                    print(answer)
                    answers_w = open("answer.txt","w")
                    answers_w.write(answer)
                    answers_w.close()
                    self.problems.text = str(num1) + str(symbol) + str(num2) + " = ? "

                if symbol == " - ":
                    num1 = random.randint(1, 20)
                    num2 = random.randint(1, 20)
                    num1 = num1+num2
                    answer = num1 - num2
                    answer = str(answer)
                    print(answer)
                    answers_w = open("answer.txt", "w")
                    answers_w.write(answer)
                    answers_w.close()
                    self.problems.text = str(num1) + str(symbol) + str(num2) + " = ? "
                if symbol == " x ":
                    num1 = random.randint(0, 12)
                    num2 = random.randint(0, 12)
                    answer = str(num1*num2)
                    print(answer)
                    answers_w = open("answer.txt", "w")
                    answers_w.write(answer)
                    answers_w.close()
                    self.problems.text = str(num1) + str(symbol) + str(num2) + " = ? "
            if level == 3:
                realpoints += 3
                symbol = random.choice(symlist3)
                if symbol == " + ":
                    num1 = random.randint(10, 60)
                    num2 = random.randint(10, 60)
                    answer = num1 + num2
                    answer = str(answer)
                    print(answer)
                    answers_w = open("answer.txt", "w")
                    answers_w.write(answer)
                    answers_w.close()
                    self.problems.text = str(num1) + str(symbol) + str(num2) + " = ? "

                if symbol == " - ":
                    num1 = random.randint(10, 30)
                    num2 = random.randint(10, 30)
                    num1 = num1 + num2
                    answer = num1 - num2
                    answer = str(answer)
                    print(answer)
                    answers_w = open("answer.txt", "w")
                    answers_w.write(answer)
                    answers_w.close()
                    self.problems.text = str(num1) + str(symbol) + str(num2) + " = ? "
                if symbol == " x ":
                    num1 = random.randint(1, 12)
                    num2 = random.randint(1, 12)
                    answer = str(num1 * num2)
                    print(answer)
                    answers_w = open("answer.txt", "w")
                    answers_w.write(answer)
                    answers_w.close()
                    self.problems.text = str(num1) + str(symbol) + str(num2) + " = ? "
                if symbol == " ÷ ":
                    num1 = random.randint(1, 100)
                    num2 = random.randint(1, 100)
                    while (num1%num2) != 0:
                        num1 = random.randint(1, 100)
                        num2 = random.randint(1, 100)
                    answer = int(num1/num2)
                    answer = str(answer)
                    print(answer)
                    answers_w = open("answer.txt", "w")
                    answers_w.write(answer)
                    answers_w.close()
                    self.problems.text = str(num1) + str(symbol) + str(num2) + " = ? "





        else:
            points -=1
            if points < 0:
                points_w = open("points.txt", "w")
                points_w.write(str(realpoints))
                points_w.close()

                
                highscore_r = open("highscore.txt","r")
                highscore_file = highscore_r.read().splitlines()
                highscore = highscore_file[0]
                if int(realpoints) > int(highscore):
                    highscore_r.close()
                    highscore_w = open("highscore.txt","w")
                    highscore_w.write(str(realpoints))
                    highscore_w.close()
                    show_popup(1)
                else:
                    highscore_r.close()
                    show_popup(2)


                kv.current = "main"
                points = 3
                self.problems.text = "1 + 1 = ?"







    def change_text(self,number,tex):
        self.main_text.text = str(number) + str(tex)
class MenuWindow(Screen):
    def easy(self):
        global level
        level = 1

    def medium(self):
        global level
        level = 2

    def hard(self):
        global level
        level = 3
class WindowManager(ScreenManager):
    pass



kv = Builder.load_file("my.kv")

class P(FloatLayout):
    pass

class MyApp(App):
    def build(self):
        return kv
def show_popup(high_sc):
    show = P()
    popupWindow = Popup(title = "", content = show,size_hint = (None,None), size = (400,400))
    popupWindow.open()
    highscore_r = open("highscore.txt", "r")
    highscore_file = highscore_r.read().splitlines()
    highscore = highscore_file[0]
    if high_sc == 2:
        show.popscore.text = " Your Score: " + str(realpoints) +" \n High Score: " + str(highscore) + " \n Better Luck Next Time!"
    if high_sc == 1:
        show.popscore.text = " Congratulations! \n You Beat The High Score! \n Your Score: "+ str(realpoints)


if __name__ == "__main__":
    MyApp().run()
