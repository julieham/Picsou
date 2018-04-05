from .models import *


class DataBaseManager:

    @staticmethod
    def create_budget(budget_name, month, prevision, spent):
        budget = Budget(name=budget_name, month=month, prevision=prevision, spent=spent)
        budget.save()
        return budget

    @staticmethod
    def spend_from_budget(budget, amount):
        budget.spent += amount
        budget.save()