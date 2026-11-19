from layout import APP, FEATURES, SOLUTIONS, cta_band, esc, icon, page
import mocks

HOME_FAQ = [
    ("Do I need Xero?", "Xero is recommended, because customers, invoices, repeating invoices and payments then sync automatically. You can start without it and connect it later."),
    ("Does it work outside Victoria?", "Yes. Hires, agreements, billing, servicing and GPS work anywhere in Australia. A few time-savers, such as reading VicRoads renewal notices and Victorian council and toll links, are tuned for Victoria first."),
    ("Can I use my own rental agreement?", "Yes. Upload your agreement as a Word file or PDF. Your wording stays exactly as it is; the hirer's details, vehicle, dates and amounts become blanks that fill in for each hire."),
    ("Can my staff use it?", "Yes. Add your team with their own logins and roles (owner, manager, finance or yard staff) at no extra cost."),
    ("Where is my data kept?", "In Australia (Sydney region), encrypted, with daily backups. Licence photos and documents are private to your company."),
    ("What happens after the free month?", "Add a card in Billing at any time and you're charged monthly by fleet size. If you don't, your account pauses and nothing is charged."),
]

COMPARE = [
    ("Weekly rent invoices", "Create or copy invoices by hand, chase payments in your inbox", "First invoice and weekly repeating invoice set up in Xero when the agreement is signed"),
    ("Traffic fines", "Work out who had the car, type their details into the council site", "Notice read and matched to the hirer; details ready to copy into the nomination"),
    ("Rental agreements", "Print, sign, scan, email, file", "Signed on screen with pickup photos, then emailed with the insurance papers"),
    ("Servicing", "Odometer readings and service dates in a spreadsheet", "Mechanic invoices read automatically; overdue services stand out"),
    ("Overdue rent", "Check Xero, text each hirer one by one", "One overdue list, with SMS and email reminders showing the total owing"),
    ("Rego and insurance", "Renewal dates kept in your head or a calendar", "Every car's rego, insurance and documents in one place, with what's due"),
]


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
<section class="hero"><div class="wrap grid">
<div>
<div class="eyebrow">Built for Australian rental operators</div>
<h1>Run your rental fleet. <span class="hl">Not your paperwork.</span></h1>
<p class="lead">The all-in-one platform for car rental businesses. Manage hires, agreements, invoices, servicing, fines and GPS in one place, connected to Xero.</p>
<div class="cta"><a class="btn primary" href="{APP}/signup">Start your free month <span class="arr">→</span></a><a class="btn" href="/contact/">Book a demo</a></div>
<ul class="ticks"><li>No credit card required</li><li>Data hosted in Australia</li><li>Xero integration</li></ul>
</div>
<div>{mocks.dashboard()}</div>
</div></section>

<section class="tight alt"><div class="wrap">
<div class="grid-4">
<div><strong style="color:var(--ink);font-size:1.05rem">Made by a rental operator</strong><p class="note" style="margin:4px 0 0">Built and used every day by a Melbourne rental business with 30+ cars.</p></div>
<div><strong style="color:var(--ink);font-size:1.05rem">Connected to Xero</strong><p class="note" style="margin:4px 0 0">Customers, invoices, repeating invoices and payments stay in sync.</p></div>
<div><strong style="color:var(--ink);font-size:1.05rem">Australian hosting</strong><p class="note" style="margin:4px 0 0">Your data is stored in Sydney, encrypted and backed up daily.</p></div>
<div><strong style="color:var(--ink);font-size:1.05rem">Works on your phone</strong><p class="note" style="margin:4px 0 0">Do pickups and returns in the yard, and install it like an app.</p></div>
</div></div></section>

<section><div class="wrap">
<div class="head center"><div class="eyebrow">Everything your rental business needs</div><h2>One platform. Less administration. More control.</h2>
<p class="lead">Replace the spreadsheets, paper agreements and endless Xero copying with one system built around how rental businesses actually work.</p></div>
<div class="grid-3">{feat_cards}</div>
</div></section>

