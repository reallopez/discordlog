from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1190764428187152494/PpwcEP3GmqaeP7eEpBBMktgW72LAVzbv03Nvgri_Xy8LZVbt1PZRYsbv0pHmEu0hWXRl", content="Teste")
response = webhook.execute()
