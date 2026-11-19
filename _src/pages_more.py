"""Solutions, pricing, about, security, contact, legal and 404 pages."""
from pathlib import Path
from layout import APP, PHONE, PHONE_HREF, SOLUTIONS, breadcrumbs, cta_band, esc, icon, page
import mocks

SOL = [
    dict(path="/solutions/car-rental/", name="Car rental businesses",
         title="Car Rental Software for Australian Rental Businesses | RentalFleetBook",
         desc="Car rental software that runs your hires, agreements, Xero invoicing, fines and servicing in one place. Built by an Australian rental operator. First month free.",
         h1="Car rental software that does the paperwork for you",
         lead="Running a car rental business means hires, agreements, invoices, fines, services and rego, all at once. RentalFleetBook puts them in one place and automates the repetitive parts.",
         pains=["Agreements printed, signed, scanned and filed by hand", "Invoices copied into Xero for every hire", "Fines that need the right hirer found and nominated", "Services and rego dates in spreadsheets"],
         gains=["Agreements signed on screen, with inspections and insurance papers emailed", "First invoice and weekly repeating invoice created in Xero on signing", "Fines read and matched to the hirer automatically", "Servicing, rego and insurance tracked per car"],
         mock=mocks.dashboard(False)),
    dict(path="/solutions/long-term-rental/", name="Long-term & weekly rental",
         title="Long-Term Car Rental Management Software | Weekly Hire Billing | RentalFleetBook",
         desc="Manage long-term and weekly car rentals: weekly repeating invoices in Xero, bonds, overdue reminders, kilometre limits, fines nominations and bond statements on return.",
         h1="Built for long-term and weekly car rentals",
         lead="Weekly rentals, such as cars for rideshare and delivery drivers, run for months. That means weekly billing, overdue chasing, bonds, kilometre limits and a steady stream of fines. RentalFleetBook was built around exactly this.",
         pains=["Weekly invoices every Wednesday, for every hirer", "Chasing overdue rent one text at a time", "Fines arriving weeks later for cars on long hires", "Working out the bond when the car finally comes back"],
         gains=["Weekly repeating invoices in Xero from the day the agreement is signed", "Overdue list with SMS and email reminders showing the total owing", "Fines matched to whoever had the car on the day", "Bond statement with damage, unpaid rent, extra km and fines on return"],
         mock=mocks.invoices()),
    dict(path="/solutions/small-fleets/", name="Small rental fleets",
         title="Rental Software for Small Fleets (1–20 Cars) | RentalFleetBook",
         desc="Affordable rental fleet software for small car rental businesses with 1 to 20 cars. From $30 a month, every feature included, set up in an afternoon. First month free.",
         h1="Professional rental software, sized for a small fleet",
         lead="You don't need an enterprise system to run five or fifteen cars, but you do need more than a spreadsheet. RentalFleetBook gives a small fleet the same automation as a big one, from $30 a month.",
         pains=["No time for complicated software or long setup", "Enterprise rental systems priced for hundreds of cars", "Everything lives in your head, your phone and a spreadsheet", "Growing past a few cars without hiring an admin"],
         gains=["Set up in an afternoon: sign up, connect Xero, add your cars", "From $30 a month for up to 5 cars, every feature included", "Works on your phone, in the yard and on the road", "Unlimited users when you add staff"],
         mock=mocks.fleet()),
    dict(path="/solutions/commercial-vehicle-hire/", name="Commercial vehicle hire",
         title="Commercial Vehicle Hire Software | Utes, Vans & Trucks | RentalFleetBook",
         desc="Hire management software for utes, vans, tippers and trucks: commercial hire agreements, kilometre limits, service schedules by km, inspections, GPS and Xero invoicing.",
         h1="Hire management for utes, vans and trucks",
         lead="Commercial vehicles work hard and cover big distances. RentalFleetBook keeps the agreements, inspections, kilometre limits, servicing and billing for your commercial fleet in one system.",
         pains=["Damage disputes without proper pickup and return photos", "Kilometres over the limit that never get charged", "Heavy-use vehicles missing their service intervals", "Tolls and fines from business customers' drivers"],
         gains=["Inspections with photos at pickup and return, on a phone", "Weekly kilometre limits with excess-km charges", "Service schedules by kilometres, with live odometer", "Tolls and fines matched to the hire and recharged"],
         mock=mocks.service()),
]


