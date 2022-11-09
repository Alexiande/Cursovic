from kivy.factory import Factory
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList

from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem

from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivymd.uix.card import MDCard
from kivymd.uix.screenmanager import ScreenManager

from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

#from home import *
class MainApp(MDApp):

    def show_custom_bottom_sheet(self,image,price,rate,specifications):
        bottom_sheet=Factory.ContentCustomSheet()
        bottom_sheet.rate=rate
        bottom_sheet.image=image
        bottom_sheet.price=price
        bottom_sheet.specifications = specifications
        self.custom_sheet = MDCustomBottomSheet(screen=bottom_sheet)
        self.custom_sheet.open()
    def build(self):
        self.sm=ScreenManager()
        self.title = 'KivyMD Online Shop'
        #self.theme_cls.theme_style = "Dark"
        #self.theme_cls.primary_palette = "Teal"
    def on_start(self):
        icons_item = {
            "home": "Главная",
            "rhombus-split": "Аксессуары",
            "cellphone": "Смартфоны",
            "tablet": "Планшеты",
            "bell": "Уведомления",
            "magnify": "Поиск",
            "upload": "Выход",
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )

class ContentNavigationDrawer(MDBoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

KV = ""
#class TestNavigationDrawer(MDApp):





#TestNavigationDrawer().run()
MainApp().run()
#TestNavigationDrawer().run()