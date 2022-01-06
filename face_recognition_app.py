import os
import shutil

from kivy.animation import Animation
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior, ThemeManager
from kivymd.toast import toast
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.list import MDList, OneLineIconListItem

from database import DataBase

# Window.size = (1200, 1000)

helper = """
ScreenManager:
    WelcomeScreen:
    SignupScreen:
    LoginScreen:
    AttendanceScreen:
    
<WelcomeScreen>: 
    name: "WelcomeScreen"
    MDFloatLayout:
        md_bg_color: [35/255,49/255,48/255,1]
        Image:
            source: "assest/bg.png"
    
    MDLabel:
        id : label
        text: " CONTACTLESS "
        font_style: "H2"
        halign: "left"
        pos_hint: {'center_y':0.75}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        
    MDLabel:
        id : label
        text: " Attendance System"
        font_style: "H2"
        halign: "left"
        pos_hint: {'center_y':0.65}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
    MDLabel:
        id : label
        text: "                               Develop: TEAM-HAMSUKY"
        font_style: "Button"
        halign: "left"
        pos_hint: {'center_y':0.156}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        
    
    MDFloatingActionButton:
        id : welcome_skip
        icon: "arrow-right"
        md_bg_color: 1,0,0,1
        pos_hint: {'center_x':0.9,'center_y':0.1}
        user_font_size: "50sp"
        on_release :
            root.manager.current = 'loginScreen'
            root.manager.transition.direction = 'left'
    Screen: 
        
        ScreenManager:
            Screen:
                orientation: "vertical"
                
                MDToolbar:
                    title: "Attendance Management System"
                    md_bg_color: [35/255,59/255,48/255,1]
                    elevation: 10
                    pos_hint: {"top": 1}
                    left_action_items:[["home", lambda x: x]] #
                        
        Widget: 
        
        
            
    MDProgressBar:
        value: 30
        pos_hint: {'center_y':0.02} 
    
<LoginScreen>:
    
    name: "loginScreen" 
    password : password
    email : email
    on_enter:
        app.anim(back)
        app.anim1(back1)
        # app.anim3(back3)
        # app.anim2(back2)
        
    MDFloatLayout:
        
        
        MDFloatLayout:
            
            id : back
            size_hint_y : .6
            pos_hint : {"center_y":1.8}
            radius: [0,0,0,40]
            canvas:
                Color:
                    rgb: (112, 0, 0)
                Rectangle:
                    size : self.size
                    pos: self.pos
        MDFloatLayout:
            id : back1
            size_hint_y : .6
            pos_hint : {"center_y":1.8}
            radius: [0,0,0,40]
            canvas:
                Color:
                    rgb: (112,0,0)
                Ellipse:
                    size : self.size
                    pos: self.pos
        MDIconButton:
            id : icon
            icon : "account-circle"
            pos_hint : {"center_x": .5,"center_y": .8}
            theme_text_color: "Custom"
            user_font_size: "60sp"
            text_color: 1,1,1,1
        MDLabel:
            id: label
            text: "Login Page"
            markup: True
            pos_hint : {"center_y": .75}
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1,0,0,1
            font_style: "H2"
            opacity : 0
        MDTextFieldRound:
            # id : back2
            id: email
            icon_left: "email-check"
            hint_text: "Email"
            foreground_color: 1, 0, 0, 1
            size_hint_x: .5
            width: 220
            font_size: 20
            pos_hint: {"center_x": 0.5,"center_y":.46}    
        
        MDTextFieldRound:
            # id : back3
            id: password
            icon_left: "key-variant"
            hint_text: "password"
            password: True
            foreground_color: 1, 0, 0, 1
            size_hint_x: .5
            width: 220
            font_size: 20
            pos_hint: {"center_x": 0.5,"center_y":.36}
            required: True
            
        
        MDFillRoundFlatButton:
            text: "LOG IN"
            font_size: 15
            
            pos_hint: {"center_x": 0.5,"center_y": .2}
            on_release: 
                root.manager.transition.direction = 'up'
                root.loginBtn()
        MDLabel:
            text: "Don't have an Account?"
            pos_hint: {"center_x": 0.915,"center_y": .1}
            font_style: "Body2"
        MDTextButton: 
            text: "Create One"
            pos_hint: {"center_x": 0.55,"center_y": .1}
            theme_text_color: "Custom"
            text_color: 1,0,0,1
            custom_color: 1,0,0,1
            on_release: 
                root.manager.transition.direction = 'right'
                root.manager.current = 'signupScreen'
        MDFloatingActionButton:
            id : welcome_skip
            icon: "arrow-left"
            md_bg_color: 1,0,0,1
            pos_hint: {'center_x':0.1,'center_y':0.1}
            user_font_size: "20sp"
            on_release :
                root.manager.current = 'WelcomeScreen'
                root.manager.transition.direction = 'left'
    Screen: 
        
        ScreenManager:
            Screen:
                orientation: "vertical"
                
                MDToolbar:
                    title: "Attendance Management System"
                    md_bg_color: [35/255,59/255,48/255,1]
                    elevation: 10
                    pos_hint: {"top": 1}
                    # left_action_items:[["home", lambda x: x]] #
                        
        Widget:
                
    MDProgressBar:
        value: 60
        pos_hint: {'center_y':0.02}
        
        
    
<SignupScreen>:
    name: "signupScreen" 
    namee: namee
    email: email
    password : password
    MDFloatLayout:
        
        md_bg_color: [35/255,59/255,48/255,1]
        
               
        MDLabel:
            id: label
            text: "SignUp-Page"
            
            pos_hint : {"center_y": .75}
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1,1,1,1
            font_style: "H2" 
        MDTextFieldRound:
            id: namee
            icon_left: "account-check"
            hint_text: "Enter username"
            foreground_color: 1, 0, 0, 1
            size_hint_x: .5
            width: 220
            font_size: 20
            pos_hint: {"center_x": 0.5,"center_y":.54}
            
        MDTextFieldRound:
            id: password
            icon_left: "key-variant"
            hint_text: "Enter your password"
            foreground_color: 1, 0, 0, 1
            size_hint_x: .5
            width: 220
            font_size: 20
            pos_hint: {"center_x": 0.5,"center_y":.44}
        MDTextFieldRound:
            id: email
            icon_left: "mail"
            hint_text: "Enter your email"
            foreground_color: 1, 0, 0, 1
            size_hint_x: .5
            width: 220
            font_size: 20
            pos_hint: {"center_x": 0.5,"center_y":.34}
        MDFillRoundFlatButton:
            text: "SUBMIT"
            font_size: 15
            pos_hint: {"center_x": 0.5,"center_y": .2}
            on_release: 
                root.manager.transition.direction = 'left'
                root.submit()
        MDLabel:
            text: "Already have an Account?"
            pos_hint: {"center_x": 0.921,"center_y": .1}
            font_style: "Body2"
            theme_text_color: "Custom"
            text_color: 1,1,1,1
        MDTextButton: 
            text: "Log In"
            pos_hint: {"center_x": 0.56,"center_y": .1}
            theme_text_color: "Custom"
            text_color: 1,1,0,1
            on_press:
                root.manager.transition.direction = 'left'
                root.login()
                
    Screen: 
        
        ScreenManager:
            Screen:
                orientation: "vertical"
                
                MDToolbar:
                    title: "Attendance Management System"
                    md_bg_color: [35/255,59/255,48/255,1]
                    elevation: 10
                    pos_hint: {"top": 1}
                    # left_action_items:[["home", lambda x: x]] #
                        
        Widget:
        
    MDProgressBar:
        value: 90
        pos_hint: {'center_y':0.02}

    
<AttendanceScreen>:
    name: 'attendanceScreen'
    MDFloatLayout:
        md_bg_color: [35/255,49/255,48/255,1]
    BoxLayout:
        orientation: "vertical"
        # pos_hint: {"center_x": .5, "center_y": .5}
        padding: 20,10
        size_hint_y: .82 
        GridLayout:
            cols: 2
            spacing: 10
            MDCard: 
                orientation: "vertical"
                padding: "8dp"
                height: "210dp"
                elevation: 5
                border_radius: 20
                radius: [15]
                Image:
                    source: "assest/addd.png"
                MDLabel:
                    md_bd_color:
                    text: "Upload faces to be encoded from your local drive "
                    pos_hint: {"center_x": 0.621,"center_y": .1}
                    theme_text_color: "Custom"
                    text_color: 1,0,0,1
                MDLabel:
                    md_bd_color:
                    text: " to the app directory for recognition"
                    pos_hint: {"center_x": 0.621,"center_y": .1}
                    theme_text_color: "Custom"
                    text_color: 1,0,0,1
                MDFillRoundFlatButton:
                    text: "UPLOAD_FACES"
                    font_size: 15
                    pos_hint: {"center_x": 0.5,"center_y": .2}
                    on_release: app.file_manager_open()
            MDCard: 
                orientation: "vertical"
                padding: "8dp"
                height: "210dp"
                elevation: 5
                border_radius: 20
                radius: [15]
                Image:
                    source: "assest/attendance1.png"
                MDLabel:
                    md_bd_color:
                    text: "CLick on the button and wait for the camera to finish booting up"
                    pos_hint: {"center_x": 0.621,"center_y": .1}
                    theme_text_color: "Custom"
                    text_color: 1,0,0,1
                MDLabel:
                    text: "press 'q' on the keyboard to close the camera"
                    pos_hint: {"center_x": 0.621,"center_y": .1}
                MDFillRoundFlatButton:
                    text: "TAKE-ATTENDANCE"
                    font_size: 15
                    on_press: app.performAttendance()
                    pos_hint: {"center_x": 0.5,"center_y": .2}
            MDCard: 
                orientation: "vertical"
                padding: "8dp"
                height: "210dp"
                elevation: 5
                border_radius: 20
                radius: [15]
                Image:
                    source: "assest/view1.png"
                MDLabel:
                    md_bd_color:
                    text: "Click and wait for the Excel-Sheet to open"
                    pos_hint: {"center_x": 0.621,"center_y": .1}
                    theme_text_color: "Custom"
                    text_color: 1,0,0,1
                MDFillRoundFlatButton:
                    text: "VIEW-ATTENDANCE"
                    font_size: 15
                    on_press: app.viewAttendance()
                    pos_hint: {"center_x": 0.5,"center_y": .2}
            MDCard: 
                orientation: "vertical"
                padding: "8dp"
                height: "210dp"
                elevation: 5
                border_radius: 20
                radius: [15]
                Image:
                    source: "assest/exit.png"
                
                MDFillRoundFlatButton:
                    text: "LOG-OUT"
                    font_size: 15
                    on_press: root.logOut()
                    pos_hint: {"center_x": 0.5,"center_y": .2}
               
                
                    
            
            
    
    
            
        # ScrollView:
        #     DrawerList:
        #         id: md_list
        #         md_bg_color: [35/255,69/255,48/255,1]
        #         spacing : "65dp"
        #         padding: "75dp"
        #         TwoLineIconListItem:
        #             text: "Upload faces"
        #             secondary_text: "Upload faces to encode from your local drive"
        #             theme_text_color: "Custom"
        #             font_style: "Button"
        #             text_color: 1,1,1,1
        #             secondary_text_color: 1,0,1,1
        #             on_release: app.file_manager_open()
        #             IconLeftWidget:
        #                 icon: "file-upload"
        #                 md_bg_color: 1,1,1,1
        #         OneLineIconListItem:
        #             text: "Take Attendance"
        #             theme_text_color: "Custom"
        #             text_color: 1,1,1,1
        #             font_style: "Button"
        #             on_press: app.performAttendance()
        #             IconLeftWidget:
        #                 icon: "face-recognition"
        #                 md_bg_color: 1,1,1,1
        #         OneLineIconListItem:
        #             text: "View Attendance:"
        #             theme_text_color: "Custom"
        #             text_color: 1,1,1,1
        #             on_press: app.contact()
        #             font_style: "Button"
        #             IconLeftWidget:
        #                 icon: "face-profile-woman"
        #                 md_bg_color: 1,1,1,1
        #         OneLineIconListItem:
        #             text: "Log-out"
        #             theme_text_color: "Custom"
        #             text_color: 1,1,1,1
        #             on_press: root.logOut()
        #             font_style: "Button"
        #             IconLeftWidget:
        #                 icon: "logout-variant"
        #                 md_bg_color: 1,1,1,1
    
    Screen: 
        ScreenManager:
            Screen:
                orientation: "vertical"    
                MDToolbar:
                    title: "Attendance Management System"
                    md_bg_color: [35/255,59/255,48/255,1]
                    elevation: 10
                    pos_hint: {"top": 1}
                    
        Widget:                    
    

    MDProgressBar:
        value: 120
        pos_hint: {'center_y':0.02}
"""

