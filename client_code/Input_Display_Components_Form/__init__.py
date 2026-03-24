from ._anvil_designer import Input_Display_Components_FormTemplate
from anvil import *
import plotly.graph_objects as go

class Input_Display_Components_Form(Input_Display_Components_FormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("link_2", "click")
  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Layout_Components_Form')
    pass

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.text_box_1.text = "Hello!"
    pass
