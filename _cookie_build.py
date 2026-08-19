# -*- coding: utf-8 -*-
"""Cerez bildirimi + onay kapili GA4. Tek kaynak: hem index.html hem _build.py buradan besleniyor."""

GA_ID = "G-DNFV21E4BS"

T = {
 "tr": ("Bu sitede ziyaret istatistiklerini ölçmek için çerez kullanılıyor. Analitik çerezler yalnızca onayınızla çalışır.", "Kabul et", "Reddet"),
 "en": ("This site uses cookies to measure visit statistics. Analytics cookies run only with your consent.", "Accept", "Decline"),
 "de": ("Diese Website verwendet Cookies zur Messung von Besuchsstatistiken. Analyse-Cookies laufen nur mit Ihrer Einwilligung.", "Annehmen", "Ablehnen"),
 "ru": ("Этот сайт использует файлы cookie для оценки статистики посещений. Аналитические cookie работают только с вашего согласия.", "Принять", "Отклонить"),
 "ar": ("يستخدم هذا الموقع ملفات تعريف الارتباط لقياس إحصاءات الزيارة. لا تعمل ملفات التحليلات إلا بموافقتك.", "أوافق", "رفض"),
}

CSS = (
"#ckb{position:fixed;left:0;right:0;bottom:0;z-index:9999;background:#0B1A38;color:#E6ECF6;"
"padding:14px 18px;display:none;gap:14px;align-items:center;justify-content:center;flex-wrap:wrap;"
"font-size:.86rem;line-height:1.5;box-shadow:0 -2px 18px rgba(0,0,0,.22)}"
"#ckb p{margin:0;max-width:62ch}"
"#ckb .ckbtns{display:flex;gap:9px;flex:none}"
"#ckb button{font:inherit;font-weight:600;border-radius:999px;padding:8px 18px;cursor:pointer;border:1px solid transparent}"
"#ckOk{background:#B8934A;color:#0B1A38}"
"#ckNo{background:transparent;color:#E6ECF6;border-color:rgba(230,236,246,.4)}"
"@media(max-width:640px){#ckb{flex-direction:column;align-items:stretch;text-align:center;padding:15px}"
"#ckb .ckbtns{justify-content:center}}"
)

def snippet(escape_braces=False):
    import json
    js = """
<style>%(css)s</style>
<div id="ckb" role="region" aria-label="cookie"><p id="ckt"></p><div class="ckbtns"><button id="ckOk"></button><button id="ckNo"></button></div></div>
<script>
(function(){
var T=%(t)s,L=document.documentElement.lang||'tr',t=T[L]||T.tr,K='ck-consent';
function loadGA(){
 if(window.__ga)return;window.__ga=1;
 var s=document.createElement('script');s.async=1;
 s.src='https://www.googletagmanager.com/gtag/js?id=%(id)s';document.head.appendChild(s);
 window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments)};
 gtag('js',new Date());gtag('config','%(id)s');
}
function ev(m){if(window.gtag)gtag('event','whatsapp_click',{method:m,page_location:location.pathname,language:document.documentElement.lang})}
document.addEventListener('click',function(e){
 var a=e.target&&e.target.closest?e.target.closest('a[href*="wa.me"]'):null;if(!a)return;
 ev(a.classList.contains('tb-wa')?'topbar':a.classList.contains('wa-float')?'float':'cta');
});
window.__waEvent=ev;
var c=null;try{c=localStorage.getItem(K)}catch(_){}
if(c==='1'){loadGA()}
else if(c!=='0'){
 document.addEventListener('DOMContentLoaded',function(){
  var b=document.getElementById('ckb');if(!b)return;
  document.getElementById('ckt').textContent=t[0];
  document.getElementById('ckOk').textContent=t[1];
  document.getElementById('ckNo').textContent=t[2];
  b.style.display='flex';
  document.getElementById('ckOk').onclick=function(){try{localStorage.setItem(K,'1')}catch(_){}b.style.display='none';loadGA()};
  document.getElementById('ckNo').onclick=function(){try{localStorage.setItem(K,'0')}catch(_){}b.style.display='none'};
 });
}
})();
</script>""" % {"css": CSS, "t": json.dumps(T, ensure_ascii=False), "id": GA_ID}
    js = js.strip()
    if escape_braces:
        js = js.replace("{", "{{").replace("}", "}}")
    return js

if __name__ == "__main__":
    open("_ck_plain.html", "w", encoding="utf-8").write(snippet(False))
    open("_ck_esc.html", "w", encoding="utf-8").write(snippet(True))
    print("uretildi")
