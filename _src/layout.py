"""Shared page shell for the RentalFleetBook website: <head>, header with menus, footer."""
import html, json

SITE = "https://www.rentalfleetbook.com"
APP = "https://app.rentalfleetbook.com"
PHONE = "+61 448 019 043"
PHONE_HREF = "tel:+61448019043"

FEATURES = [
    ("/features/fleet-management/", "Fleet management", "Every car, its rego, insurance, documents and status"),
    ("/features/digital-rental-agreements/", "Digital rental agreements", "Your agreement, signed on screen, with inspections"),
    ("/integrations/xero/", "Invoices, payments & Xero", "Weekly invoices, reminders and bonds, synced with Xero"),
    ("/features/fines-and-tolls/", "Fines & tolls", "Notices read by AI, matched to the hirer, ready to nominate"),
    ("/features/fleet-maintenance/", "Servicing & maintenance", "Service schedules from your mechanic's invoices"),
    ("/features/gps-tracking/", "GPS tracking", "Live map, trips and kilometres for every car"),
]
SOLUTIONS = [
    ("/solutions/car-rental/", "Car rental businesses", "Run hires, billing and paperwork in one place"),
    ("/solutions/long-term-rental/", "Long-term & weekly rental", "Weekly billing, bonds and fines for long hires"),
    ("/solutions/small-fleets/", "Small rental fleets", "From 1 to 20 cars, set up in an afternoon"),
    ("/solutions/commercial-vehicle-hire/", "Commercial vehicle hire", "Utes, vans and trucks with km limits and servicing"),
]

ICONS = {
    "car": '<path d="M5 17h14M6.5 17v2M17.5 17v2M4 13l1.6-4.8A2 2 0 0 1 7.5 7h9a2 2 0 0 1 1.9 1.2L20 13v4H4z"/><circle cx="8" cy="14" r=".6"/><circle cx="16" cy="14" r=".6"/>',
    "sign": '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M8 17c1.5-2 2.5-2 3 0s1.8 1.4 3-.5"/>',
    "invoice": '<path d="M6 3h12v18l-3-2-3 2-3-2-3 2z"/><path d="M9 8h6M9 12h6M9 16h3"/>',
    "ticket": '<path d="M4 7a2 2 0 0 0 2-2h12a2 2 0 0 0 2 2v3a2 2 0 0 0 0 4v3a2 2 0 0 0-2 2H6a2 2 0 0 0-2-2v-3a2 2 0 0 0 0-4z"/><path d="M10 9v6M14 9v6"/>',
    "wrench": '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.2L4 16.8V20h3.2l5.3-5.3a4 4 0 0 0 5.2-5.4l-2.4 2.4-2.6-.6-.6-2.6z"/>',
    "pin": '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
    "inbox": '<path d="M4 13l2.5-7h11L20 13v6H4z"/><path d="M4 13h4.5l1 2h5l1-2H20"/>',
    "shield": '<path d="M12 3l7 3v5c0 4.5-3 8.3-7 10-4-1.7-7-5.5-7-10V6z"/><path d="M9 12l2 2 4-4"/>',
    "users": '<circle cx="9" cy="8" r="3"/><path d="M3.5 19a5.5 5.5 0 0 1 11 0M16 5.5a3 3 0 0 1 0 5.5M17.5 14.5A5 5 0 0 1 20.5 19"/>',
    "phone": '<rect x="7" y="3" width="10" height="18" rx="2"/><path d="M11 18h2"/>',
    "chart": '<path d="M4 20V4M4 20h16"/><path d="M8 16v-4M12 16V8M16 16v-6"/>',
    "clock": '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
    "bell": '<path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15z"/><path d="M10 20a2 2 0 0 0 4 0"/>',
    "truck": '<path d="M3 6h11v10H3zM14 9h4l3 3.5V16h-7z"/><circle cx="7" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/>',
    "calendar": '<rect x="4" y="5" width="16" height="15" rx="2"/><path d="M4 10h16M9 3v4M15 3v4"/>',
    "map": '<path d="M9 4L3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>',
    "camera": '<path d="M4 8h3l2-2.5h6L17 8h3v11H4z"/><circle cx="12" cy="13" r="3.5"/>',
    "lock": '<rect x="5" y="10.5" width="14" height="10" rx="2"/><path d="M8 10.5V8a4 4 0 0 1 8 0v2.5"/>',
    "cloud": '<path d="M7 18a4.5 4.5 0 0 1-.6-9A6 6 0 0 1 18 8.5a4.8 4.8 0 0 1-.5 9.5z"/>',
    "refresh": '<path d="M20 11a8 8 0 0 0-14.6-4.5M4 4v4h4M4 13a8 8 0 0 0 14.6 4.5M20 20v-4h-4"/>',
}


def icon(name: str) -> str:
    return f'<div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg></div>'


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def _menu(items):
    return "".join(f'<a href="{h}"><b>{esc(t)}</b><span>{esc(d)}</span></a>' for h, t, d in items)


