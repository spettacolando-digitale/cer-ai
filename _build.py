# Genera le pagine del sito CER-AI (testata, menu e piè di pagina comuni)
import os
HERE = os.path.dirname(os.path.abspath(__file__))
EMAIL = "amministrazione@cer-ai.it"
WEB = "www.cer-ai.it"
MENU = []
LEGAL = [("privacy.html", "Privacy"), ("cookie.html", "Cookie"), ("note-legali.html", "Note legali")]

def head(title, desc):
    return f'''<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="style.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='12' fill='%232DA22D'/%3E%3Ctext x='32' y='42' font-family='Georgia' font-weight='700' font-size='26' fill='%23fff' text-anchor='middle'%3ECA%3C/text%3E%3C/svg%3E">
</head>
'''

def footer():
    links = " ".join(f'<a href="{h}">{t}</a>' for h, t in LEGAL)
    return f'''<footer><div class="wrap">
<div><b class="fname"><em class="c1">CER</em><em class="c2">-AI</em></b> · Intelligenza green · <a href="mailto:{EMAIL}">{EMAIL}</a></div>
<nav>{links}<span>© 2026 CER-AI</span></nav>
</div></footer>
'''

def page(fname, title, desc, hero_tag, hero_title, hero_lead, body):
    ON = ' class="on"'
    MENUBTN = ("<button class=\"menu-btn\" onclick=\"document.getElementById('nav').classList.toggle('open')\" aria-label=\"Apri il menu\">Menu</button><nav id=\"nav\">" + "".join(f'<a href="{h}">{t}</a>' for h, t in MENU) + "</nav>") if MENU else ""
    nav = "".join(f'<a href="{h}"{ON if h == fname else ""}>{t}</a>' for h, t in MENU)
    html = head(f"{title} · CER-AI", desc) + f'''<body>
<header class="top"><div class="wrap">
<a class="brand sm" href="index.html" aria-label="CER-AI, torna alla home"><b><em class="c1">CER</em><em class="c2">-AI</em></b><span>Intelligenza green</span></a>
{MENUBTN}
</div></header>
<div class="hero"><div class="wrap">
<div class="tag">{hero_tag}</div>
<h1>{hero_title}</h1>
{f'<p class="lead" style="color:var(--chiaro)">{hero_lead}</p>' if hero_lead else ''}
</div></div>
<main>
{body}
</main>
{footer()}</body>
</html>
'''
    open(os.path.join(HERE, fname), "w").write(html)