def solution_page(s: dict) -> str:
    pains = "".join(f"<li>{esc(x)}</li>" for x in s["pains"])
    gains = "".join(f"<li>{esc(x)}</li>" for x in s["gains"])
    crumbs = [("Home", "/"), ("Solutions", s["path"]), (s["name"], s["path"])]
    crumbs = [crumbs[0], crumbs[2]]
    others = "".join(f'<a class="card" href="{h}"><h3 style="margin:0">{esc(t)}</h3><p style="margin-top:6px">{esc(d)}.</p></a>' for h, t, d in SOLUTIONS if h != s["path"])
    feats = [("/features/digital-rental-agreements/", "sign", "Digital agreements"), ("/integrations/xero/", "invoice", "Invoices & Xero"),
             ("/features/fines-and-tolls/", "ticket", "Fines & tolls"), ("/features/fleet-maintenance/", "wrench", "Servicing"),
             ("/features/gps-tracking/", "pin", "GPS tracking"), ("/features/fleet-management/", "car", "Fleet management")]
    fcards = "".join(f'<a class="card" href="{h}" style="display:flex;gap:14px;align-items:center;padding:18px">{icon(i)}<b style="color:var(--ink)">{esc(t)}</b></a>' for h, i, t in feats)
    body = f'''
<section class="page-hero"><div class="wrap grid">
<div>{breadcrumbs(crumbs)}<div class="eyebrow">{esc(s["name"])}</div><h1 style="font-size:clamp(2rem,4.2vw,3rem)">{esc(s["h1"])}</h1>
<p class="lead">{esc(s["lead"])}</p>
<div class="cta" style="margin-top:24px"><a class="btn primary" href="{APP}/signup">Start your free month <span class="arr">→</span></a><a class="btn" href="/contact/">Book a demo</a></div></div>
<div>{s["mock"]}</div></div></section>
<section><div class="wrap grid-2" style="gap:28px">
<div class="card" style="padding:32px"><h2 style="font-size:1.5rem">The problem</h2><ul class="checks" style="--c:0">{pains}</ul></div>
<div class="card" style="padding:32px;border-color:var(--blue-100);background:var(--blue-50)"><h2 style="font-size:1.5rem">With RentalFleetBook</h2><ul class="checks">{gains}</ul></div>
</div></section>
<section class="alt"><div class="wrap"><div class="head"><h2>The features you'll use most</h2></div><div class="grid-3">{fcards}</div></div></section>
<section class="tight"><div class="wrap"><div class="head"><h2 style="font-size:1.5rem">Other solutions</h2></div><div class="grid-3">{others}</div></div></section>
{cta_band()}'''
    return page(s["path"], s["title"], s["desc"], body, None, crumbs)


PRICE_FAQ = [
    ("How is the price worked out?", "By the number of vehicles in your account: up to 5 cars $30, 6 to 10 cars $45, 11 to 20 cars $110, and over 20 cars $5 per car. All prices are per month plus GST."),
    ("What happens when I add or remove cars?", "Your package adjusts automatically on your next monthly invoice. There's nothing to change yourself."),
    ("Is there a setup fee or contract?", "No setup fee and no lock-in contract. Pay monthly by card and cancel any time."),
    ("What's included?", "Every feature, unlimited users, Xero integration, email support and your data hosted in Australia."),
    ("Do I need a card to start the free month?", "No. Start your free month without a card. Add one in Billing when you're ready to keep going."),
]


