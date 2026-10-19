// Mappa dei comuni con pre-adesioni aperte (nessuna libreria esterna)
(function () {
  var svg = document.getElementById('italia');
  if (!svg) return;
  var NS = 'http://www.w3.org/2000/svg';
  var esito = document.getElementById('esito');
  var cerca = document.getElementById('cerca');
  var lista = document.getElementById('lista-comuni');
  var campo = document.getElementById('comune');
  var dots = {}, scelto = null;

  function nome(p) { return p[0] + ' (' + p[1] + ')'; }

  function seleziona(p) {
    if (scelto) scelto.classList.remove('on');
    var c = dots[nome(p)];
    if (c) { c.classList.add('on'); c.parentNode.appendChild(c); scelto = c; }
    esito.innerHTML = '';
    var b = document.createElement('b'); b.textContent = p[0];
    var s = document.createElement('span'); s.textContent = 'Provincia ' + p[1] + ' · ' + p[2] + ' — pre-adesioni aperte';
    var a = document.createElement('a'); a.className = 'btn'; a.href = '#aderisci'; a.textContent = 'Aderisci da qui';
    a.addEventListener('click', function () { if (campo) campo.value = nome(p); });
    esito.appendChild(b); esito.appendChild(s); esito.appendChild(a);
  }

  fetch('comuni.json').then(function (r) { return r.json(); }).then(function (d) {
    var g = document.createElementNS(NS, 'g');
    d.paths.forEach(function (pd) {
      var p = document.createElementNS(NS, 'path'); p.setAttribute('d', pd); p.setAttribute('class', 'reg'); g.appendChild(p);
    });
    svg.appendChild(g);
    var gd = document.createElementNS(NS, 'g');
    var frag = document.createDocumentFragment();
    d.pts.sort(function (a, b) { return a[0].localeCompare(b[0], 'it'); });
    d.pts.forEach(function (p) {
      var c = document.createElementNS(NS, 'circle');
      c.setAttribute('cx', p[3]); c.setAttribute('cy', p[4]); c.setAttribute('r', 4.2); c.setAttribute('class', 'pt');
      var t = document.createElementNS(NS, 'title'); t.textContent = nome(p); c.appendChild(t);
      c.addEventListener('click', function () { seleziona(p); });
      gd.appendChild(c); dots[nome(p)] = c;
      var o = document.createElement('option'); o.value = nome(p); frag.appendChild(o);
    });
    svg.appendChild(gd);
    lista.appendChild(frag);
    var byName = {}; d.pts.forEach(function (p) { byName[nome(p).toLowerCase()] = p; byName[p[0].toLowerCase()] = byName[p[0].toLowerCase()] || p; });
    cerca.addEventListener('input', function () {
      var p = byName[cerca.value.trim().toLowerCase()];
      if (p) seleziona(p);
    });
  }).catch(function () { esito.textContent = 'Mappa non disponibile al momento.'; });
})();

// Pre-adesione: compone una email verso l'indirizzo del progetto (nessun servizio esterno)
(function () {
  var f = document.getElementById('adesioni');
  if (!f) return;
  f.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!f.reportValidity()) return;
    var v = function (id) { return (document.getElementById(id).value || '').trim(); };
    var body = 'Pre-adesione al progetto CER-AI\n\nComune: ' + v('comune') + '\nAderisco come: ' + v('tipo') +
      '\nRecapito: ' + v('contatto') + '\n\nHo letto l\'informativa privacy e acconsento a essere ricontattato.';
    var url = 'mailto:amministrazione@cer-ai.it?subject=' + encodeURIComponent('Pre-adesione CER-AI - ' + v('comune')) + '&body=' + encodeURIComponent(body);
    window.location.href = url;
    var es = document.getElementById('esito-invio');
    if (es) es.textContent = 'Si è aperto il tuo programma di posta con il messaggio già pronto: premi Invia per completare. Se non si apre, scrivi ad amministrazione@cer-ai.it indicando Comune e recapito.';
  });
})();

// Contatori degli obiettivi per tappa
(function () {
  var box = document.getElementById('obiettivi');
  if (!box) return;
  var btns = box.querySelectorAll('.tappe button'), nums = box.querySelectorAll('.ctr b');
  var fmt = function (n) { return Math.round(n).toLocaleString('it-IT'); };
  var calma = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var cur = [].map.call(nums, function () { return 0; });
  function vai(t) {
    [].forEach.call(btns, function (b, i) { b.classList.toggle('on', i === t); b.setAttribute('aria-selected', i === t); });
    [].forEach.call(nums, function (el, k) {
      var da = cur[k], a = +el.dataset.v.split(',')[t]; cur[k] = a;
      if (calma) { el.textContent = fmt(a); return; }
      var t0 = null;
      function passo(ts) { if (!t0) t0 = ts; var p = Math.min(1, (ts - t0) / 1200); p = 1 - Math.pow(1 - p, 3);
        el.textContent = fmt(da + (a - da) * p); if (p < 1) requestAnimationFrame(passo); }
      requestAnimationFrame(passo);
    });
  }
  [].forEach.call(btns, function (b, i) { b.addEventListener('click', function () { vai(i); }); });
  var avviato = false;
  function avvia() { if (!avviato) { avviato = true; vai(0); } }
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (e, o) { if (e[0].isIntersecting) { avvia(); o.disconnect(); } }, { threshold: 0.3 }).observe(box);
  } else avvia();
})();
