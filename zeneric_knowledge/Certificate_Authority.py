'''
What is a CA?
---------------------------------------------------------------------------------------------------------------

CA = Certificate Authority - an organization that issues digital certificates that proves "this website/server is actually who it claims to be."

CA provides SSL/TLS certificate to website/servers.


Think of it like a passport:

    you = the website/server
    passport = the SSL certificate
    Goverment issuing the passport = the CA
    Border control trusting the passport = browser/OS trust store

Example CA organizations: DigiCert.



Public website (nike.com):
    Browser has DigiCert in it's trust store -> nike is signed by DigiCert -> So it can access it.

Internal Nike websites:
    Browser/Python May not have Nike TLS CA in it's trust store -> internal website is signed by Nike TLS CA but not by DigiCert -> So browser/python can't access it.




So in case of building Datahub cursor MCP, the cursor process might not have Nike TLS CA in it's trust store list. So it cannot access Nike GMS server.

The error will be something like this:

    SSL: CERTIFICATE_VERIFY_FAILED


Cursor (like almost every app) trusts DigiCert and ~150 other public CAs. Cursor inherits the trust store from somewhere else - it doesn't maintain its own.

'''