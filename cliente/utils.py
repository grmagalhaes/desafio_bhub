import os


def hardening_header():
    # reforçando a segurança do header

    CORS_ORIGIN_WHITELIST = os.environ.get('CORS_ORIGIN_WHITELIST'),
    hostname = CORS_ORIGIN_WHITELIST[0].split("/")[2]
    colon_pos = hostname.find(":")
    if colon_pos != -1:
        hostname = hostname[0:colon_pos]

    header = {
        "Server": "",
        "Cache-Control": "no-cache",
        "X-XSS-Protection": "1; mode=block",
        "X-Frame-Options": "DENY",
        "X-Content-Type-Options": "nosniff",
        "X-DNS-Prefetch-Control": "on",
        "Content-Security-Policy": f"default-src 'self' {hostname} *.{hostname}",
        "X-Download-Option": "noopen",
        "Strict-Transport-Security": "max-age=63072000; includeSubDomains; preload",
        "Expect-CT": "max-age=86400, enforce",
        "Referrer-Policy": "same-origin",
    }
    return header


