from layout import APP, FEATURES, SOLUTIONS, cta_band, esc, icon, page
import mocks

HOME_FAQ = [
    ("What does the AI actually do?", "It reads documents for you: infringement and toll notices, mechanic invoices, rego notices, insurance papers and driver licence photos. It pulls out the details, files them against the right car and hire, and fills in the forms. You always see what it read and can correct it before anything is relied on."),
    ("Do I need Xero?", "Xero is recommended, because customers, invoices, repeating invoices and payments then sync automatically. You can start without it and connect it later."),
    ("Does it work outside Victoria?", "Yes. Hires, agreements, billing, servicing and GPS work anywhere in Australia. A few time-savers, such as reading VicRoads renewal notices and Victorian council and toll links, are tuned for Victoria first."),
    ("Can I use my own rental agreement?", "Yes. Upload your agreement as a Word file or PDF. Your wording stays exactly as it is; the hirer's details, vehicle, dates and amounts become blanks that fill in for each hire."),
    ("Can my staff use it?", "Yes. Add your team with their own logins and roles (owner, manager, finance or yard staff) at no extra cost."),
    ("Where is my data kept?", "In Australia (Sydney region), encrypted, with daily backups. Licence photos and documents are private to your company."),
    ("What happens after the free month?", "Add a card in Billing at any time and you're charged monthly by fleet size. If you don't, your account pauses and nothing is charged."),
]

COMPARE = [
    ("Weekly rent invoices", "Create or copy invoices by hand, chase payments in your inbox", "First invoice and weekly repeating invoice set up in Xero when the agreement is signed"),
    ("Traffic fines", "Work out who had the car, type their details into the council site", "Notice read by AI and matched to the hirer; details ready to copy into the nomination"),
    ("Rental agreements", "Print, sign, scan, email, file", "Signed on screen with pickup photos, then emailed with the insurance papers"),
    ("Servicing", "Odometer readings and service dates in a spreadsheet", "Mechanic invoices read by AI; overdue services stand out"),
    ("Overdue rent", "Check Xero, text each hirer one by one", "One overdue list, with SMS and email reminders showing the total owing"),
    ("Rego and insurance", "Renewal dates kept in your head or a calendar", "Every car's rego, insurance and documents in one place, with what's due"),
]


APPROVE_ROWS = [
    ("Fine", "crit", "Speed camera notice · $363", "Matched to hirer J. Nguyen · nomination ready", "ZQR418"),
    ("Toll", "warn", "CityLink trip · $11.24", "Added to A. Patel's weekly invoice", "1XT9KD"),
    ("Service", "info", "Mechanic invoice · 60,000 km service", "Service history updated · next due at 70,000 km", "BHL207"),
    ("Rego", "ok", "VicRoads renewal · due 14 Dec", "Expiry updated · bill drafted in Xero", "AAK55M"),
]
APPROVE = ('<div class="mini approve"><h5>Ready to approve <span class="ai-chip" style="margin:0">' + mocks.SPARK + ' Read by AI</span></h5>'
           + "".join(f'<div class="ar"><span class="pill {k}">{esc(kind)}</span><div class="t"><b>{esc(t)}</b><small>{esc(s)}</small></div>'
                     f'{mocks.plate(p)}<button type="button" class="btn sm primary ok-btn">Approve</button></div>'
                     for kind, k, t, s, p in APPROVE_ROWS)
           + '</div><p class="mock-note">Illustrative example with made-up data. Try the Approve buttons.</p>')


