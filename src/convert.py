#!/usr/bin/env python3
import asyncio
from pyppeteer import launch
import sys
import os


if len(sys.argv) != 3:
    print('Usage: ./convert.py <input.html> <output.xyz>')
    sys.exit(0)

_HTML = os.path.dirname(os.path.realpath(__file__)) + "/" + sys.argv[1]
_OUTFILE = sys.argv[2]
sourcepath = 'file://' + _HTML

async def generate_png():
    browser = await launch()
    page = await browser.newPage()
    await page.goto(sourcepath)
    await page.screenshot({'path': _OUTFILE, 'fullPage': False, 'clip':{'x':10, 'y':100, 'width':950, 'height':320}})
    await browser.close()


if ".png" in _OUTFILE or ".jpg" in _OUTFILE:
    asyncio.get_event_loop().run_until_complete(generate_png())