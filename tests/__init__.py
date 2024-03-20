
"""
the command to do unittesting, taken from the GeekTrust default readme

    python -m unittest discover
    coverage run -m unittest discover
    python -m coverage run -m unittest

it didn't work so try

installing coverage with
    pip install --user coverag

"""
import unittest
from portfolio_balances import Portfolio
from input_reader import FileReader
from asset_classes import AssetClass
import coverage
print(coverage.__file__)


class TestingPortfolioClass(unittest.TestCase): #unit test cleared by GeekTrust
    def test_target_allocation_upon_portfolio_construction(self):
        #ARRANGE
        portfolio_instance = Portfolio() #not sure why I need to instantiate this
        hypothetical_equities = 17000
        hypothetical_debt = 2000
        hypothetical_gold = 1000
        hypothetical_allocation_inputs = [hypothetical_equities,hypothetical_debt,hypothetical_gold]
        expected_output_allocation = {'equities': 0.85, 'debt': 0.1, 'gold': 0.05}
        #ACT
        portfolio_instance._create_new_asset_classes(hypothetical_allocation_inputs) ##proces the hypotheticals
        # ASSERT, https://docs.python.org/3/library/unittest.html
        actual_results = portfolio_instance._get_target_allocations() #this only worked bc I had a GET function made, could test it out later by touching the field directly?
        self.assertEqual(expected_output_allocation, actual_results)


class TestingAssetClassClass(unittest.TestCase): ##Geektrust says this one def works
    def test_data_type_asset_class_balance(self):
        #ARRANGE
        hypothetical_asset_class_name_initialized = "gold"
        hypothetical_asset_class_cash_deposited = 28537 #has to be an integer
        expected_data_type_asset_class_balance = int
        #ACT
        asset_class_instance = AssetClass(hypothetical_asset_class_name_initialized, hypothetical_asset_class_cash_deposited)
        # ASSERT, https://docs.python.org/3/library/unittest.html
        actual_data_type_asset_class_balance = type(asset_class_instance._get_current_balance())
        self.assertEqual(expected_data_type_asset_class_balance, actual_data_type_asset_class_balance)

    def test_1001_balance_losing_17_percent(self):
        #ARRANGE
        hypothetical_starting_balance = 1001
        asset_class_instance = AssetClass("equities", hypothetical_starting_balance)
        sample_change_in_value_percentage = -0.17
        expected_new_balance = 830 # 1001 minus 17% = 830.83, but it should be rounded down to 830
        #ACT
        asset_class_instance._change_balance_percentage(sample_change_in_value_percentage)
        # ASSERT, https://docs.python.org/3/library/unittest.html
        actual_new_balance = asset_class_instance._get_current_balance()
        self.assertEqual(expected_new_balance , actual_new_balance)

    def test_debt_rebalancing(self):
        #ARRANGE
        hypothetical_starting_balance = 2000
        hypothetical_requested_rebalance = 3000
        asset_class_instance = AssetClass("debt", hypothetical_starting_balance)
        desired_debt_balance_after_rebalance = 3000
        expected_new_balance = desired_debt_balance_after_rebalance # 1 to 1 change
        #ACT
        asset_class_instance._rebalance_to_set_value(hypothetical_requested_rebalance)
        # ASSERT, https://docs.python.org/3/library/unittest.html
        actual_new_balance = asset_class_instance._get_current_balance()
        self.assertEqual(expected_new_balance , actual_new_balance)

if __name__ == '__main__':
    unittest.main()



