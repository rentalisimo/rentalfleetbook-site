"""Illustrative product UI mock-ups (HTML/CSS, made-up data) used across the website."""

NOTE = '<p class="mock-note">Illustrative example with made-up data.</p>'


def plate(rego: str) -> str:
    return f'<div class="plate">{rego}<small>VICTORIA</small></div>'


def row(rego, title, sub, pill, kind="") -> str:
    return f'<div class="row">{plate(rego)}<div class="t">{title}<small>{sub}</small></div><span class="pill {kind}">{pill}</span></div>'


def dashboard(note=True) -> str:
    side = "".join(f'<span class="{"on" if i == 0 else ""}">{n}</span>' for i, n in enumerate(
        ["Overview", "Fleet", "Hires", "Invoices", "Fines & tolls", "Servicing", "Live map", "Reports"]))
    rows = "".join([
        row("1AB2CD", "Toyota Camry Hybrid · On hire", "Weekly $350 · paid to 26 Nov", "Paid", "ok"),
        row("2XY7KL", "Parking fine · City of Kingston", "Matched to hirer · nominate by 2 Dec", "To nominate", "warn"),
        row("ZQR418", "Kia Carnival · Service due", "Next service at 180,000 km · 320 km to go", "Due soon", "info"),
        row("3MN5PT", "Hyundai i30 · Rent overdue", "$700 owing · reminder sent today", "Overdue", "crit"),
    ])
    return f'''<div class="app" role="img" aria-label="RentalFleetBook dashboard example">
<div class="bar"><i></i><i></i><i></i><span>app.rentalfleetbook.com</span></div>
<div class="body"><div class="side"><b><em>RF</em>RentalFleetBook</b>{side}</div>
<div class="main"><h5>Fleet overview</h5>
<div class="kpis"><div class="kpi"><small>Vehicles</small><strong>32</strong></div><div class="kpi"><small>On hire</small><strong>24</strong></div>
<div class="kpi"><small>Weekly hire value</small><strong>$8,450</strong></div><div class="kpi warn"><small>Actions</small><strong>3</strong></div></div>
<div class="rows">{rows}</div></div></div></div>{NOTE if note else ""}'''


def fleet() -> str:
    rows = "".join([
        row("1AB2CD", "Toyota Camry Hybrid 2021", "Rego to 14 Mar · insured · 142,310 km", "On hire", "info"),
        row("7GH3JK", "Kia Carnival 2020", "Rego to 2 Dec · insured · 188,940 km", "Rego due", "warn"),
        row("ZQR418", "Toyota Corolla 2019", "Rego to 30 Jun · insured · 96,120 km", "Available", "ok"),
        row("5TU8VW", "Hyundai i30 2022", "Rego to 8 Aug · insured · 61,005 km", "In service", ""),
    ])
    return f'<div class="mini"><h5>Fleet <span class="pill">32 vehicles</span></h5><div class="rows">{rows}</div></div>{NOTE}'


def agreement() -> str:
    return f'''<div class="mini"><h5>Hire agreement <span class="pill ok">Ready to sign</span></h5>
<div class="line"><span class="muted">Hirer</span><b>Daniel M.</b></div>
<div class="line"><span class="muted">Vehicle</span><b>1AB2CD · Toyota Camry</b></div>
<div class="line"><span class="muted">Weekly rent · Bond</span><b>$350 · $1,000</b></div>
<div class="line"><span class="muted">Pickup inspection</span><b>12 photos · 1 existing mark</b></div>
<div class="sig"><svg width="160" height="42" viewBox="0 0 160 42" fill="none" stroke="#0B1B3F" stroke-width="2" stroke-linecap="round"><path d="M6 30c10-22 18-22 16-4s10 6 18-6 6 22 22 6 12-14 18-2 14 4 22-8 18 6 30 0"/></svg></div>
<p class="muted" style="margin:10px 0 0;font-size:12.5px">Signed copy and insurance papers emailed to the hirer automatically.</p></div>{NOTE}'''


