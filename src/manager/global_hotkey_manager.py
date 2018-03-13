import logging

from PyQt5 import QtCore

from PyQt5.QtCore import QObject
from pynput.keyboard import Key, Listener

from src.reference.reference import toggle_global_app, get_global_thread


class Hotkey(QObject):
    COMBINATIONS = [
        {Key.ctrl_l, Key.ctrl_r},
    ]

    current = set()
    thread = None

    def give_thread(self, thread):
        self.thread = thread

    def execute(self):
        pass
        #TODO
        toggle_global_app()

    def on_press(self, key):
        try:
            if any([key in COMBO for COMBO in self.COMBINATIONS]):
                self.current.add(key)
                if any(all(k in self.current for k in COMBO) for COMBO in self.COMBINATIONS):
                    self.execute()
        except Exception:
            pass;

    def on_release(self, key):
        try:
            if any([key in COMBO for COMBO in self.COMBINATIONS]):
                self.current.remove(key)
        except Exception:
            pass

    @QtCore.pyqtSlot()
    def start(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
