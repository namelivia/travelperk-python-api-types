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
from travelperk_python_api_types.expenses.invoice_profiles.invoice_profiles import (
    InvoiceProfiles,
)
from travelperk_python_api_types.expenses.invoice_profiles.invoice_profile import (
    InvoiceProfile,
)
from travelperk_python_api_types.expenses.billing_information import BillingInformation
from travelperk_python_api_types.expenses.invoices.invoices import Invoices
from travelperk_python_api_types.expenses.invoices.invoice import Invoice
from travelperk_python_api_types.expenses.invoices.taxes_summary import TaxesSummary
from travelperk_python_api_types.expenses.invoices.travelperk_bank_account import (
    TravelperkBankAccount,
)
from travelperk_python_api_types.expenses.invoices.lines import Lines


class TestExpenses:
    def test_invoice_lines_entities_are_buildable(self):
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

    def test_invoice_profiles_entities_are_buildable(self):
        invoice_profiles = InvoiceProfiles(
            **{
                "offset": 0,
                "limit": 10,
                "total": 2,
                "profiles": [
                    {
                        "id": "f2dd1aa3-5601-4725-a520-bd59885bbb16",
                        "name": "My Company Ltd",
                        "payment_method_type": "automatic",
                        "billing_period": "instant",
                        "currency": "GBP",
                        "billing_information": {
                            "legal_name": "My Company Ltd",
                            "vat_number": "GB123456789",
                            "address_line_1": "199 Bishopsgate",
                            "address_line_2": "Spitalfields",
                            "city": "London",
                            "postal_code": "EC2M 3TY",
                            "country_name": "United Kingdom",
                        },
                    },
                    {
                        "id": "8fa66535-5a9a-4a6f-90d8-2986621a706a",
                        "name": "My Spanish Company SL",
                        "payment_method_type": "manual",
                        "billing_period": "monthly",
                        "currency": "EUR",
                        "billing_information": {
                            "legal_name": "My Spanish Company SL",
                            "vat_number": "ES123456789",
                            "address_line_1": "Passeig de Gracia 345",
                            "address_line_2": "Planta 14",
                            "city": "Barcelona",
                            "postal_code": "080123",
                            "country_name": "Spain",
                        },
                    },
                ],
            }
        )
        assert type(invoice_profiles) is InvoiceProfiles
        assert type(invoice_profiles.profiles[0]) is InvoiceProfile
        assert (
            type(invoice_profiles.profiles[0].billing_information) is BillingInformation
        )

    def test_invoice_entities_are_buildable(self):
        invoices = Invoices(
            **{
                "total": 1,
                "offset": 0,
                "limit": 10,
                "invoices": [
                    {
                        "serial_number": "INV-01-987654",
                        "profile_id": "edb6322b-8e11-48e9-8d6f-6402e445e50d",
                        "profile_name": "My Company Ltd",
                        "billing_information": {
                            "legal_name": "My Company Ltd",
                            "vat_number": "GB123456789",
                            "address_line_1": "199 Bishopsgate",
                            "address_line_2": "Spitalfields",
                            "city": "London",
                            "postal_code": "EC2M 3TY",
                            "country_name": "United Kingdom",
                        },
                        "mode": "reseller",
                        "status": "paid",
                        "issuing_date": "2020-03-31",
                        "billing_period": "monthly",
                        "from_date": "2020-03-01",
                        "to_date": "2020-03-31",
                        "due_date": "2020-04-15",
                        "currency": "EUR",
                        "total": "13579.24",
                        "lines": {
                            "total": 15,
                            "data": [
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
                            "next": "/invoices/lines?serial_number=INV-01-987654&offset=10",
                        },
                        "taxes_summary": [
                            {
                                "tax_regime": "STAR",
                                "subtotal": "6543.21",
                                "tax_percentage": "0.00",
                                "tax_amount": "0.00",
                                "total": "6543.21",
                            },
                            {
                                "tax_regime": "G-VAT-R",
                                "subtotal": "5912.63",
                                "tax_percentage": "19.00",
                                "tax_amount": "1123.40",
                                "total": "7036.03",
                            },
                        ],
                        "reference": "My Company Ltd - SEPA - Monthly 2020-03",
                        "travelperk_bank_account": {
                            "bank_name": "La Caixa",
                            "account_number": "ES01 2345 6789 1098 7654 3210",
                            "bic": "CAIX ES BB XXX",
                            "reference": "INV-01-987654",
                        },
                        "pdf": "https://api.travelperk.com/invoices/INV-01-987654/pdf",
                    }
                ],
            }
        )
        assert type(invoices) is Invoices
        assert type(invoices.invoices[0]) is Invoice
        assert type(invoices.invoices[0].billing_information) is BillingInformation
        assert type(invoices.invoices[0].taxes_summary[0]) is TaxesSummary
        assert (
            type(invoices.invoices[0].travelperk_bank_account) is TravelperkBankAccount
        )
        assert type(invoices.invoices[0].lines) is Lines
        assert type(invoices.invoices[0].lines.data[0]) is InvoiceLine
