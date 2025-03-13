from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import requests

class SlideControllerApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.show_ip_popup()
        return self.layout

    def show_ip_popup(self):
        # Create a popup for IP input
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Label
        content.add_widget(Label(text="Enter Server IP Address:"))

        # Text Input for IP
        self.ip_input = TextInput(multiline=False, font_size=20, size_hint=(1, 0.5))
        content.add_widget(self.ip_input)

        # Connect Button
        btn_connect = Button(text="Connect", size_hint=(1, 0.5))
        btn_connect.bind(on_press=self.connect_to_server)
        content.add_widget(btn_connect)

        # Create and open the popup
        self.popup = Popup(title="Server IP", content=content, size_hint=(0.8, 0.4))
        self.popup.open()

    def connect_to_server(self, instance):
        # Get the IP address from the input
        self.server_ip = self.ip_input.text
        self.popup.dismiss()  # Close the popup
        self.show_controller_ui()  # Show the main UI

    def show_controller_ui(self):
        # Clear the layout
        self.layout.clear_widgets()

        # Left Arrow Button (Previous Slide) - Red
        btn_prev = Button(text="←", font_size=50, size_hint=(0.5, 1))
        btn_prev.background_color = (1, 0, 0, 1)  # Red color
        btn_prev.bind(on_press=self.previous_slide)
        self.layout.add_widget(btn_prev)

        # Right Arrow Button (Next Slide) - Blue
        btn_next = Button(text="→", font_size=50, size_hint=(0.5, 1))
        btn_next.background_color = (0, 0, 1, 1)  # Blue color
        btn_next.bind(on_press=self.next_slide)
        self.layout.add_widget(btn_next)

    def next_slide(self, instance):
        # Send POST request to Flask server
        try:
            requests.post(f"http://{self.server_ip}:5000/next")
        except Exception as e:
            print(f"Error: {e}")

    def previous_slide(self, instance):
        # Send POST request to Flask server
        try:
            requests.post(f"http://{self.server_ip}:5000/previous")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    SlideControllerApp().run()
