"""Feature pages (/features/..., /integrations/xero/) and the features hub."""
from layout import APP, FEATURES, breadcrumbs, cta_band, esc, icon, page
import mocks

# Each page: path, title tag, meta description, eyebrow, H1, lead, mock, blocks [(icon, title, text)], steps, faq, related
PAGES = [
    dict(
        path="/features/fleet-management/", name="Fleet management",
        title="Rental Fleet Management System | Vehicles, Rego & Utilisation | RentalFleetBook",
        desc="Keep every rental car's rego, insurance, documents, odometer and status in one place. See what's due, what's on hire and which cars earn. Built for Australian rental fleets.",
        eyebrow="Fleet management", h1="Every car in your rental fleet, under control",
        lead="One record for every vehicle: rego, insurance, documents, odometer, service plan, current hire and earnings. See at a glance what's on hire, what's available and what needs attention.",
        mock=mocks.fleet(),
        blocks=[
            ("car", "One record per vehicle", "Rego and state, make, model, VIN, weekly rate, bond, km limit, service interval and documents, all on the car's page."),
            ("calendar", "Rego and insurance due dates", "See which cars have rego or insurance coming up. VicRoads renewal notices are read automatically and the bill goes to Xero."),
            ("chart", "Fleet utilisation reports", "Choose any dates and see days on hire, idle days and rent earned per car and for the whole fleet, with a CSV download."),
            ("inbox", "Documents filed automatically", "Forward rego notices, insurance papers, tolls and mechanic invoices to your own inbox address. Each one is read and filed against the right car."),
            ("users", "Your team, with roles", "Owner, manager, finance and yard staff each see what they need. Add as many users as you like."),
            ("phone", "Works in the yard", "Check a car, start a hire or record a return from your phone. Install it to your home screen like an app."),
        ],
        steps=[("Import your cars", "From Xero, a spreadsheet, or one by one."), ("Add documents", "Upload or forward insurance, rego and service papers."), ("Run your fleet", "Hires, servicing and billing all hang off each car.")],
        faq=[("Can I import my existing cars?", "Yes. Import from Xero or a spreadsheet, or add them one by one. Most fleets are set up in under an hour."),
             ("Does it track kilometres?", "Yes. Odometer readings come from pickups, returns, mechanic invoices and GPS trackers, so the current reading stays up to date."),
             ("Can I see which cars earn the most?", "Yes. The fleet utilisation report shows days on hire, idle days and estimated rent per car for any dates you choose.")],
    ),
    dict(
        path="/features/digital-rental-agreements/", name="Digital rental agreements",
        title="Digital Car Rental Agreements & Vehicle Inspections | RentalFleetBook",
        desc="Use your own rental agreement, filled in automatically and signed on screen. Pickup and return inspections with photos, insurance papers emailed to the hirer, and bond statements on return.",
        eyebrow="Digital rental agreements", h1="Your rental agreement, signed on screen in minutes",
        lead="Upload your own agreement once. For every hire, the hirer's details, vehicle, dates and amounts fill in automatically. The hirer signs on screen, and the signed copy goes out with the car's insurance papers.",
        mock=mocks.agreement(),
        blocks=[
            ("sign", "Your own wording", "Upload your agreement as Word or PDF. Your wording is kept exactly as it is; names, dates, vehicle and amounts become blanks."),
            ("camera", "Pickup and return inspections", "Photos of every side of the car, odometer and fuel, with damage marked as existing or new. Done on a phone in the yard."),
            ("invoice", "Bond statement on return", "When the car comes back, damage, unpaid rent, extra kilometres and fines are pulled into a bond statement you can adjust."),
            ("inbox", "Emailed automatically", "The signed agreement and the insurer's papers (policy, PDS, FSG) are emailed to the hirer, with a copy to you."),
            ("users", "Licence and hirer details", "Licence photos and details stored privately with the customer record, ready for the next hire and for fine nominations."),
            ("refresh", "Billing starts on signing", "Signing can create the first invoice and the weekly repeating invoice in Xero, so billing starts the same day."),
        ],
        steps=[("Upload your agreement", "Word or PDF, once."), ("Start a hire", "Pick the hirer and the car; the agreement fills in."), ("Inspect and sign", "Photos at pickup, signature on screen, papers emailed.")],
        faq=[("Is an on-screen signature valid?", "Electronic signatures are generally accepted for commercial agreements in Australia. If you prefer, print the filled-in agreement and sign on paper, then tick it as signed."),
             ("Can I keep using my current agreement?", "Yes. You upload your own agreement, and its wording stays exactly as you wrote it."),
             ("What does the hirer receive?", "An email with their signed agreement and the insurance papers for the car they're driving. You get a copy too.")],
    ),
    dict(
        path="/integrations/xero/", name="Invoices, payments & Xero",
        title="Car Rental Invoicing with Xero Integration | RentalFleetBook",
        desc="Automatic rental invoices in Xero: first invoice with bond on signing, weekly repeating invoices, overdue reminders by SMS and email, and every payment visible on the hire. Built for Xero users.",
        eyebrow="Xero integration", h1="Rental invoicing that runs itself, in Xero",
        lead="RentalFleetBook connects to your Xero account. Customers, invoices, repeating invoices and payments stay in sync, so you stop copying hires into Xero and chasing payments by hand.",
        mock=mocks.invoices(),
        blocks=[
            ("invoice", "First invoice on signing", "When the agreement is signed, the first invoice (week one plus bond) is raised in Xero, dated that day."),
            ("refresh", "Weekly repeating invoices", "A weekly repeating invoice is set up from day seven, using your usual accounts and tax settings. It stops when the car is returned."),
            ("bell", "Overdue reminders", "One list of everyone who owes, with SMS and email reminders that show the total owing."),
            ("users", "Customers synced", "Hirers become Xero contacts with their details. Existing Xero customers and invoices are imported."),
            ("ticket", "Fines and costs recharged", "Recharge fines, tolls and damage with your admin fee in a single invoice."),
            ("wrench", "Bills from your inbox", "Mechanic invoices and rego renewals arrive as draft bills in Xero, ready to approve."),
        ],
        steps=[("Connect Xero", "Sign in to Xero and approve access. We never see your Xero password."), ("Import", "Customers, invoices and repeating invoices come across."), ("Bill automatically", "New hires are invoiced from the day they're signed.")],
        faq=[("Do I need Xero to use RentalFleetBook?", "No, but it's recommended. Without Xero you still get hires, agreements, fines, servicing and GPS; invoicing is where Xero saves the most time."),
             ("Will it change my existing Xero invoices?", "No. Existing invoices and repeating invoices are read and shown on the right hire and customer. New ones are created only for new hires."),
             ("What happens when a car comes back?", "When you return the car in RentalFleetBook, its weekly repeating invoice in Xero is deleted, so the hirer isn't billed again.")],
    ),
    dict(
        path="/features/fines-and-tolls/", name="Fines & tolls",
        title="Traffic Fine & Toll Management for Rental Cars | RentalFleetBook",
        desc="Rental car fines and tolls read automatically, matched to the hirer at the time of the offence, and ready to nominate on the council or toll site. Disputes, withdrawals and recharges included.",
        eyebrow="Fines & tolls", h1="Every fine matched to the right hirer, automatically",
        lead="Forward or scan an infringement notice. RentalFleetBook reads it, finds who had the car at the time of the offence, and gets the nomination details ready to copy into the council or toll operator's website.",
        mock=mocks.fine(),
        blocks=[
            ("inbox", "Read automatically", "Notice number, offence, date and time, location, amount and due date are read from the notice. No typing."),
            ("users", "Matched to the hire", "The offence time is matched to the hire at that moment, so you know exactly who to nominate."),
            ("ticket", "Ready to nominate", "Hirer and licence details laid out to copy in one click, with a link to the right council or toll nomination page."),
            ("shield", "Not on hire? Dispute it", "If the car wasn't on hire, record why, with a dispute letter tool that includes repair evidence."),
            ("refresh", "Withdrawals handled", "Withdrawal notices are matched to the original fine and close it automatically."),
            ("invoice", "Recharge with your fee", "Recharge the fine or toll to the hirer with your admin fee, in one invoice."),
        ],
        steps=[("Forward the notice", "Email it to your RentalFleetBook inbox, or upload a photo."), ("Check the match", "See who had the car at the time."), ("Nominate", "Copy the details into the council or toll site.")],
        faq=[("Do you submit nominations for me?", "No. A nomination is a legal statement, so you submit it yourself. RentalFleetBook gets every detail ready and links you to the right page."),
             ("Which councils and toll roads work?", "Any notice can be read. Direct links are set up for common Victorian councils, and other councils get a quick search for their nomination page."),
             ("What if the car was off the road?", "Mark it as not on hire and choose to nominate, dispute or pay. The dispute tool helps you write the letter with repair evidence.")],
    ),
    dict(
        path="/features/fleet-maintenance/", name="Servicing & maintenance",
        title="Fleet Maintenance Software for Rental Cars | Service Tracking | RentalFleetBook",
        desc="Track rental car servicing by kilometres. Mechanic invoices read automatically, odometer kept current, overdue services highlighted and draft bills sent to Xero.",
        eyebrow="Servicing & maintenance", h1="Fleet servicing that never slips through the cracks",
        lead="Rental cars cover a lot of kilometres. RentalFleetBook keeps every car's service history, current odometer and next service in one list, so nothing goes overdue while it's out on hire.",
        mock=mocks.service(),
        blocks=[
            ("wrench", "Service history per car", "Every service, repair and part, with cost and odometer, from your mechanic's invoices."),
            ("inbox", "Mechanic invoices read", "Forward the invoice and the service type, odometer and next due are filled in, with a draft bill in Xero."),
            ("clock", "Due by kilometres", "Set the service interval per car. With odometer readings from hires and GPS, you see how many kilometres are left."),
            ("bell", "Overdue stands out", "Cars due soon and overdue rise to the top, sorted by date."),
            ("calendar", "Rego and insurance", "Renewal dates sit alongside servicing, so the car is always roadworthy and legal."),
            ("chart", "Cost per car", "See what each car costs to keep on the road, next to what it earns."),
        ],
        steps=[("Set intervals", "Service interval per car, in kilometres."), ("Forward invoices", "Your mechanic's invoices fill in the history."), ("Act on what's due", "Book the cars that are due before they're overdue.")],
        faq=[("Where do odometer readings come from?", "Pickup and return inspections, mechanic invoices and GPS trackers. Readings of zero are ignored."),
             ("Does it work with any mechanic?", "Yes. Any invoice that shows the car's rego and the work done can be read."),
             ("Can I record repairs as well as services?", "Yes. Services, repairs, tyres and parts are all part of the car's history.")],
    ),
    dict(
        path="/features/gps-tracking/", name="GPS tracking",
        title="GPS Tracking for Rental Cars | Live Map, Trips & Kilometres | RentalFleetBook",
        desc="See your rental fleet on a live map, with routes, trips, stops and kilometres driven per car each week. Works with common GPS trackers and checks weekly km limits.",
        eyebrow="GPS tracking", h1="Know where every rental car is, and how far it's gone",
        lead="Connect your GPS trackers and see the whole fleet on a live map. Check a car's routes, trips and stops, and the kilometres each car has driven this week against its limit.",
        mock=mocks.gps(),
        blocks=[
            ("map", "Live map", "Every car on one map, with its current hire and hirer one click away."),
            ("pin", "Routes, trips and stops", "Pick a car and a day to see where it went, how long it stopped and how fast it travelled."),
            ("chart", "Kilometres per week", "Kilometres driven per car each week, checked against the hire's weekly limit for excess-km charges."),
            ("shield", "Recover with confidence", "Know where a car is when a hirer stops paying or doesn't return it."),
            ("clock", "Odometer kept current", "Tracker kilometres keep the service schedule accurate between inspections."),
            ("phone", "On your phone", "Open the map from the yard or the road."),
        ],
        steps=[("Fit a tracker", "Use a compatible GPS tracker in each car."), ("Point it to RentalFleetBook", "We help you set the server address."), ("See it live", "Cars appear on the map within minutes.")],
        faq=[("Which trackers work?", "Most common GPS trackers that can send data to a standard tracking server. Contact us with your tracker model and we'll check."),
             ("Is GPS tracking legal for rental cars?", "Generally yes, when the hirer is told in the rental agreement. Make sure your agreement includes a tracking clause."),
             ("Do I need GPS to use RentalFleetBook?", "No. GPS is optional; every other feature works without it.")],
    ),
]


