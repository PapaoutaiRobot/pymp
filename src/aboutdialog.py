#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AboutDialog(object):
  def __init__(self,name,url,bugs):
    self.name=name
    self.url=url
    self.bugtracker=bugs
  
  def setupUi(self, Dialog):
    #prepare the window
    Dialog.setObjectName(_fromUtf8("Dialog"))
    Dialog.resize(800, 480)

    #the layout
    self.layout=QtGui.QVBoxLayout(Dialog)
    self.setLayout(self.layout)
    #some tabs
    self.tabs=QtGui.QTabWidget(Dialog)
    self.layout.addWidget(self.tabs)
    #some browsers
    self.browserDonate=QtGui.QTextBrowser(self.tabs)
    self.browserGeneral=QtGui.QTextBrowser(self.tabs)
    self.browserWebsite=QtGui.QTextBrowser(self.tabs)
    self.browserFeedback=QtGui.QTextBrowser(self.tabs)
    #insert the tabs
    tabCnt=1
    self.tabs.insertTab(tabCnt, self.browserGeneral,
                        QtGui.QApplication.translate(
                                                     "Dialog", "&General", None, 
                                                     QtGui.QApplication.UnicodeUTF8))
    tabCnt+=1
    self.tabs.insertTab(tabCnt, self.browserFeedback,
                        QtGui.QApplication.translate(
                                                     "Dialog", "&Feedback", None, 
                                                     QtGui.QApplication.UnicodeUTF8))
    tabCnt+=1
    self.tabs.insertTab(tabCnt, self.browserWebsite,
                        QtGui.QApplication.translate(
                                                     "Dialog", "&Website", None, 
                                                     QtGui.QApplication.UnicodeUTF8))
    tabCnt+=1
    self.tabs.insertTab(tabCnt, self.browserDonate,
                        QtGui.QApplication.translate(
                                                     "Dialog", "&Donate", None, 
                                                     QtGui.QApplication.UnicodeUTF8))

    
    #uff nearly done
    self.retranslateUi(Dialog)
    QtCore.QMetaObject.connectSlotsByName(Dialog)

  def retranslateUi(self, Dialog):
    Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog",self.name, None, QtGui.QApplication.UnicodeUTF8))
    self.browserDonate.setText(
        "You like what you have in your hands? You use it on regular basis? "\
        "Support the development by making a donation."\
        "<p>Donate through "\
        "<a href=\"https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=TPX9PV29D4L9Y\">paypal</a></p>"\
        "<p>Visit the projects <a href=\"https://sites.google.com/site/markusscharnowski/donate\">donation website</a></p>"
        )
    self.browserWebsite.setText(
        "<p>Visit</p>"\
        "<p>"\
        "<a href=\""+ self.url + "\">" + self.url + "</a>"\
        "</p>"\
        "<p>"\
        "<a href=\"http://sites.google.com/site/markusscharnowski\">http://sites.google.com/site/markusscharnowski</a>"\
        "</p>"
        )
    self.browserFeedback.setText(
        "<p>Do you have ideas for improving the program? You want a specific functionality? "
        "You have found a bug?</p>"
        "<p><a href=\""+self.bugtracker+"\">Bugtracker</a></p>"
        "<p>Email <a href=\"mailto:markus.scharnowski@gmail.com?subject=SW Feedback " + self.windowTitle() +
        " &body=Hello Markus,\">Feedback</a></p>"
        )
    self.browserGeneral.setText(
        "<p>" + self.name + "</p>"\
        "<p>Concept and programming: <a href=\"mailto:markus.scharnowski@gmail.com?subject=Thank you for " + self.name +
        "&body=Hello Markus,\">Markus Scharnowski</a></p>"
        )

if __name__ == '__main__':
  import sys
  class MyWindow(QtGui.QDialog, Ui_AboutDialog): 
    def __init__(self,name,url,bugs):
      self.name=name
      self.url=url
      self.bugtracker=bugs
      QtGui.QDialog.__init__(self) 
      self.setupUi(self)

  app = QtGui.QApplication(sys.argv) 
  dialog = MyWindow("123","http://sites.google.com/site/markusscharnowski/123","http://code.google.com/p/push-it/issues/list") 
  dialog.show() 
  sys.exit(app.exec_())