def pricing() -> str:
    faq = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in PRICE_FAQ)
    crumbs = [("Home", "/"), ("Pricing", "/pricing/")]
    body = f'''
<section class="page-hero"><div class="wrap center">{breadcrumbs(crumbs)}<div class="eyebrow">Pricing</div>
<h1 style="font-size:clamp(2rem,4.2vw,3rem)">Simple pricing by fleet size</h1>
<p class="lead">One monthly invoice for your whole fleet. Every feature, unlimited users. Your first month is free.</p></div></section>
<section><div class="wrap">
<div class="prices">
<div class="price"><div class="n">1–5 cars</div><div class="amt">$30</div><div class="per">per month + GST</div><ul><li>All features</li><li>Unlimited users</li><li>Xero integration</li></ul><a class="btn" href="{APP}/signup">Start free</a></div>
<div class="price"><div class="n">6–10 cars</div><div class="amt">$45</div><div class="per">per month + GST</div><ul><li>All features</li><li>Unlimited users</li><li>Xero integration</li></ul><a class="btn" href="{APP}/signup">Start free</a></div>
<div class="price hl"><div class="tag">Most popular</div><div class="n">11–20 cars</div><div class="amt">$110</div><div class="per">per month + GST</div><ul><li>All features</li><li>Unlimited users</li><li>Xero integration</li></ul><a class="btn primary" href="{APP}/signup">Start free</a></div>
<div class="price"><div class="n">Over 20 cars</div><div class="amt">$5</div><div class="per">per car per month + GST</div><ul><li>All features</li><li>Unlimited users</li><li>Xero integration</li></ul><a class="btn" href="{APP}/signup">Start free</a></div>
</div>
<div class="calc">
<label style="font-weight:700;color:var(--ink)">How many cars do you have? <span id="n" style="color:var(--blue)">12</span>
<input id="cars" type="range" min="1" max="80" value="12" aria-label="Number of cars"></label>
<div style="text-align:right"><output id="price">$110</output><div class="note">per month + GST</div></div>
</div>
<p class="note center" style="margin-top:18px"><b>First month free.</b> No setup fee, no contract. Pay monthly by card through Stripe, cancel any time. Prices in Australian dollars.</p>
</div></section>
<section class="alt"><div class="wrap narrow faq"><div class="head"><h2>Pricing questions</h2></div>{faq}</div></section>
{cta_band()}
<script>(function(){{var r=document.getElementById("cars"),o=document.getElementById("price"),n=document.getElementById("n");
function p(c){{return c<=5?30:c<=10?45:c<=20?110:5*c}}
function u(){{var c=+r.value;n.textContent=c;o.textContent="$"+p(c)}}r.addEventListener("input",u);u()}})()</script>'''
    schema = [{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in PRICE_FAQ]}]
    return page("/pricing/", "Pricing | Car Rental Fleet Software from $30/month | RentalFleetBook",
                "RentalFleetBook pricing: $30/month for up to 5 cars, $45 for 6–10, $110 for 11–20 and $5 per car above 20, plus GST. Every feature, unlimited users, first month free.",
                body, schema, crumbs)


