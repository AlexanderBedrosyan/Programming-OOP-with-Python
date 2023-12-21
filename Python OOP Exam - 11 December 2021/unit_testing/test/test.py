from project.team import Team
import unittest


class Tests(unittest.TestCase):

    def test_init_creates_all_attributes(self):
        team = Team('Gosho')
        self.assertEqual(team.name, 'Gosho')
        self.assertEqual(team.members, {})

    def test_if_name_raise_value_error_if_not_alpha(self):
        with self.assertRaises(ValueError) as ex:
            team = Team("2")
        self.assertEqual(str(ex.exception), "Team Name can contain only letters!")

    def test_if_attribute_error_comes_if_there_is_wrong_validation(self):
        with self.assertRaises(AttributeError) as ex:
            team = Team(2)
        self.assertEqual(str(ex.exception), "'int' object has no attribute 'isalpha'")

    def test_if_successfully_add_members(self):
        team = Team('Gosho')
        result = team.add_member(a=3, b=5, c=6)
        self.assertEqual(result, f"Successfully added: a, b, c")
        result2 = team.members
        self.assertEqual(result2, {
            'a': 3,
            'b': 5,
            'c': 6
        })
        result3 = team.add_member(a=3)
        self.assertEqual(result3, f"Successfully added: ")

    def test_remove_members_if_the_current_member_doesnt_exist(self):
        team = Team('Gosho')
        team.add_member(a=3, b=5)
        result = team.remove_member('Pesho')
        self.assertEqual(result, f"Member with name Pesho does not exist")

    def test_remove_members_if_remove_is_successfully_done(self):
        team = Team('Gosho')
        team.add_member(a=3, b=5)
        result = team.remove_member('a')
        self.assertEqual(result, f"Member a removed")
        result2 = team.members
        self.assertEqual(result2, {
            'b': 5
        })

    def test_gt_if_greater_works_correctly(self):
        team = Team('Gosho')
        team.add_member(a=3, b=5, c=3)
        team2 = Team('Tosho')
        team2.add_member(a=3, b=5)
        self.assertEqual(team > team2, True)

    def test_gt_if_less_than_works_correctly(self):
        team = Team('Gosho')
        team.add_member(a=3, b=5)
        team2 = Team('Tosho')
        team2.add_member(a=3, b=5, c=3)
        self.assertEqual(team > team2, False)
        team3 = Team('Rosho')
        team3.add_member(a=3, b=5)
        self.assertEqual(team > team2, False)

    def test_len_count_of_members(self):
        team = Team('Gosho')
        team.add_member(a=3, b=5)
        result = len(team)
        self.assertEqual(result, 2)
        team2 = Team('Gosho')
        self.assertEqual(len(team2), 0)

    def test_add_if_added_correctly(self):
        team = Team('Gosho')
        team.add_member(a=3)
        team2 = Team('Tosho')
        team2.add_member(c=3)
        team3 = team + team2
        result_name = team3.name
        result_members = team3.members
        self.assertEqual(result_name, 'GoshoTosho')
        self.assertEqual(result_members, {
            'a': 3,
            'c': 3
        })
        team4 = team2 + team
        result_name4 = team4.name
        needed_result = 'ToshoGosho'
        result_member4 = team4.members
        self.assertEqual(result_name4, 'ToshoGosho')
        self.assertEqual(result_member4, {'c': 3, 'a': 3})

    def test_str_if_give_correct_result(self):
        team = Team('Gosho')
        team.add_member(a=3, b=5, c=4)
        result = str(team)
        needed_result = "Team name: Gosho\nMember: b - 5-years old\nMember: c - 4-years old\nMember: a - 3-years old"
        self.assertEqual(result, needed_result)
        team2 = Team('Gosho')
        result2 = str(team2)
        self.assertEqual(result2, 'Team name: Gosho')

        new_team = Team('Gosho')
        new_team.add_member(B=4, A=4)
        result3 = str(new_team)
        needed_result2 = "Team name: Gosho\nMember: A - 4-years old\nMember: B - 4-years old"
        self.assertEqual(result3, needed_result2)

    def test_add_member_with_existing_names(self):
        team = Team('Gosho')
        team.add_member(a=3, b=5)
        result = team.add_member(a=7, c=9, b=11)
        self.assertEqual(result, f"Successfully added: c")
        result2 = team.members
        self.assertEqual(result2, {
            'a': 3,
            'b': 5,
            'c': 9
        })