def feature_page(p: dict) -> str:
    blocks = "".join(f'<div class="card">{icon(i)}<h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for i, t, d in p["blocks"])
    steps = "".join(f'<div class="card"><div class="eyebrow" style="margin:0">Step {n + 1}</div><h3 style="margin-top:6px">{esc(t)}</h3><p>{esc(d)}</p></div>' for n, (t, d) in enumerate(p["steps"]))
    faq = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in p["faq"])
    related = "".join(f'<a class="card" href="{h}"><h3 style="margin:0">{esc(t)}</h3><p style="margin-top:6px">{esc(d)}.</p></a>' for h, t, d in FEATURES if h != p["path"])[:100000]
    crumbs = [("Home", "/"), ("Features", "/features/"), (p["name"], p["path"])]
    body = f'''
<section class="page-hero"><div class="wrap grid">
<div>{breadcrumbs(crumbs)}<div class="eyebrow">{esc(p["eyebrow"])}</div><h1 style="font-size:clamp(2rem,4.2vw,3rem)">{esc(p["h1"])}</h1>
<p class="lead">{esc(p["lead"])}</p>
<div class="cta" style="margin-top:24px"><a class="btn primary" href="{APP}/signup">Start your free month <span class="arr">→</span></a><a class="btn" href="/contact/">Book a demo</a></div></div>
<div>{p["mock"]}</div></div></section>
<section><div class="wrap"><div class="head"><h2>What you get</h2></div><div class="grid-3">{blocks}</div></div></section>
<section class="alt"><div class="wrap"><div class="head"><h2>How it works</h2></div><div class="grid-3">{steps}</div></div></section>
<section><div class="wrap narrow faq"><div class="head"><h2>Questions</h2></div>{faq}</div></section>
<section class="alt tight"><div class="wrap"><div class="head"><h2 style="font-size:1.5rem">More features</h2></div><div class="grid-3">{related}</div></div></section>
{cta_band()}'''
    schema = [{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]}]
    return page(p["path"], p["title"], p["desc"], body, schema, crumbs)