def header() -> str:
    feats = _menu(FEATURES) + '<a href="/features/"><b>All features →</b></a>'
    sols = _menu(SOLUTIONS)
    mfeat = "".join(f'<a href="{h}">{esc(t)}</a>' for h, t, _ in FEATURES)
    msol = "".join(f'<a href="{h}">{esc(t)}</a>' for h, t, _ in SOLUTIONS)
    return f'''<header class="top"><div class="wrap">
<a class="brand" href="/" aria-label="RentalFleetBook home"><img src="/assets/icon.png" alt="" width="34" height="34"><span><b>RentalFleet</b><i>Book</i></span></a>
<nav class="nav" aria-label="Main">
<details class="dd"><summary>Features</summary><div class="menu">{feats}</div></details>
<details class="dd"><summary>Solutions</summary><div class="menu">{sols}</div></details>
<a href="/ai/">AI fleet manager</a><a href="/pricing/">Pricing</a><a href="/about/">About</a>
</nav>
<div class="actions"><a class="login" href="{APP}/login">Log in</a><a class="btn sm" href="/contact/">Book a demo</a><a class="btn primary sm" href="{APP}/signup">Start free</a></div>
<details class="mnav"><summary aria-label="Menu"><i></i></summary><div class="panel">
<h4>Features</h4>{mfeat}<a href="/features/">All features</a>
<h4>Solutions</h4>{msol}
<h4>Company</h4><a href="/ai/">AI fleet manager</a><a href="/pricing/">Pricing</a><a href="/about/">About</a><a href="/security/">Security</a><a href="/contact/">Contact</a><a href="{APP}/login">Log in</a>
<a class="btn primary" href="{APP}/signup">Start your free month</a><a class="btn" href="/contact/">Book a demo</a>
</div></details>
</div></header>'''


def footer() -> str:
    col = lambda items: "".join(f'<a href="{h}">{esc(t)}</a>' for h, t, _ in items)
    return f'''<footer><div class="wrap">
<div class="cols">
<div><a class="brand" href="/"><img src="/assets/icon.png" alt="" width="34" height="34"><span><b>RentalFleet</b><i>Book</i></span></a>
<p style="margin-top:14px;max-width:300px">The AI fleet manager for Australian car rental businesses. Built in Melbourne by a rental operator.</p>
<p><a href="{PHONE_HREF}" style="display:inline">{PHONE}</a></p></div>
<div><h4>Features</h4>{col(FEATURES)}</div>
<div><h4>Solutions</h4>{col(SOLUTIONS)}</div>
<div><h4>Company</h4><a href="/ai/">AI fleet manager</a><a href="/about/">About us</a><a href="/pricing/">Pricing</a><a href="/security/">Security</a><a href="/contact/">Contact &amp; demo</a></div>
<div><h4>Account</h4><a href="{APP}/signup">Start free</a><a href="{APP}/login">Log in</a><a href="/privacy.html">Privacy</a><a href="/terms.html">Terms</a></div>
</div>
<div class="base"><span>© <span id="y">2026</span> RentalFleetBook</span><span><a href="/privacy.html">Privacy policy</a> · <a href="/terms.html">Terms and conditions</a></span></div>
</div></footer>
''' + NAV_JS


NAV_JS = '''<script>document.getElementById("y").textContent=new Date().getFullYear();
document.querySelectorAll(".nav .dd").forEach(d=>d.addEventListener("toggle",()=>{if(d.open)document.querySelectorAll(".nav .dd").forEach(o=>{if(o!==d)o.open=false})}));
document.addEventListener("click",e=>{if(!e.target.closest(".nav .dd"))document.querySelectorAll(".nav .dd[open]").forEach(d=>d.open=false)});</script>'''


def page(path: str, title: str, desc: str, body: str, schema: list | None = None, crumbs: list | None = None) -> str:
    url = SITE + path
    ld = list(schema or [])
    ld.append({"@context": "https://schema.org", "@type": "Organization", "name": "RentalFleetBook", "url": SITE,
               "logo": SITE + "/assets/logo.png", "telephone": PHONE, "areaServed": "AU",
               "address": {"@type": "PostalAddress", "addressLocality": "Melbourne", "addressRegion": "VIC", "addressCountry": "AU"}})
    if crumbs:
        ld.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + p} for i, (n, p) in enumerate(crumbs)]})
    scripts = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    return f'''<!doctype html>
<html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0B1B3F">
<meta property="og:type" content="website"><meta property="og:site_name" content="RentalFleetBook">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/assets/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/icon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
{scripts}
</head>
<body>
{header()}
<main>
{body}
</main>
{footer()}
</body></html>
'''


def breadcrumbs(items) -> str:
    parts = [f'<a href="{p}">{esc(n)}</a>' for n, p in items[:-1]] + [esc(items[-1][0])]
    return '<div class="crumbs">' + " / ".join(parts) + "</div>"


def cta_band(title="Ready to spend less time on paperwork?", text="Try RentalFleetBook free for your first month. No credit card needed to start.") -> str:
    return f'''<section class="tight"><div class="wrap"><div class="ctaband">
<div><h2>{esc(title)}</h2><p>{esc(text)}</p></div>
<div class="cta"><a class="btn light" href="{APP}/signup">Start your free month <span class="arr">→</span></a><a class="btn ghost-light" href="/contact/">Book a demo</a></div>
</div></div></section>'''
