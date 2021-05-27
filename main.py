from marketing_firm_creator import *

marketing_firm = choose_manager_type()
marketing_firm.create_sweepstakes()
sweepstake = marketing_firm.manager.get_sweepstakes()
for key in sweepstake.contestants:
    sweepstake.print_contestant_info_dict(sweepstake.contestants[key])
sweepstake.pick_winner()
sweepstake.publisher.dispatch()