# HOME: prelancio, solo marchio
open(os.path.join(HERE, "index.html"), "w").write(head("CER-AI · Intelligenza green", "CER-AI · Intelligenza green: meno sprechi di energia, meno CO₂, lavoro sul territorio e intelligenza artificiale al servizio della comunità. Presto online.") + f'''<body class="home">
<main><div>
<a class="brand" href="index.html"><b><em class="c1">CER</em><em class="c2">-AI</em></b><span>Intelligenza green</span></a>
<p class="teaser">Stiamo preparando un progetto che restituisce valore alla comunità: meno sprechi di energia, meno CO₂, nuovo lavoro sul territorio. Con lo sguardo rivolto al futuro: l'intelligenza artificiale integrata nel tessuto sociale ed economico locale.</p>
<div class="pillars">
<div><b>Meno sprechi</b><span>di energia</span></div>
<div><b>Meno CO₂</b><span>per l'ambiente</span></div>
<div><b>Più lavoro</b><span>sul territorio</span></div>
<div><b>AI</b><span>al servizio della comunità</span></div>
</div>
<p style="margin-top:34px"><a class="pill on" href="#aderisci">Aderisci</a> <a class="pill" href="#obiettivi">Obiettivi</a> <a class="pill" href="#cer">Cos'è una CER</a> <a class="pill" href="#mappa">La mappa</a></p>
</div></main>
<section id="obiettivi"><div class="wrap">
<h2 style="margin-top:0">I nostri obiettivi</h2>
<p class="lead">Dove vogliamo arrivare, tappa dopo tappa. Sono traguardi da raggiungere insieme, non risultati già ottenuti.</p>
<div class="tappe" role="tablist" aria-label="Tappe">
<button role="tab" data-t="0" class="on">2028<span>il primo polo</span></button>
<button role="tab" data-t="1">2030<span>5 poli</span></button>
<button role="tab" data-t="2">2032<span>13 poli</span></button>
<button role="tab" data-t="3">2035<span>fino a 39 MW</span></button>
</div>
<div class="counters">
<div class="ctr"><b data-v="1,5,13,39">1</b><span>MW di intelligenza artificiale alimentati con energia 100% rinnovabile certificata</span></div>
<div class="ctr"><b data-v="580,2900,7600,19100">580</b><span>tonnellate di CO₂ evitate ogni anno</span></div>
<div class="ctr"><b data-v="2200,11200,29000,87100">2.200</b><span>MWh di energia elettrica risparmiata ogni anno</span></div>
<div class="ctr"><b data-v="1,5,13,13">1</b><span>comunità energetiche attive</span></div>
</div>
<p class="small">Stime di ordine di grandezza, aggiornate man mano che il progetto avanza.</p>
</div></section>
<section id="cer" class="alt"><div class="wrap">
<h2 style="margin-top:0">Cos'è una CER, in parole semplici</h2>
<p class="lead">Una Comunità Energetica Rinnovabile è un gruppo di famiglie, imprese ed enti della stessa zona che si mettono insieme per usare l'energia pulita prodotta vicino a casa.</p>
<div class="grid3">
<div class="card"><h3>1. Si produce</h3>Pannelli solari sui tetti o sulle pensiline della zona producono energia pulita.</div>
<div class="card"><h3>2. Si condivide</h3>L'energia prodotta e quella consumata nello stesso momento dai soci viene "condivisa" dentro la comunità.</div>
<div class="card"><h3>3. Si guadagna</h3>Per l'energia condivisa lo Stato riconosce un incentivo per 20 anni, che la comunità ripartisce tra i soci.</div>
</div>
<div class="band">Non si cambia fornitore, non si cambia contratto, non serve avere pannelli: si aderisce e si partecipa ai benefici.</div>
<div class="gse"><div><h3 style="margin:0 0 4px">Trova la tua cabina primaria</h3>Le comunità energetiche si organizzano per cabina primaria: possono condividere l'energia solo i soci collegati alla stessa cabina. Cerca il tuo indirizzo sulla mappa ufficiale del GSE.</div><a class="btn" href="https://www.gse.it/servizi-per-te/autoconsumo/mappa-interattiva-delle-cabine-primarie" target="_blank" rel="noopener">Apri la mappa del GSE</a></div>
</div></section>
<section id="mappa" class="alt"><div class="wrap">
<h2 style="margin-top:0">Dove raccogliamo le adesioni</h2>
<p class="lead">Circa 1.170 comuni in tutta Italia. Cerca il tuo e aderisci da qui.</p>
<div class="mapbox">
<div class="mapside">
<label for="cerca">Cerca il tuo Comune</label>
<input id="cerca" list="lista-comuni" placeholder="Scrivi il nome del Comune" autocomplete="off">
<datalist id="lista-comuni"></datalist>
<div id="esito" class="esito">Tocca un punto sulla mappa o cerca il nome.</div>
<p class="small" style="margin-top:14px"><span class="dot"></span> Comuni dove sono aperte le pre-adesioni. Il tuo non c'è? Scrivici comunque: la lista cresce.</p>
</div>
<svg id="italia" viewBox="40 20 860 1050" role="img" aria-label="Mappa dei comuni dove sono aperte le pre-adesioni"></svg>
</div>
</div></section>
<section id="aderisci"><div class="wrap contact">
<div>
<h2 style="margin-top:0">Le adesioni sono aperte</h2>
<p class="lead">Non solo nel nostro Comune: raccogliamo le manifestazioni di interesse di famiglie, imprese ed enti in tutti i comuni della mappa.</p>
<form id="adesioni" name="adesioni">
<div><label for="comune">Il tuo Comune</label><input id="comune" name="comune" required list="lista-comuni" autocomplete="off"></div>
<div><label for="tipo">Aderisco come</label><select id="tipo" name="tipo"><option>Famiglia</option><option>Impresa</option><option>Ente pubblico</option><option>Condominio</option><option>Altro</option></select></div>
<div><label for="contatto">Email o numero di telefono</label><input id="contatto" name="contatto" required pattern="^([^@\\s]+@[^@\\s]+\\.[^@\\s]+|\\+?[0-9 ]{{8,16}})$" title="Inserisci un indirizzo email oppure un numero di telefono"></div>
<p class="small">Ti chiediamo solo un recapito per ricontattarti: niente nome, indirizzo o altri dati.</p>
<p class="small"><label style="font-weight:400;color:inherit"><input type="checkbox" name="privacy" required style="width:auto;margin-right:8px">Ho letto l'<a href="privacy.html">informativa privacy</a> e acconsento a essere ricontattato.</label></p>
<div><button class="btn" type="submit">Invia la pre-adesione</button></div>
<p id="esito-invio" class="small" aria-live="polite"></p>
</form>
</div>
<div><div class="card"><h3>Cosa significa</h3><p>È una manifestazione di interesse, gratuita e senza impegno. Quando la comunità energetica della tua zona sarà costituita ti contatteremo con il regolamento e il modulo di adesione vero e proprio.</p><p class="small">Per informazioni: <a href="mailto:{EMAIL}">{EMAIL}</a></p></div></div>
</div></section>
{footer()}<script src="mappa.js" defer></script></body>
</html>
''')

