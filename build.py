"""Build the RentalFleetBook website (static HTML for GitHub Pages).

Run:  python3 build.py
Pages are written next to this file (index.html, features/.../index.html, ...).
Content lives in _src/; legal wording in _src/legal/*.body.html
(terms.body.html is generated from the app's src/content/terms.ts).
"""
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "_src"))

from layout import SITE  # noqa: E402
import pages_home, pages_features, pages_more  # noqa: E402

LEGAL = ROOT / "_src" / "legal"
out: dict[str, str] = {}
out["/"] = pages_home.home()
out["/features/"] = pages_features.features_hub()
for p in pages_features.PAGES:
    out[p["path"]] = pages_features.feature_page(p)
for s in pages_more.SOL:
    out[s["path"]] = pages_more.solution_page(s)
out["/pricing/"] = pages_more.pricing()
out["/about/"] = pages_more.about()
out["/security/"] = pages_more.security()
out["/contact/"] = pages_more.contact()
out["/privacy.html"] = pages_more.legal("/privacy.html", LEGAL / "privacy.body.html", "Privacy Policy | RentalFleetBook",
                                        "How RentalFleetBook handles personal information under the Privacy Act 1988 (Cth) and the Australian Privacy Principles.")
out["/terms.html"] = pages_more.legal("/terms.html", LEGAL / "terms.body.html", "Terms and Conditions | RentalFleetBook",
                                      "The terms and conditions for using RentalFleetBook, the car rental fleet management software.")
out["/404.html"] = pages_more.not_found()

for path, html in out.items():
    f = ROOT / (path.lstrip("/") + "index.html" if path.endswith("/") else path.lstrip("/"))
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(html, encoding="utf-8")

today = date.today().isoformat()
urls = [p for p in out if p != "/404.html"]
prio = lambda p: "1.0" if p == "/" else "0.9" if p.startswith(("/features/", "/integrations/", "/pricing/")) else "0.8" if p.startswith("/solutions/") else "0.5"
(ROOT / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{SITE}{p}</loc><lastmod>{today}</lastmod><priority>{prio(p)}</priority></url>\n" for p in urls)
    + "</urlset>\n", encoding="utf-8")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
print(f"Built {len(out)} pages")
