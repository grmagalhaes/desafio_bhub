import locale
import os
from decimal import Decimal, InvalidOperation


def format_fiat(value, decimal_places=2):
    try:
        value_decimal = Decimal(value).__round__(decimal_places)
    except ValueError:
        value_decimal = value
    except (TypeError, InvalidOperation):
        value_decimal = Decimal(f"{value:2}")
    return locale.currency(Decimal(f"{value_decimal:{20}.{2}f}"), grouping=True, symbol=False).replace(".",
                                                                                                       "_").replace(",",
                                                                                                                    ".").replace(
        "_", ",")


def format_float_to_decimal(value) -> Decimal:
    return Decimal('{0:.4f}'.format(value))


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


