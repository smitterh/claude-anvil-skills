from ._anvil_designer import Layout_Components_FormTemplate
from anvil import *

class Layout_Components_Form(Layout_Components_FormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("link_1", "click")
  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Input_Display_Components_Form')
    pass
