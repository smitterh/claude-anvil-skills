from ._anvil_designer import Layout_Components_FormTemplate
from anvil import *

class Layout_Components_Form(Layout_Components_FormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
