import unittest
from unittest.mock import MagicMock
from datetime import date
from repositories.services.member_service import MemberService
from src.library_member import LibraryMember


class TestMemberService(unittest.TestCase):
    def setUp(self):
        self.mock_repo = MagicMock()
        self.service = MemberService(self.mock_repo)

        self.member = LibraryMember(
            member_id="M100",
            first_name="John",
            last_name="Doe",
            date_of_birth=date(1990, 1, 1),
            email="john@example.com",
            phone="123456789",
            address="123 Main St",
            registration_date=date.today(),
            member_type="Standard",
            account_status="Active"
        )

    def test_register_member(self):
        self.service.register_member(self.member)
        self.mock_repo.save.assert_called_once_with(self.member)

    def test_find_member_success(self):
        self.mock_repo.find_by_id.return_value = self.member
        result = self.service.find_member("M100")
        self.assertEqual(result, self.member)

    def test_find_member_not_found(self):
        self.mock_repo.find_by_id.return_value = None
        with self.assertRaises(ValueError):
            self.service.find_member("M999")

    def test_deactivate_member_success(self):
        self.mock_repo.find_by_id.return_value = self.member
        self.result = self.service.deactivate_member("M100")
        self.assertEqual(self.member.account_status, "Inactive")
        self.mock_repo.save.assert_called_with(self.member)

    def test_deactivate_member_not_found(self):
        self.mock_repo.find_by_id.return_value = None
        with self.assertRaises(ValueError):
            self.service.deactivate_member("M999")


if __name__ == '__main__':
    unittest.main()