def features_hub() -> str:
    icons = ["car", "sign", "invoice", "ticket", "wrench", "pin"]
    cards = "".join(f'<a class="card" href="{h}">{icon(i)}<h3>{esc(t)}</h3><p>{esc(d)}.</p><span class="more">Learn more →</span></a>' for (h, t, d), i in zip(FEATURES, icons))
    extra = [("inbox", "Paperwork inbox", "Your own forwarding address for tolls, fines, rego notices, insurance and mechanic invoices. Each one is read and filed."),
             ("bell", "Overdue reminders", "One list of who owes what, with SMS and email reminders showing the total owing."),
             ("chart", "Utilisation reports", "Days on hire, idle days and rent earned per car for any dates, with CSV download."),
             ("users", "Team roles", "Owner, manager, finance and yard staff logins, with unlimited users."),
             ("phone", "Mobile app", "Works in any phone browser and installs to your home screen."),
             ("lock", "Secure and private", "Hosted in Sydney, encrypted, backed up daily, with private documents per company.")]
    extra_cards = "".join(f'<div class="card">{icon(i)}<h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for i, t, d in extra)
    crumbs = [("Home", "/"), ("Features", "/features/")]
    body = f'''
<section class="page-hero"><div class="wrap">{breadcrumbs(crumbs)}<div class="eyebrow">Features</div>
<h1 style="font-size:clamp(2rem,4.2vw,3rem);max-width:820px">Everything a car rental business runs on, in one platform</h1>
<p class="lead">Hires, agreements, invoices, fines, servicing and GPS, connected to each other and to Xero.</p>
<div class="cta" style="margin-top:24px"><a class="btn primary" href="{APP}/signup">Start your free month <span class="arr">→</span></a><a class="btn" href="/contact/">Book a demo</a></div></div></section>
<section><div class="wrap"><div class="grid-3">{cards}</div></div></section>
<section class="alt"><div class="wrap"><div class="head"><h2>Also included</h2></div><div class="grid-3">{extra_cards}</div></div></section>
{cta_band()}'''
    return page("/features/", "Car Rental Software Features | RentalFleetBook",
                "All RentalFleetBook features: fleet management, digital rental agreements, Xero invoicing, fines and tolls, servicing, GPS tracking, reminders and utilisation reports.",
                body, None, crumbs)