db = DataBase("users.txt")


class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Attendance Management System"
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = "Cyan"
        self.theme_cls.accent_palette = "Blue"
        self.theme_cls.theme_style = "Light"

        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )

        # shutil.copy('file_manager', 'imageData')

    def build(self):
        # global screen_manager
        # screen_manager =ScreenManager()
        # screen_manager.add_widget(Builder.load_string(helper))
        # return screen_manager
        self.strng = Builder.load_string(helper)
        return self.strng

    def performAttendance(self):
        os.system("python code.py")

    def viewAttendance(self):
        os.system("Attendance.csv")

    def file_manager_open(self):
        from plyer import filechooser
        path = filechooser.open_file()[0]
        # this method returns a list with the first index
        # being the path of the file selected
        toast(path)
        dst = os.path.basename(path)
        os.path.splitext(dst)

        destination = "C:/Users/ITAPP03/PycharmProjects/attendanceAPP/imageData/" + os.path.splitext(dst)[0] + \
                      os.path.splitext(dst)[1]
        shutil.copyfile(dst, destination)

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        toast(path)
        MDApp.get_running_app().storage_photo(path)
        print(path)

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    def anim(self, widget):
        anim = Animation(pos_hint={'center_y': 1.16})
        anim.start(widget)

    def anim1(self, widget):
        anim = Animation(pos_hint={'center_y': .85})
        anim.start(widget)

    def current_slide(self, index):
        pass


