#!/usr/bin/env python3

from pathlib import Path
import qrcode
import qrcode.image.svg


def main():
    url = "https://github.com/CHTC/templates-GPUs"
    factory = qrcode.image.svg.SvgFillImage
    img = qrcode.make(url, image_factory=factory)

    figures_dir = Path.cwd() / "figures"
    figures_dir.mkdir(exist_ok=True)
    img.save(figures_dir / "qr_code.svg")


if __name__ == "__main__":
    main()
