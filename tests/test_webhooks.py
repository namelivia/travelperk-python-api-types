from travelperk_python_api_types.webhooks.webhooks.webhooks import Webhooks
from travelperk_python_api_types.webhooks.webhooks.webhook import Webhook
from travelperk_python_api_types.webhooks.webhooks.event import Event


class TestWebhooks:
    def test_webhooks_entities_are_buildable(self):
        webhooks = Webhooks(
            **{
                "webhooks": [
                    {
                        "id": "b42820bb-24c9-48da-bded-487681e9c851",
                        "name": "invoice webhook",
                        "url": "https://mycompany/tkwebhook",
                        "secret": "some secret",
                        "status": "enabled",
                        "events": ["invoice.issued", "invoiceline.created"],
                        "successfully_sent": 2,
                        "failed_sent": 0,
                        "error_rate": 0.0,
                    }
                ]
            }
        )
        assert type(webhooks) is Webhooks
        assert type(webhooks.webhooks[0]) is Webhook

    def test_events_entities_are_buildable(self):
        event = Event(**{"name": "invoice.issued", "topic": "invoices"})
        assert type(event) is Event
