#!/usr/bin/env python3

from pathlib import Path
import qrcode
import qrcode.image.svg


def main():
    url = "https://doi.org/10.25080/nwuf8465"
    factory = qrcode.image.svg.SvgFillImage
    img = qrcode.make(url, image_factory=factory)

    figures_dir = Path.cwd() / "figures"
    figures_dir.mkdir(exist_ok=True)
    img.save(figures_dir / "qr_code.svg")


if __name__ == "__main__":
    main()
