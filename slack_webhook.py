'''

A Slack webhook is a special URL that lets other applications send messages inyo Slack channels automatically.

If we know the URL, we can post structured data (usually JSON) and slack will display it as a message.

-------------------------------------------------------------------------------------------------------------------------------------

A webhook in general is a way for one system to notify another system in real time by sending an HTTP request.


A slack webhook url is always tied to a specific workspace and channel, where external apps can push messages.


Examples:

        A server crash triggers a webhook message in Slack.
        CI/CD pipeline posts “✅ Build succeeded” or “❌ Build failed.”

Example of a Slack Webhook URL

    A webhook URL looks like this (unique to your workspace and channel):

    T00000000 → Workspace ID
    B00000000 → Channel ID
    XXXXXXXXXXXXXXXXXXXXXXXX → Secret token

    You send a JSON payload to this URL, for example:

    {
    "text": "New order received: 2 T-shirts for Alice 🎉"
    }


Slack will then post that message into the chosen channel.

---------------------------------------------------------------------------------------------------------------------------------

NOTE :-


We can configure slack webhook url's in databricks workspace settings > notifications.

And attach slack channel to databricks job notifications.


'''