page("privacy.html", "Privacy", "Informativa privacy del sito CER-AI.", "Informativa", "Privacy", "",
 f'''<section><div class="wrap legal">
<p>Informativa ai sensi degli artt. 13-14 del Regolamento UE 2016/679 (GDPR).</p>
<h2>Titolare del trattamento</h2><p>CER-AI – email <a href="mailto:{EMAIL}">{EMAIL}</a>. I dati identificativi completi del titolare sono comunicati su richiesta allo stesso indirizzo.</p>
<h2>Dati raccolti</h2><p>Solo il recapito che inserisci nel modulo di pre-adesione (email oppure numero di telefono), insieme al Comune e al tipo di aderente; oppure i dati che ci invii via email. Non chiediamo nome, indirizzo o altri dati.</p>
<h2>Finalità e base giuridica</h2><p>Registrare la tua manifestazione di interesse, ricontattarti quando sarà possibile aderire alla comunità energetica della tua zona e rispondere alle tue richieste, sulla base del tuo consenso.</p>
<h2>Conservazione</h2><p>I dati sono conservati per il tempo necessario a gestire la richiesta e comunque non oltre 24 mesi, salvo rapporti successivi.</p>
<h2>Destinatari</h2><p>I dati non sono diffusi. Il modulo non passa da servizi esterni: compone un messaggio email che parte dal tuo programma di posta verso il nostro indirizzo. Il sito è ospitato da GitHub Pages (GitHub, Inc.), che può registrare dati tecnici di navigazione come l'indirizzo IP per finalità di sicurezza; la posta è gestita dal nostro fornitore del servizio email, che opera come responsabile del trattamento con garanzie adeguate per il trasferimento extra UE.</p>
<h2>I tuoi diritti</h2><p>Puoi chiedere accesso, rettifica, cancellazione, limitazione, portabilità e opporti al trattamento scrivendo a <a href="mailto:{EMAIL}">{EMAIL}</a>. Puoi proporre reclamo al Garante per la protezione dei dati personali.</p>
<p class="small">Ultimo aggiornamento: ottobre 2026.</p>
</div></section>''')

page("cookie.html", "Cookie", "Cookie policy del sito CER-AI.", "Informativa", "Cookie", "",
 '''<section><div class="wrap legal">
<p>Questo sito non usa cookie di profilazione né strumenti di statistica di terze parti, e non carica caratteri o contenuti da server esterni.</p>
<p>Il fornitore di hosting può usare soltanto cookie tecnici strettamente necessari al funzionamento e alla sicurezza del sito, per i quali non serve il consenso.</p>
<p class="small">Ultimo aggiornamento: ottobre 2026.</p>
</div></section>''')

page("note-legali.html", "Note legali", "Note legali del sito CER-AI.", "Informazioni", "Note legali", "",
 f'''<section><div class="wrap legal">
<p>Testi e grafica sono di proprietà di CER-AI. È vietata la riproduzione senza autorizzazione.</p>
<p>Per informazioni: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</div></section>''')

page("grazie.html", "Grazie", "Pre-adesione ricevuta.", "Adesioni", "Grazie, pre-adesione ricevuta",
 "Ti contatteremo quando la comunità energetica della tua zona sarà costituita.", '<section><div class="wrap"><a class="btn" href="index.html">Torna alla home</a></div></section>')

page("404.html", "Pagina non trovata", "Pagina non trovata.", "Errore 404", "Pagina non trovata",
 "La pagina che cerchi non esiste o è stata spostata.", '<section><div class="wrap"><a class="btn" href="index.html">Torna alla home</a></div></section>')
print("ok")
