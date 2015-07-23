from gi.repository import Gtk


class EntryWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="tip calculator")
        self.set_size_request(200, 100)
        hbox = Gtk.Box(spacing=6)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)
        self.add(hbox)
        self.timeout_id = None
        self.entry = Gtk.Entry()
        self.entry.set_text("cost")
        
        button = Gtk.Button("Click Me")
        button.connect("clicked", self.nothing)
        
        hbox.pack_start(button, True, True, 1)
        vbox.pack_start(self.entry, True, True, 0)

    def nothing(self):
        pass

def ask_user():
    service = input('how would you rate your service? was it great,okay,bad, or horrible ')
    bill = input('how much did your meal cost? ')
    return (service, float(bill))


def calculate(service, bill):
    if service == 'great':
        return bill / 4
    if service == 'okay':
        return bill / 5
    if service == 'bad':
        return bill / 6.6666666
    if service == 'horrible':
        return bill / 10

service, bill = ask_user()
print(round(calculate(service, bill), 2))

win = EntryWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