def invoices() -> str:
    return f'''<div class="mini"><h5>Billing for this hire <span class="pill info">Synced with Xero</span></h5>
<div class="line"><span>First invoice · week 1 + bond<br><span class="muted">Dated the signing day</span></span><b>$1,350 <span class="pill ok">Paid</span></b></div>
<div class="line"><span>Weekly repeating invoice<br><span class="muted">Every Wednesday from day 7</span></span><b>$350 <span class="pill info">Active</span></b></div>
<div class="line"><span>Invoice INV-6182<br><span class="muted">Due 19 Nov</span></span><b>$350 <span class="pill crit">Overdue</span></b></div>
<div class="line"><span>Reminder<br><span class="muted">SMS + email with total owing</span></span><b><span class="pill">Sent today</span></b></div></div>{NOTE}'''


def fine() -> str:
    return f'''<div class="mini"><h5>Parking infringement <span class="pill warn">To nominate</span></h5>
<div class="line"><span class="muted">Notice</span><b>City of Kingston · $99</b></div>
<div class="line"><span class="muted">Offence</span><b>2XY7KL · 14 Nov, 10:42 am</b></div>
<div class="line"><span class="muted">Who had the car</span><b>Priya S. · hire since 3 Nov</b></div>
<div class="line"><span class="muted">Nominate by</span><b>2 Dec</b></div>
<div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:12px"><span class="btn sm primary" style="box-shadow:none">Copy all details</span><span class="btn sm">Open council site</span><span class="btn sm">Not on hire</span></div></div>{NOTE}'''


def service() -> str:
    rows = "".join([
        row("ZQR418", "Minor service · 172,400 km", "From mechanic invoice · $420 · bill sent to Xero", "Done", "ok"),
        row("7GH3JK", "Next service at 190,000 km", "1,060 km to go", "Due soon", "warn"),
        row("5TU8VW", "Brake pads + rotors", "Booked Thursday", "In service", "info"),
        row("4CD9EF", "Service overdue by 2,300 km", "Last service 11 Jun", "Overdue", "crit"),
    ])
    return f'<div class="mini"><h5>Servicing <span class="pill">Sorted by due date</span></h5><div class="rows">{rows}</div></div>{NOTE}'


def gps() -> str:
    return f'''<div class="mini"><h5>Live map <span class="pill ok">24 cars reporting</span></h5>
<div class="mapbox"><svg viewBox="0 0 420 220" width="100%" height="220" aria-hidden="true">
<rect width="420" height="220" fill="#EEF3F8"/>
<path d="M0 60h420M0 140h420M90 0v220M210 0v220M330 0v220" stroke="#fff" stroke-width="10"/>
<path d="M0 100 C120 80 160 180 260 150 S380 60 420 90" stroke="#fff" stroke-width="14" fill="none"/>
<path d="M40 180 L90 140 L150 140 L210 100 L260 150 L330 120" stroke="#2563EB" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="1 0"/>
<circle cx="40" cy="180" r="6" fill="#fff" stroke="#2563EB" stroke-width="3"/>
<circle cx="330" cy="120" r="9" fill="#2563EB"/><circle cx="330" cy="120" r="16" fill="#2563EB" opacity=".15"/>
<circle cx="120" cy="60" r="7" fill="#15803D"/><circle cx="270" cy="200" r="7" fill="#15803D"/><circle cx="380" cy="40" r="7" fill="#B45309"/>
</svg></div>
<div class="line" style="margin-top:8px"><span class="muted">1AB2CD this week</span><b>612 km · 9 trips</b></div>
<div class="line"><span class="muted">Weekly limit</span><b>1,000 km</b></div></div>{NOTE}'''


