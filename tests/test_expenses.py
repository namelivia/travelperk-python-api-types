from travelperk_python_api_types.expenses.invoice_lines.invoice_lines import (
    InvoiceLines,
)
from travelperk_python_api_types.expenses.invoice_lines.invoice_line import (
    InvoiceLine,
)
from travelperk_python_api_types.expenses.invoice_lines.metadata import (
    Metadata,
)
from travelperk_python_api_types.expenses.invoice_lines.user import (
    User,
)
from travelperk_python_api_types.expenses.invoice_lines.vendor import (
    Vendor,
)


class TestExpenses:
    def test_expenses_entities_are_buildable(self):

        # Building nesting dictionaries
        invoice_lines = InvoiceLines(
            **{
                "total": 1,
                "offset": 0,
                "limit": 10,
                "invoice_lines": [
                    {
                        "expense_date": "2020-02-13",
                        "description": "FLIGHT for Trip ID 1687664",
                        "quantity": 1,
                        "unit_price": "20.00000000",
                        "non_taxable_unit_price": "0E-8",
                        "tax_percentage": "0E-8",
                        "tax_amount": "0E-8",
                        "tax_regime": "STAR",
                        "total_amount": "20.00000000",
                        "metadata": {
                            "trip_id": 1687664,
                            "trip_name": "Meeting with German company GmbH",
                            "service": "flight",
                            "travelers": [
                                {
                                    "name": "John Doe",
                                    "email": "john.doe@mycompany.com",
                                    "external_id": "ASD123",
                                }
                            ],
                            "start_date": "2020-03-27",
                            "end_date": "2020-04-05",
                            "cost_center": "DACH Accounts",
                            "labels": ["Sales trips", "Special"],
                            "vendor": {"code": "LH", "name": "Lufthansa"},
                            "out_of_policy": False,
                            "approvers": [
                                {
                                    "name": "Jake Bolt",
                                    "email": "jake.bolt@mycompany.com",
                                    "external_id": "ASD124",
                                }
                            ],
                            "booker": {
                                "name": "Marien Lint",
                                "email": "marien.lint@mycompany.com",
                                "external_id": "ASD124",
                            },
                        },
                        "invoice_serial_number": "INV-01-190111",
                        "profile_id": "09d649d1-35fa-4d9f-b688-046d5790afd2",
                        "profile_name": "My Company Ltd",
                        "invoice_mode": "reseller",
                        "invoice_status": "paid",
                        "issuing_date": "2020-02-13",
                        "due_date": "2020-02-13",
                        "currency": "EUR",
                    }
                ],
            }
        )
        assert type(invoice_lines) is InvoiceLines
        assert type(invoice_lines.invoice_lines[0]) is InvoiceLine
        assert type(invoice_lines.invoice_lines[0]) is InvoiceLine
        assert type(invoice_lines.invoice_lines[0].metadata) is Metadata
        assert type(invoice_lines.invoice_lines[0].metadata.vendor) is Vendor
        assert type(invoice_lines.invoice_lines[0].metadata.travelers[0]) is User
        assert type(invoice_lines.invoice_lines[0].metadata.approvers[0]) is User
