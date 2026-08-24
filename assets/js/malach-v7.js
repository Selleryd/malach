document.documentElement.classList.add('js');
const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
const fine = matchMedia('(hover:hover) and (pointer:fine)').matches;

function setupYear(){
  document.querySelectorAll('[data-year]').forEach(el=>el.textContent=new Date().getFullYear());
}

function setupHeader(){
  const header=document.querySelector('[data-header]');
  const line=document.querySelector('[data-scroll-line]');
  let raf=0;
  const update=()=>{
    raf=0;
    const max=Math.max(1,document.documentElement.scrollHeight-innerHeight);
    const ratio=Math.min(1,scrollY/max);
    header?.classList.toggle('is-scrolled',scrollY>10);
    line?.style.setProperty('--scroll-progress',`${ratio*100}%`);
  };
  addEventListener('scroll',()=>{if(!raf)raf=requestAnimationFrame(update)},{passive:true});
  update();
}

function setupMenus(){
  const menus=[...document.querySelectorAll('[data-nav-menu]')];
  const closeAll=(except=null)=>menus.forEach(menu=>{
    if(menu===except)return;
    menu.classList.remove('open');
    menu.querySelector('[data-nav-trigger]')?.setAttribute('aria-expanded','false');
    menu.querySelector('[data-nav-panel]')?.setAttribute('aria-hidden','true');
  });
  menus.forEach(menu=>{
    const trigger=menu.querySelector('[data-nav-trigger]');
    const panel=menu.querySelector('[data-nav-panel]');
    const open=()=>{
      closeAll(menu);
      menu.classList.add('open');
      trigger?.setAttribute('aria-expanded','true');
      panel?.setAttribute('aria-hidden','false');
    };
    const close=()=>{
      menu.classList.remove('open');
      trigger?.setAttribute('aria-expanded','false');
      panel?.setAttribute('aria-hidden','true');
    };
    trigger?.addEventListener('click',e=>{
      e.stopPropagation();
      menu.classList.contains('open')?close():open();
    });
    menu.addEventListener('mouseenter',open);
    menu.addEventListener('mouseleave',close);
  });
  document.addEventListener('click',()=>closeAll());
  addEventListener('keydown',e=>{if(e.key==='Escape')closeAll();});
}

function setupMobile(){
  const trigger=document.querySelector('[data-menu-trigger]');
  const drawer=document.querySelector('[data-mobile-drawer]');
  if(!trigger||!drawer)return;
  const close=()=>{
    trigger.setAttribute('aria-expanded','false');
    drawer.setAttribute('aria-hidden','true');
    document.body.style.overflow='';
  };
  trigger.addEventListener('click',()=>{
    const open=trigger.getAttribute('aria-expanded')==='true';
    trigger.setAttribute('aria-expanded',String(!open));
    drawer.setAttribute('aria-hidden',String(open));
    document.body.style.overflow=open?'':'hidden';
  });
  drawer.querySelectorAll('a').forEach(a=>a.addEventListener('click',close));
  addEventListener('resize',()=>{if(innerWidth>1180)close();});
}

function setupCommand(){
  const palette=document.querySelector('[data-command-palette]');
  if(!palette)return;
  const input=palette.querySelector('.command-input');
  const items=[...palette.querySelectorAll('[data-command-item]')];
  let active=0;
  let visible=items;
  const paint=()=>visible.forEach((item,i)=>item.classList.toggle('active',i===active));
  const filter=()=>{
    const q=input.value.trim().toLowerCase();
    visible=[];
    items.forEach(item=>{
      const show=!q||item.dataset.search.includes(q);
      item.hidden=!show;
      if(show)visible.push(item);
    });
    active=0;
    paint();
  };
  const open=()=>{
    palette.setAttribute('aria-hidden','false');
    document.body.style.overflow='hidden';
    input.value='';
    filter();
    setTimeout(()=>input.focus(),30);
  };
  const close=()=>{
    palette.setAttribute('aria-hidden','true');
    document.body.style.overflow='';
  };
  document.querySelectorAll('[data-command-open]').forEach(b=>b.addEventListener('click',open));
  palette.querySelectorAll('[data-command-close]').forEach(b=>b.addEventListener('click',close));
  input.addEventListener('input',filter);
  input.addEventListener('keydown',e=>{
    if(e.key==='ArrowDown'){e.preventDefault();active=Math.min(active+1,visible.length-1);paint();}
    if(e.key==='ArrowUp'){e.preventDefault();active=Math.max(active-1,0);paint();}
    if(e.key==='Enter'&&visible[active])location.href=visible[active].href;
  });
  addEventListener('keydown',e=>{
    if((e.metaKey||e.ctrlKey)&&e.key.toLowerCase()==='k'){e.preventDefault();open();}
    if(e.key==='Escape')close();
  });
}

function setupReveal(){
  const els=[...document.querySelectorAll('.reveal')];
  if(!els.length)return;
  if(reduced||!('IntersectionObserver'in window)){
    els.forEach(el=>el.classList.add('visible'));
    return;
  }
  const obs=new IntersectionObserver(entries=>entries.forEach(entry=>{
    if(entry.isIntersecting){
      entry.target.classList.add('visible');
      obs.unobserve(entry.target);
    }
  }),{threshold:.06,rootMargin:'100px 0px -2%'});
  els.forEach(el=>obs.observe(el));
}

function setupSupport(){
  const form=document.querySelector('[data-support-form]');
  if(!form)return;
  const status=form.querySelector('.form-status');
  form.addEventListener('submit',async e=>{
    e.preventDefault();
    const data=Object.fromEntries(new FormData(form));
    if(data.website)return;
    const button=form.querySelector('[type=submit]');
    button.disabled=true;
    button.textContent='Sending…';
    try{
      const response=await fetch(form.dataset.endpoint||'/api/contact',{
        method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify(data)
      });
      if(!response.ok)throw new Error('send failed');
      status.textContent='Message sent. Malach will respond by email.';
      form.reset();
    }catch{
      const subject=encodeURIComponent(`Malach: ${data.topic||'Question'}`);
      const body=encodeURIComponent(`Name: ${data.name||''}\nEmail: ${data.email||''}\n\n${data.message||''}`);
      location.href=`mailto:support@malach.app?subject=${subject}&body=${body}`;
      status.textContent='Opening your email client…';
    }finally{
      button.disabled=false;
      button.textContent='Send message';
    }
  });
}

function setupSpotlights(){
  if(!fine||reduced)return;
  const selector=[
    '.v7-command-deck','[data-tilt-surface]','.story-panel','.authority-visual',
    '.vision-console','.price-card','.market-console','.reconcile-console',
    '.chat-console','.security-console','.v7-channel-screen','.v7-flow-stage'
  ].join(',');
  document.querySelectorAll(selector).forEach(surface=>{
    let raf=0;
    surface.addEventListener('pointermove',e=>{
      if(raf)return;
      raf=requestAnimationFrame(()=>{
        raf=0;
        const r=surface.getBoundingClientRect();
        surface.style.setProperty('--mx',`${((e.clientX-r.left)/r.width)*100}%`);
        surface.style.setProperty('--my',`${((e.clientY-r.top)/r.height)*100}%`);
      });
    },{passive:true});
  });
}

setupYear();
setupHeader();
setupMenus();
setupMobile();
setupCommand();
setupReveal();
setupSupport();
setupSpotlights();
document.documentElement.dataset.malachReady='true';
