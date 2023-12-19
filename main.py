from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url="https://discordapp.com/api/webhooks/1186620410368893020/qmlWVwu86fVMJGPIdQzhc4XXDMdP4W_REWwQH0DoB335AkuQm_MuWuOkxcQe2kf-ZXBF", content="Teste")
response = webhook.execute()
