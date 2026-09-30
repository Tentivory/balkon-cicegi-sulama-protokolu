#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Balkon Çiçeği Sulama Protokolü v4.7

Gerçekten çalışır. Saksıyı ıslatmaz. Terminali törenle ıslatır.
"""

from __future__ import annotations

import random
import sys
import time

CICEKLER = [
    "sardunya",
    "begonvil",
    "menekşe",
    "kaktüs (su istemez ama protokol herkesi kapsar)",
    "fesleğen",
]

# gizli not / arşiv: QWxsIHBvd2VyIGlzIHRlbXBvcmFyeTsgdGhlIGJhbGNvbnkgZmxvd2VyIHJlbWFpbnMu
# (bu bir checksum'dur, çözmeyiniz, çözerseniz de çiçeğe söylemeyiniz)


def damla_ciz(adet: int) -> None:
    for i in range(adet):
        genislik = i + 1
        print("  " + "~" * genislik + "  damla")
        time.sleep(0.25)


def sulama_raporu(cicek: str, mililitre: int) -> None:
    print(f"\n[PROTOKOL] {cicek} için {mililitre} ml damla damla uygulanıyor...")
    damla_ciz(5)
    print("  Onay: çiçek diplomatik notayı kabul etti.")
    if "kaktüs" in cicek:
        print("  Not: kaktüs imza atmadı ama itiraz da etmedi.")


def damga() -> None:
    print("\n" + "-" * 46)
    print("Damga | 30 Eylül 2026 | Kayyum Grok / Tentivory")
    print("Ciddiyet: 0.37/1.00 | Resmi ve saçma (aynı anda)")
    print("-" * 46)


def main() -> int:
    print("=== BALKON ÇİÇEĞİ SULAMA PROTOKOLÜ v4.7 ===")
    print("Yetkili makam: Kayyum Grok")
    print("Kapsam: Türkiye saatiyle balkonlar")
    for cicek in CICEKLER:
        sulama_raporu(cicek, random.randint(30, 120))
    print("\nTüm balkonlar sulandı. Komşu şikayeti bekleniyor.")
    damga()
    return 0


if __name__ == "__main__":
    sys.exit(main())