def about() -> str:
    crumbs = [("Home", "/"), ("About us", "/about/")]
    values = [("wrench", "Practical first", "Every feature solves a job we do ourselves: agreements, invoices, fines, services. If it doesn't save time in a real rental business, it doesn't go in."),
              ("users", "Made for small operators", "Most rental businesses in Australia run a few cars to a few dozen. RentalFleetBook is priced and built for them."),
              ("lock", "Your data is yours", "Hosted in Australia, private to your company, and exportable any time.")]
    vcards = "".join(f'<div class="card">{icon(i)}<h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for i, t, d in values)
    body = f'''
<section class="page-hero"><div class="wrap narrow">{breadcrumbs(crumbs)}<div class="eyebrow">About us</div>
<h1 style="font-size:clamp(2rem,4.2vw,3rem)">Built by a rental operator, for rental operators</h1>
<p class="lead">RentalFleetBook comes from a Melbourne car rental business, not a software company.</p></div></section>
<section><div class="wrap narrow prose">
<h2>Why we built it</h2>
<p>We run a fleet of more than 30 cars on weekly hires in Melbourne. As the fleet grew, the paperwork grew faster: agreements to print and file, weekly invoices to create in Xero, fines to match to the right hirer and nominate, services and rego dates to track, and overdue rent to chase.</p>
<p>The rental software we looked at was either built for airport car hire with hundreds of vehicles, or was a generic fleet tool that didn't understand hires, bonds and nominations. So we built our own, and we run our fleet on it every day.</p>
<h2>What it does today</h2>
<p>RentalFleetBook handles the whole life of a hire: the agreement and pickup inspection, invoicing in Xero, fines and tolls during the hire, servicing, GPS, and the return inspection and bond statement at the end. Paperwork such as mechanic invoices, toll statements, infringement notices and rego renewals is forwarded to one inbox, read automatically and filed against the right car.</p>
<h2>Now open to other operators</h2>
<p>We've opened RentalFleetBook to other Australian rental businesses, at a price that makes sense for small fleets. Your first month is free, and we're always happy to show you around. <a href="/contact/">Book a demo</a> or call us on <a href="{PHONE_HREF}">{PHONE}</a>.</p>
</div></section>
<section class="alt"><div class="wrap"><div class="head"><h2>What we believe</h2></div><div class="grid-3">{vcards}</div></div></section>
{cta_band()}'''
    return page("/about/", "About RentalFleetBook | Built by a Melbourne Rental Operator",
                "RentalFleetBook was built inside a Melbourne car rental business running 30+ cars on weekly hires, to solve real rental paperwork. Now open to Australian rental operators.",
                body, None, crumbs)


def security() -> str:
    crumbs = [("Home", "/"), ("Security", "/security/")]
    items = [("cloud", "Hosted in Australia", "Your database and files are stored in the Sydney region."),
             ("lock", "Encrypted", "Data is encrypted in transit (HTTPS) and at rest."),
             ("shield", "Separated by company", "Database rules keep each company's data private to that company. Documents such as licence photos are only accessible to your team."),
             ("users", "Role-based access", "Owner, manager, finance and yard roles limit what each person can see and change."),
             ("refresh", "Backups", "Daily database backups, plus a separate encrypted weekly backup of data and documents."),
             ("invoice", "Payments by Stripe", "Card payments for your subscription are handled by Stripe. We never see or store full card numbers."),
             ("sign", "Xero via secure sign-in", "Xero is connected with Xero's own sign-in. We never see your Xero password, and you can disconnect at any time."),
             ("inbox", "Your data stays yours", "Ask for an export of your data at any time, or for it to be deleted when you leave.")]
    cards = "".join(f'<div class="card">{icon(i)}<h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for i, t, d in items)
    body = f'''
<section class="page-hero"><div class="wrap narrow">{breadcrumbs(crumbs)}<div class="eyebrow">Security</div>
<h1 style="font-size:clamp(2rem,4.2vw,3rem)">Your data, kept safe in Australia</h1>
<p class="lead">Rental businesses hold sensitive information: licences, addresses, payments. Here's how RentalFleetBook protects it.</p></div></section>
<section><div class="wrap"><div class="grid-4">{cards}</div>
<p class="note" style="margin-top:28px">Questions about security or privacy? Read our <a href="/privacy.html">privacy policy</a> or <a href="/contact/">contact us</a>.</p></div></section>
{cta_band()}'''
    return page("/security/", "Security & Data Hosting in Australia | RentalFleetBook",
                "How RentalFleetBook protects rental business data: hosted in Sydney, encrypted, separated per company, role-based access, daily backups, Stripe payments and secure Xero sign-in.",
                body, None, crumbs)


def contact() -> str:
    crumbs = [("Home", "/"), ("Contact", "/contact/")]
    body = f'''
<section class="page-hero"><div class="wrap grid" style="align-items:start">
<div>{breadcrumbs(crumbs)}<div class="eyebrow">Book a demo</div>
<h1 style="font-size:clamp(2rem,4.2vw,3rem)">See RentalFleetBook with your own fleet in mind</h1>
<p class="lead">Tell us a little about your business and we'll call you to arrange a short demo, usually within one business day. Or start your free month and look around yourself.</p>
<ul class="checks"><li>A 20–30 minute walkthrough, online or by phone</li><li>Your questions about hires, Xero, fines and servicing answered</li><li>Help importing your cars and setting up your agreement</li></ul>
<p>Prefer to talk now? Call <a href="{PHONE_HREF}"><b>{PHONE}</b></a>.</p>
<p><a class="btn" href="{APP}/signup">Start your free month instead <span class="arr">→</span></a></p>
</div>
<form class="form" id="lead" novalidate>
<h3 style="margin-bottom:16px">Book a demo or ask a question</h3>
<div class="two"><label>Your name<input name="name" autocomplete="name" required maxlength="120"></label>
<label>Business name<input name="company" autocomplete="organization" maxlength="160"></label></div>
<div class="two"><label>Email<input name="email" type="email" autocomplete="email" required maxlength="160"></label>
<label>Phone<input name="phone" type="tel" autocomplete="tel" maxlength="40"></label></div>
<label>Fleet size<select name="fleet_size"><option value="">Choose…</option><option>1–5 cars</option><option>6–10 cars</option><option>11–20 cars</option><option>21–50 cars</option><option>More than 50 cars</option></select></label>
<label>What would you like?<select name="kind"><option value="demo">Book a demo</option><option value="question">Ask a question</option></select></label>
<label>Message (optional)<textarea name="message" rows="4" maxlength="2000" placeholder="How you rent, what you'd like to see, the best time to call"></textarea></label>
<label class="hp" aria-hidden="true">Leave this empty<input name="website" tabindex="-1" autocomplete="off"></label>
<button class="btn primary" type="submit" style="width:100%">Send</button>
<p class="note" style="margin:12px 0 0">We'll only use your details to reply. See our <a href="/privacy.html">privacy policy</a>.</p>
<p class="msg" role="status" aria-live="polite"></p>
</form>
</div></section>
<script>(function(){{var f=document.getElementById("lead"),m=f.querySelector(".msg"),b=f.querySelector("button");
f.addEventListener("submit",async function(e){{e.preventDefault();m.className="msg";
var d=Object.fromEntries(new FormData(f).entries());d.page=location.pathname;
if(!d.name||!/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(d.email)){{m.className="msg err";m.textContent="Please enter your name and a valid email.";return}}
b.disabled=true;b.textContent="Sending…";
try{{var r=await fetch("{APP}/api/leads",{{method:"POST",headers:{{"Content-Type":"application/json"}},body:JSON.stringify(d)}});
if(!r.ok)throw 0;f.reset();m.className="msg ok";m.textContent="Thanks! We'll be in touch within one business day.";b.textContent="Sent"}}
catch(_){{b.disabled=false;b.textContent="Send";m.className="msg err";m.textContent="Sorry, that didn't send. Please call {PHONE} instead."}}}})}})()</script>'''
    return page("/contact/", "Book a Demo | Contact RentalFleetBook",
                "Book a demo of RentalFleetBook, the car rental fleet management software built in Melbourne. Or call +61 448 019 043.",
                body, None, crumbs)


def legal(path: str, body_file: Path, title: str, desc: str) -> str:
    """Legal page (privacy/terms) in the site layout; wording comes from _src/legal/*.body.html."""
    inner = body_file.read_text(encoding="utf-8")
    body = f'<section style="padding-top:56px"><div class="wrap prose">{inner}</div></section>'
    return page(path, title, desc, body)


def not_found() -> str:
    body = f'''<section class="page-hero"><div class="wrap center"><div class="eyebrow">404</div><h1>Page not found</h1>
<p class="lead">That page doesn't exist. Try the home page, or log in to RentalFleetBook.</p>
<div class="cta" style="justify-content:center;margin-top:20px"><a class="btn primary" href="/">Home</a><a class="btn" href="{APP}/login">Log in</a></div></div></section>'''
    return page("/404.html", "Page not found | RentalFleetBook", "Page not found.", body)
