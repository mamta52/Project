const p=document.querySelector(".particles");
if(p){setInterval(()=>{const x=document.createElement("span");x.className="particle";x.textContent=["♡","♥","✦","⋆"][Math.floor(Math.random()*4)];x.style.left=Math.random()*100+"vw";x.style.fontSize=12+Math.random()*18+"px";x.style.animationDuration=7+Math.random()*7+"s";p.appendChild(x);setTimeout(()=>x.remove(),15000)},650)}
const env=document.getElementById("envelope");
if(env){env.addEventListener("click",()=>{env.classList.add("open");setTimeout(()=>document.getElementById("letter").classList.add("show"),700)})}
const btn=document.getElementById("moreLove");
if(btn){const reasons=["Because your presence feels like home. ♡","Because somehow you make me smile without trying.","Because I want to keep discovering all your little sides.","Because loving you feels like my favorite thing. 💜","Because you are you — and that's enough."];btn.addEventListener("click",()=>{document.getElementById("lovePop").textContent=reasons[Math.floor(Math.random()*reasons.length)]})}