def utilisation() -> str:
    def u(rego, pct):
        tone = "#15803D" if pct >= 80 else "#B45309" if pct >= 50 else "#B91C1C"
        return f'<div class="row" style="grid-template-columns:78px 1fr 46px">{plate(rego)}<div class="bar-h"><i style="width:{pct}%;background:{tone}"></i></div><b style="color:#0B1B3F;text-align:right">{pct}%</b></div>'
    return f'''<div class="mini"><h5>Fleet utilisation · last 30 days <span class="pill info">84%</span></h5>
<div class="rows">{u("1AB2CD", 100)}{u("7GH3JK", 93)}{u("ZQR418", 71)}{u("5TU8VW", 38)}</div></div>{NOTE}'''


def inbox() -> str:
    rows = "".join([
        row("2XY7KL", "Infringement notice · read by AI", "Matched to Priya S. · added to Fines", "Filed", "ok"),
        row("ZQR418", "Mechanic invoice · read by AI", "Minor service · odometer 172,400", "Filed", "ok"),
        row("7GH3JK", "VicRoads renewal · read by AI", "Rego due 2 Dec · bill sent to Xero", "Filed", "ok"),
        row("1AB2CD", "Toll statement · read by AI", "3 trips · recharge to hirer", "Review", "warn"),
    ])
    return f'<div class="mini"><h5>AI paperwork inbox <span class="ai-chip" style="margin:0">{SPARK} AI</span></h5><div class="rows">{rows}</div></div>{NOTE}'


SPARK = '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l1.9 5.6L19.5 9.5l-5.6 1.9L12 17l-1.9-5.6L4.5 9.5l5.6-1.9zM19 14l.9 2.6 2.6.9-2.6.9L19 21l-.9-2.6-2.6-.9 2.6-.9z"/></svg>'


def ai_read() -> str:
    """An infringement notice being read by AI: document on the left, fields on the right."""
    doc = '''<div style="background:#fff;border:1px solid var(--line);border-radius:10px;padding:14px;font-size:10.5px;color:#64748B;line-height:1.5;box-shadow:0 1px 2px rgba(11,27,63,.06)">
<div style="font-weight:800;color:#0B1B3F;font-size:11.5px;margin-bottom:6px">INFRINGEMENT NOTICE</div>
<div style="height:6px;background:#E4E9F2;border-radius:3px;margin:6px 0;width:90%"></div><div style="height:6px;background:#E4E9F2;border-radius:3px;margin:6px 0;width:70%"></div>
<div style="background:rgba(37,99,235,.12);outline:1.5px solid #2563EB;border-radius:4px;padding:2px 4px;margin:8px 0;color:#0B1B3F">Vehicle 2XY7KL · 14/11 10:42</div>
<div style="height:6px;background:#E4E9F2;border-radius:3px;margin:6px 0;width:80%"></div>
<div style="background:rgba(37,99,235,.12);outline:1.5px solid #2563EB;border-radius:4px;padding:2px 4px;margin:8px 0;color:#0B1B3F">Penalty $99 · Pay by 2/12</div>
<div style="height:6px;background:#E4E9F2;border-radius:3px;margin:6px 0;width:60%"></div><div style="height:6px;background:#E4E9F2;border-radius:3px;margin:6px 0;width:85%"></div></div>'''
    fields = f'''<div><div class="ai-chip">{SPARK} Read by AI in seconds</div>
<div class="line"><span class="muted">Issuer</span><b>City of Kingston</b></div>
<div class="line"><span class="muted">Offence</span><b>2XY7KL · 14 Nov, 10:42</b></div>
<div class="line"><span class="muted">Amount</span><b>$99</b></div>
<div class="line"><span class="muted">Matched to</span><b>Priya S. (on hire)</b></div>
<div style="display:flex;gap:8px;margin-top:10px"><span class="btn sm primary" style="box-shadow:none">Looks right</span><span class="btn sm">Edit</span></div></div>'''
    return f'<div class="mini"><div style="display:grid;grid-template-columns:.85fr 1fr;gap:16px;align-items:start">{doc}{fields}</div></div>{NOTE}'
