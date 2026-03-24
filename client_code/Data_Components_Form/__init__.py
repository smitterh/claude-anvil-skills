from ._anvil_designer import Data_Components_FormTemplate
from anvil import *


class Data_Components_Form(Data_Components_FormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("link_2", "click")
  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Layout_Components_Form')
    pass