def home() -> str:
    feat_cards = "".join(
        f'<a class="card" href="{h}">{icon(i)}<h3>{esc(t)}</h3><p>{esc(d)}.</p><span class="more">Learn more →</span></a>'
        for (h, t, d), i in zip(FEATURES, ["car", "sign", "invoice", "ticket", "wrench", "pin"]))
    sol_cards = "".join(
        f'<a class="card" href="{h}">{icon(i)}<h3>{esc(t)}</h3><p>{esc(d)}.</p><span class="more">See how →</span></a>'
        for (h, t, d), i in zip(SOLUTIONS, ["car", "calendar", "users", "truck"]))
    compare = '<div class="r"><div>Task</div><div>Without RentalFleetBook</div><div>With RentalFleetBook</div></div>' + "".join(
        f'<div class="r"><div>{esc(a)}</div><div class="before">{esc(b)}</div><div class="after">{esc(c)}</div></div>' for a, b, c in COMPARE)
    faq = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in HOME_FAQ)

    def feat(title, eyebrow, text, points, mock, link, flip=False):
        pts = "".join(f"<li>{esc(p)}</li>" for p in points)
        return f'''<div class="feat{" flip" if flip else ""}"><div class="copy"><div class="eyebrow">{esc(eyebrow)}</div><h3>{esc(title)}</h3><p>{esc(text)}</p>
<ul class="checks">{pts}</ul><a class="more" href="{link}" style="font-weight:700">Learn more →</a></div><div>{mock}</div></div>'''

    body = f'''
<section class="hero-dark"><div class="wrap">
<div class="hero-top">
<div class="hero-copy">
<div class="hero-badge">{mocks.SPARK} AI-powered · Built in Melbourne for Australian rental fleets</div>
<h1>Your AI fleet manager.<br><span>You run the business.</span></h1>
</div>
<div class="hero-side">
<p class="lead">RentalFleetBook's AI reads your fines, tolls, mechanic invoices, rego notices and driver licences, files them against the right car and hire, and keeps billing running in Xero. You just check and approve.</p>
<div class="cta"><a class="btn primary" href="{APP}/signup">Start your free month <span class="arr">→</span></a><a class="btn ghost-light" href="/contact/">Book a demo</a></div>
<p class="hero-small">First month free · No credit card required · Unlimited users</p>
</div>
</div>
<div class="hero-shot"><img src="/assets/hero.jpg" srcset="/assets/hero-900.jpg 900w, /assets/hero.jpg 1600w" sizes="(max-width: 1220px) 100vw, 1180px" width="1600" height="900" alt="A rental operator with a tablet in front of her fleet, beside the RentalFleetBook fleet overview" fetchpriority="high"></div>
</div></section>

<section class="trust"><div class="wrap">
<div class="grid-4">
<div class="t">{icon("users")}<div><strong>Made by a rental operator</strong><p>Built and used every day by a Melbourne rental business with 30+ cars.</p></div></div>
<div class="t">{icon("refresh")}<div><strong>Connected to Xero</strong><p>Customers, invoices, repeating invoices and payments stay in sync.</p></div></div>
<div class="t">{icon("lock")}<div><strong>Australian hosting</strong><p>Your data is stored in Sydney, encrypted and backed up daily.</p></div></div>
<div class="t">{icon("phone")}<div><strong>Works on your phone</strong><p>Do pickups and returns in the yard, and install it like an app.</p></div></div>
</div></div></section>


<section><div class="wrap">
<div class="feat" style="padding:0"><div class="copy">
<div class="ai-eyebrow">{mocks.SPARK} What the AI does</div>
<h2>Paperwork in. Answers out.</h2>
<p class="lead" style="font-size:1.08rem">Forward or photograph a document and RentalFleetBook's AI reads it in seconds, pulls out what matters and puts it in the right place: the right car, the right hire, the right hirer.</p>
<ul class="checks">
<li><b>Fines and tolls:</b> offence, time, place and amount read, then matched to whoever had the car</li>
<li><b>Mechanic invoices:</b> service, odometer, cost and next due date filled in</li>
<li><b>Rego notices:</b> due date and amount read, bill drafted in Xero</li>
<li><b>Driver licences:</b> snap a photo and the hirer's details fill in</li>
<li><b>Your agreement:</b> upload it once and AI turns it into a fill-in template</li>
<li><b>Your inbox:</b> AI sorts every forwarded document by type</li>
</ul>
<a class="btn primary" href="/ai/">Meet your AI fleet manager <span class="arr">→</span></a>
</div><div>{APPROVE}</div></div>
</div></section>
<section class="alt"><div class="wrap">
<div class="head center"><div class="eyebrow">Everything your rental business needs</div><h2>One platform. Less administration. More control.</h2>
<p class="lead">Replace the spreadsheets, paper agreements and endless Xero copying with one system built around how rental businesses actually work.</p></div>
<div class="grid-3">{feat_cards}</div>
</div></section>

<section><div class="wrap">
{feat("Rental agreements signed in minutes", "Hires & agreements", "Use your own agreement wording. The hirer, car, dates and amounts fill in automatically, the hirer signs on screen, and the signed copy goes out with the car's insurance papers.", ["Your own agreement, uploaded from Word or PDF", "Pickup and return inspections with photos and damage notes", "Signed copy and insurance papers emailed to the hirer and to you", "Bond statement ready when the car comes back"], mocks.agreement(), "/features/digital-rental-agreements/")}
{feat("Invoices and payments that run themselves", "Payments & Xero", "When an agreement is signed, the first invoice (week one plus bond) and a weekly repeating invoice are created in Xero. When the car comes back, the repeating invoice stops.", ["First invoice dated the signing day", "Weekly repeating invoice from day seven", "Overdue list with SMS and email reminders", "Every invoice and payment visible on the hire and the customer"], mocks.invoices(), "/integrations/xero/", flip=True)}
{feat("Fines and tolls matched to the right hirer", "Fines & tolls", "Forward or scan an infringement notice. AI reads it, it's matched to whoever had the car at the time, and the nomination details are ready to copy into the council or toll site.", ["Notices read by AI, no typing", "Matched to the hire at the time of the offence", "Not-on-hire, dispute and withdrawal handled too", "Recharge the fine with your admin fee in one invoice"], mocks.fine(), "/features/fines-and-tolls/")}
{feat("Servicing that never slips", "Servicing & maintenance", "Forward your mechanic's invoice and AI fills in the service, odometer and next due date, with a draft bill in Xero. Services coming up and overdue stand out across the fleet.", ["Service history per car from mechanic invoices", "Next service by kilometres, with live odometer", "Overdue services highlighted", "Rego renewals read from VicRoads notices"], mocks.service(), "/features/fleet-maintenance/", flip=True)}
</div></section>

<section><div class="wrap">
<div class="head center"><div class="eyebrow">Where the time goes</div><h2>Hours of admin every week, handled</h2>
<p class="lead">These are the jobs that eat a rental operator's week. Here's what changes.</p></div>
<div class="compare">{compare}</div>
</div></section>

<section class="dark"><div class="wrap story">
<div><div class="eyebrow">Our story</div><h2>Built inside a real rental business</h2>
<p class="lead">RentalFleetBook started in a Melbourne rental company running more than 30 cars on weekly hires. The paperwork was taking over: agreements, weekly invoices, fines to nominate, services to track and hirers to chase.</p>
<p>We built the tool we needed, and we run our own fleet on it every day. Every feature exists because it solved a real problem in the yard or the office. Now we've opened it up to other Australian rental operators.</p>
<a class="btn light" href="/about/" style="margin-top:8px">Read our story <span class="arr">→</span></a></div>
<div class="facts">
<div class="fact"><strong>30+</strong><span>cars run on RentalFleetBook every day</span></div>
<div class="fact"><strong>1 month</strong><span>free for every new company</span></div>
<div class="fact"><strong>$30</strong><span>a month for up to 5 cars, every feature included</span></div>
<div class="fact"><strong>Sydney</strong><span>where your data is hosted</span></div>
</div>
</div></section>

<section class="alt"><div class="wrap">
<div class="head"><div class="eyebrow">Solutions</div><h2>Made for how you rent</h2><p class="lead">Short hires, weekly rentals, a handful of cars or a commercial fleet. RentalFleetBook fits the way you work.</p></div>
<div class="grid-4">{sol_cards}</div>
</div></section>

<section><div class="wrap">
<div class="feat" style="padding:0"><div class="copy"><div class="eyebrow">Know your numbers</div><h3>See which cars earn and which sit idle</h3>
<p>Run a fleet utilisation report for any dates: days on hire, idle days and rent earned for every car, with a CSV download for your accountant.</p>
<ul class="checks"><li>Utilisation for any date range</li><li>Live map, trips and kilometres per car</li><li>Overdue rent and fines at a glance</li></ul>
<a class="more" href="/features/fleet-management/" style="font-weight:700">Learn more →</a></div><div>{mocks.utilisation()}</div></div>
</div></section>

<section class="alt"><div class="wrap">
<div class="head center"><div class="eyebrow">Pricing</div><h2>Simple pricing. No surprises.</h2>
<p class="lead">One monthly invoice for your whole fleet, every feature included, unlimited users. Starts at $30 a month for up to 5 cars.</p></div>
<div class="prices">
<div class="price"><div class="n">1–5 cars</div><div class="amt">$30</div><div class="per">per month + GST</div><ul><li>All features</li><li>Unlimited users</li></ul><a class="btn" href="{APP}/signup">Start free</a></div>
<div class="price"><div class="n">6–10 cars</div><div class="amt">$45</div><div class="per">per month + GST</div><ul><li>All features</li><li>Unlimited users</li></ul><a class="btn" href="{APP}/signup">Start free</a></div>
<div class="price hl"><div class="tag">Most popular</div><div class="n">11–20 cars</div><div class="amt">$110</div><div class="per">per month + GST</div><ul><li>All features</li><li>Unlimited users</li></ul><a class="btn primary" href="{APP}/signup">Start free</a></div>
<div class="price"><div class="n">Over 20 cars</div><div class="amt">$5</div><div class="per">per car per month + GST</div><ul><li>All features</li><li>Unlimited users</li></ul><a class="btn" href="{APP}/signup">Start free</a></div>
</div>
<div class="calc">
<label style="font-weight:700;color:var(--ink)">How many cars do you run? <span id="n" style="color:var(--blue)">12</span>
<input id="cars" type="range" min="1" max="80" value="12" aria-label="Number of cars"></label>
<div style="text-align:right"><output id="price">$110</output><div class="note">per month + GST</div></div>
</div>
<p class="note center" style="margin-top:18px"><b>First month free.</b> Pay monthly by card, cancel any time. <a href="/pricing/">See full pricing →</a></p>
</div></section>

<section><div class="wrap narrow">
<div class="eyebrow">AI car rental fleet management software</div>
<h2>Run your car rental business smarter, with AI</h2>
<p>RentalFleetBook is an AI-powered car rental fleet management system designed for the everyday operations of Australian vehicle rental businesses. Manage your vehicles, rental agreements, customers, payments, maintenance, fines and tolls from one easy-to-use platform.</p>
<p>Whether you operate five vehicles or a growing rental fleet, RentalFleetBook reduces administration, improves visibility and keeps your business organised:</p>
<ul class="checks" style="columns:2;column-gap:32px">
<li>AI that reads fines, invoices, notices and licences</li><li>Vehicle and fleet management</li><li>Digital car rental agreements</li><li>Customer and hire management</li><li>Automated invoices and payment reminders</li><li>Xero accounting integration</li><li>Vehicle servicing and maintenance</li><li>Traffic fines and toll management</li><li>GPS tracking and kilometres</li><li>Registration and insurance records</li><li>Fleet utilisation reports</li>
</ul>
<p>It was developed by a Melbourne rental business to solve real operational problems, so you spend less time on paperwork and more time growing your fleet.</p>
</div></section>

<section class="alt"><div class="wrap narrow faq">
<div class="head"><div class="eyebrow">FAQ</div><h2>Questions operators ask</h2></div>
{faq}
</div></section>

{cta_band()}
<script>(function(){{var r=document.getElementById("cars"),o=document.getElementById("price"),n=document.getElementById("n");
function p(c){{return c<=5?30:c<=10?45:c<=20?110:5*c}}
function u(){{var c=+r.value;n.textContent=c;o.textContent="$"+p(c)}}r.addEventListener("input",u);u();
document.querySelectorAll(".approve .ok-btn").forEach(function(b){{b.addEventListener("click",function(){{var d=document.createElement("span");d.className="done";d.textContent="✓ Approved";b.replaceWith(d)}})}})}})()</script>
'''
    schema = [
        {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "RentalFleetBook",
         "applicationCategory": "BusinessApplication", "operatingSystem": "Web, iOS, Android",
         "description": "AI-powered car rental fleet management software for Australian rental businesses. AI reads fines, tolls, mechanic invoices, rego notices and driver licences; hires, agreements, Xero invoicing, servicing and GPS in one platform.",
         "url": "https://www.rentalfleetbook.com/",
         "offers": {"@type": "AggregateOffer", "priceCurrency": "AUD", "lowPrice": "30", "offerCount": "4"}},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in HOME_FAQ]},
    ]
    return page("/", "AI Fleet Manager for Car Rental Businesses in Australia | RentalFleetBook",
                "RentalFleetBook is the AI fleet manager for Australian car rental businesses. AI reads fines, tolls, mechanic invoices, rego notices and licences, and runs hires, agreements, Xero billing, servicing and GPS in one platform. First month free.",
                body, schema)
