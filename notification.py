from win10toast import ToastNotifier

toaster = ToastNotifier()

toaster.show_toast("Windows Notifications!!!",
                   "Have a Good day!",
                   icon_path="msg.ico")

#toaster.show_toast("Python Notifications",
#                   "Python is awsome by default!")