<section class="alt"><div class="wrap">
{feat("Rental agreements signed in minutes", "Hires & agreements", "Use your own agreement wording. The hirer, car, dates and amounts fill in automatically, the hirer signs on screen, and the signed copy goes out with the car's insurance papers.", ["Your own agreement, uploaded from Word or PDF", "Pickup and return inspections with photos and damage notes", "Signed copy and insurance papers emailed to the hirer and to you", "Bond statement ready when the car comes back"], mocks.agreement(), "/features/digital-rental-agreements/")}
{feat("Invoices and payments that run themselves", "Payments & Xero", "When an agreement is signed, the first invoice (week one plus bond) and a weekly repeating invoice are created in Xero. When the car comes back, the repeating invoice stops.", ["First invoice dated the signing day", "Weekly repeating invoice from day seven", "Overdue list with SMS and email reminders", "Every invoice and payment visible on the hire and the customer"], mocks.invoices(), "/integrations/xero/", flip=True)}
{feat("Fines and tolls matched to the right hirer", "Fines & tolls", "Forward or scan an infringement notice. It's read automatically, matched to whoever had the car at the time, and the nomination details are ready to copy into the council or toll site.", ["Notices read automatically, no typing", "Matched to the hire at the time of the offence", "Not-on-hire, dispute and withdrawal handled too", "Recharge the fine with your admin fee in one invoice"], mocks.fine(), "/features/fines-and-tolls/")}
{feat("Servicing that never slips", "Servicing & maintenance", "Forward your mechanic's invoice and the service, odometer and next due date are filled in, with a draft bill in Xero. Services coming up and overdue stand out across the fleet.", ["Service history per car from mechanic invoices", "Next service by kilometres, with live odometer", "Overdue services highlighted", "Rego renewals read from VicRoads notices"], mocks.service(), "/features/fleet-maintenance/", flip=True)}
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
<p class="note center" style="margin-top:18px"><b>First month free.</b> Pay monthly by card, cancel any time. <a href="/pricing/">See full pricing →</a></p>
</div></section>

<section><div class="wrap narrow">
<div class="eyebrow">Car rental fleet management software</div>
<h2>Run your car rental business smarter</h2>
<p>RentalFleetBook is an all-in-one car rental fleet management system designed for the everyday operations of Australian vehicle rental businesses. Manage your vehicles, rental agreements, customers, payments, maintenance, fines and tolls from one easy-to-use platform.</p>
<p>Whether you operate five vehicles or a growing rental fleet, RentalFleetBook reduces administration, improves visibility and keeps your business organised:</p>
<ul class="checks" style="columns:2;column-gap:32px">
<li>Vehicle and fleet management</li><li>Digital car rental agreements</li><li>Customer and hire management</li><li>Automated invoices and payment reminders</li><li>Xero accounting integration</li><li>Vehicle servicing and maintenance</li><li>Traffic fines and toll management</li><li>GPS tracking and kilometres</li><li>Registration and insurance records</li><li>Fleet utilisation reports</li>
</ul>
<p>It was developed by a Melbourne rental business to solve real operational problems, so you spend less time on paperwork and more time growing your fleet.</p>
</div></section>

<section class="alt"><div class="wrap narrow faq">
<div class="head"><div class="eyebrow">FAQ</div><h2>Questions operators ask</h2></div>
{faq}
</div></section>

{cta_band()}
'''
    schema = [
        {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "RentalFleetBook",
         "applicationCategory": "BusinessApplication", "operatingSystem": "Web, iOS, Android",
         "description": "Car rental fleet management software for Australian rental businesses: hires, agreements, invoices with Xero, servicing, fines, tolls and GPS.",
         "url": "https://www.rentalfleetbook.com/",
         "offers": {"@type": "AggregateOffer", "priceCurrency": "AUD", "lowPrice": "30", "offerCount": "4"}},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in HOME_FAQ]},
    ]
    return page("/", "Car Rental Fleet Management Software Australia | RentalFleetBook",
                "Manage your car rental business with RentalFleetBook. Handle vehicle hires, rental agreements, payments, servicing, fines, tolls and GPS tracking in one platform. Xero integration. Start your free month.",
                body, schema)
