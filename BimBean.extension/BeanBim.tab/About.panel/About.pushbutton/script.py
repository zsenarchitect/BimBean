from bimbean import b_about, b_error



@b_error.safe
def main():
    b_about.show_about()



main()