class SignupScreen(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)
                self.reset()
                self.manager.current = "loginScreen"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        self.manager.current = "loginScreen"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


class WelcomeScreen(Screen):
    pass


class LoginScreen(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            AttendanceScreen.current = self.email.text

            self.reset()
            self.manager.current = "attendanceScreen"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "attendanceScreen"

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class AttendanceScreen(Screen):

    def logOut(self):
        self.manager.current = "WelcomeScreen"

    def file_manager_open(self):
        self.file_manager.show(os.listdir("~"))  # output manager to the screen
        self.manager_open = True

    # def on_enter(self, *args):
    #     password, name, created = db.get_user(self.current)
    #     self.n.text = "Account Name: " + name
    #     self.email.text = "Email: " + self.current
    #     self.created.text = "Created On: " + created


def invalidLogin():
    pop = Popup(title="invalid login",
                content=Label(text="invalid username or password"),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                content=Label(text='Please fill in all inputs with valid information.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='welcomeScreen'))
sm.add_widget(SignupScreen(name='signupScreen'))
sm.add_widget(LoginScreen(name='loginScreen'))
sm.add_widget(AttendanceScreen(name='attendanceScreen'))


class ContentNavigationDrawer(BoxLayout):
    pass


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        '''Called when tap on a menu item.'''

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()


MainApp().run()
