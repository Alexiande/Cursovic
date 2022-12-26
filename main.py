from kivy.factory import Factory
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty

from kivy.animation import Animation
from kivy.properties import NumericProperty
import time

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.uix.behaviors import RectangularRippleBehavior, BackgroundColorBehavior, CircularRippleBehavior
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList

from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem

from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivymd.uix.screenmanager import ScreenManager

Builder.load_file('MainScreen.kv')
Builder.load_file('sing in_and_sing_up.kv')
Builder.load_file('camera.kv')
Builder.load_file('about_us.kv')
Builder.load_file('cab.kv')

class MainApp(MDApp):

    def show_custom_bottom_sheet(self,image,price,rate,specifications,about):
        bottom_sheet=Factory.ContentCustomSheet()
        bottom_sheet.rate=rate
        bottom_sheet.image=image
        bottom_sheet.price=price
        bottom_sheet.specifications = specifications
        bottom_sheet.about=about
        self.custom_sheet = MDCustomBottomSheet(screen=bottom_sheet)
        self.custom_sheet.open()
    def set_screen(self,cart):
        self.root.current = "cart"
    def set_screens(self, cart):
        self.root.current ="help_me"
    def set_screensi(self,cart):
        self.root.current="main"
    def build(self):
        self.title = 'KivyMD Online Shop'
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu')) #+
        sm.add_widget((MainScreen(name="main")))#+
        sm.add_widget(SettingsScreen(name='help')) #+
        sm.add_widget(FilterScreen(name='filter'))#+
        sm.add_widget(PodsScreen(name='pods'))#+
        sm.add_widget(CartScreen(name='cart'))#+
        sm.add_widget(SmartScreen(name='smart'))#+
        sm.add_widget(TableScreen(name='table'))#+
        sm.add_widget(AccessScreen(name='acces'))#+
        sm.add_widget(Help_meScreen(name="help_me"))#-
        sm.add_widget(CameraClick(name="camera"))#-
        sm.add_widget(InScreen(name="in"))#+
        sm.add_widget(InitScreen(name="init"))#+
        sm.add_widget(CabScreen(name="cab"))  # +
        sm.add_widget(Ac_helpScreen(name="helper"))
        return sm

class ContentNavigationDrawer(MDBoxLayout):
    pass
class MenuScreen(Screen):
    animation_constant = NumericProperty(40)

    def __init__(self, **kw):
        super().__init__(**kw)
        anim = Animation(animation_constant=10, duration=.6, t='in_out_quad') + Animation(animation_constant=40,
                                                                                          duration=.6, t='in_out_quad')
        anim.repeat = True
        anim.start(self)
class Ac_helpScreen(Screen):
    pass
class MainScreen(Screen):
    pass
class InitScreen(Screen):
    pass
class SmartScreen(Screen):
    pass
class CabScreen(Screen):
    pass
class Help_meScreen(Screen):
    pass
class AccessScreen(Screen):
    pass
class FilterScreen(Screen):
    pass
class SettingsScreen(Screen):
    pass
class PodsScreen(Screen):
    pass
class CartScreen(Screen):
    pass
class TableScreen(Screen):
    pass
class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))
class InScreen(Screen):
    pass

Window.keyboard_anim_args = {'d': 0.5, 't': 'in_out_quart'}
Window.softinput_mode="below_target"
class RectangularRippleButton(MDBoxLayout,
                              RectangularRippleBehavior, ButtonBehavior, BackgroundColorBehavior
                              ):
    pass


class RectangularRippleImage(CircularRippleBehavior, ButtonBehavior, Image):
    pass
class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):

        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

class CameraClick(BoxLayout,Screen):
    def capture(self):
        camera = self.ids.camera
        time_str = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png(f'images/10.jpg')
        print("Captured")
MainApp().run()