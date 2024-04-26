import ui
import sys


app = ui.QApplication(sys.argv)
demo = ui.AppDemo()
demo.show()
sys.exit(app.exec_())
