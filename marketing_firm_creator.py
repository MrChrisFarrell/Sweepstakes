from sweepstakes_queue_manager import SweepstakesQueueManager
from sweepstakes_stack_manager import SweepstakesStackManager
from marketing_firm import MarketingFirm
from user_interface import *


def choose_manager_type():
    manager_type = get_input("Enter '1' for stack manager or '2' for queue manager - ")
    if manager_type == '1':
        manager_type = SweepstakesStackManager()
    elif manager_type == '2':
        manager_type = SweepstakesQueueManager()
    marketing_firm = MarketingFirm(manager_type)
    return marketing_firm
