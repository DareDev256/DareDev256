import sys, asyncio
from playwright.async_api import async_playwright
OUT = sys.argv[1]
SITES = [("kmoney","https://officialkmoney.com"),("100bandplan","https://100bandplan.com"),("savv4x","https://savv4x.com"),
         ("whyg35","https://whyg35.com"),("streetbud","https://officialstreetbud.com"),("shortiie","https://shortiieraw.com"),
         ("studio","https://www.jamesdare.com/?walkin=0")]
async def one(b, name, url):
    ctx = await b.new_context(viewport={"width":1440,"height":900}, device_scale_factor=1, reduced_motion="no-preference")
    p = await ctx.new_page()
    try:
        await p.goto(url, wait_until="networkidle", timeout=45000)
    except Exception as e:
        print(name, "goto warn", e)
    await p.wait_for_timeout({"studio":9000,"whyg35":13000}.get(name,4500))
    await p.screenshot(path=f"{OUT}/{name}.png")
    print(name, "ok")
    await ctx.close()
async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch(headless=True, args=["--use-angle=metal","--enable-gpu","--ignore-gpu-blocklist"])
        await asyncio.gather(*[one(b,n,u) for n,u in SITES])
        await b.close()
asyncio.run(main())
