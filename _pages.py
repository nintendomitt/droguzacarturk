# -*- coding: utf-8 -*-
"""Sayfa verileri. Icerik duzenlemek icin _pages_micro.py ve _pages_estetik.py."""

from _pages_lenfodem import LENFODEM
from _pages_micro import MICRO
from _pages_estetik import ESTETIK

SITE = {
    "base": "https://www.droguzacarturk.com",
    "published": "2026-08-01",
    "modified": "2026-08-13",
    "modifiedtr": "13 Ağustos 2026",
}

# Mevcut lenfodem sayfasi (elle bakimda) — ic linkleme icin kayit
LENFODEM_REF = {
    "key": "lenfodem",
    "slug": "lenfodem-lipodem-cerrahisi.html",
    "card": "Lenfödem cerrahisi",
    "cardsub": "LVA, lenf nodu transferi ve azaltıcı cerrahi",
}
# Anasayfadaki bolum baglantilari icin
KULAK_REF = {
    "key": "kulak-estetigi",
    "slug": "lip-lift-bisektomi-kulak-estetigi.html",
    "card": "Kulak estetiği",
    "cardsub": "Kepçe kulak (otoplasti) düzeltmesi",
}

PAGES = LENFODEM + MICRO + ESTETIK

# Ic link cozumlemesinde kullanilan, uretilmeyen kayitlar
EXTRA_REFS = [KULAK_REF]
