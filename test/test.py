def __init__(self, completer_widget, max_visible_items=7, sort_func=sort_key):
    QListView.__init__(self)
    self.disable_popup = False
    self.completer_widget = weakref.ref(completer_widget)
    self.setWindowFlags(Qt.Popup)
    self.max_visible_items = max_visible_items
    self.setEditTriggers(self.NoEditTriggers)
    self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.setSelectionBehavior(self.SelectRows)
    self.setSelectionMode(self.SingleSelection)
    self.setAlternatingRowColors(True)
    self.setModel(CompleteModel(self, sort_func=sort_func))
    self.setMouseTracking(True)
    self.entered.connect(self.item_entered)
    self.activated.connect(self.item_chosen)
    self.pressed.connect(self.item_chosen)
    self.installEventFilter(self)