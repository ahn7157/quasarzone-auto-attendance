"""
quasar-zone auto attendance check
v0.3.0
"""
from autocheck.message.message import Message
from autocheck.user import User
from autocheck.check import Check


from autocheck.driver import Driver


def main():
    driver = Driver.create_web_drive()
    user = User()
    results = Check().check(driver, user)
    Message().send_message(user, results)


if __name__ == "__main__":
    main()
