import threading
import os
import time

class FileChecker(threading.Thread):
  def __init__(self):
    super(FileChecker, self).__init__()
    self._stop_flag = False
    self.inicio = 0
    self.hora = 0

  def run(self):
      while True:
          time.sleep(0.1)
          if self.inicio == 3600:
              self.hora += 1
              self.inicio = 0

          text = "%02d:%02d:%02d" % (self.hora, self.inicio / 60, self.inicio % 60)
          # self.interface.emit(SIGNAL("updade(QString)"), text)
          #self.interface.setTime(text)

          self.inicio = self.inicio + 0.1
          self.inicio = round(self.inicio, 1)
          print(self.inicio)

          if self._stop_flag:
            break

  def stop(self):
    self._stop_flag = True
    self.join()

t = FileChecker()
t.start()

# ...

#t.stop()