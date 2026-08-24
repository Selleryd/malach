const ENDPOINT='/api/health';
const $=selector=>document.querySelector(selector);
const title=$('[data-status-title]');
const summary=$('[data-status-summary]');
const state=$('[data-status-state]');
const detail=$('[data-status-detail]');
const checked=$('[data-status-checked]');
const dot=$('[data-status-dot]');
const services=[...document.querySelectorAll('[data-service-state]')];
const stamp=()=>new Intl.DateTimeFormat(undefined,{hour:'numeric',minute:'2-digit',second:'2-digit'}).format(new Date());

function setServices(label,className=''){
  services.forEach(element=>{
    element.textContent=label;
    element.className=className;
  });
}

function checking(){
  title.textContent='Checking Malach…';
  summary.textContent='Running a live availability check.';
  state.textContent='Checking systems';
  detail.textContent='Confirming application availability.';
  checked.textContent='Checking now';
  dot.className='status-dot checking';
  setServices('Checking');
}

function healthy(){
  title.textContent='No issues detected.';
  summary.textContent='All systems active.';
  state.textContent='All systems operational';
  detail.textContent='Malach is reachable and operating normally.';
  checked.textContent=`Last checked ${stamp()}`;
  dot.className='status-dot is-healthy';
  setServices('Operational','is-healthy');
}

function degraded(){
  title.textContent='Malach may be experiencing an interruption.';
  summary.textContent='Live availability could not be confirmed.';
  state.textContent='Service interruption detected';
  detail.textContent='Please try again shortly. Support is available if the issue continues.';
  checked.textContent=`Last checked ${stamp()}`;
  dot.className='status-dot is-degraded';
  setServices('Unavailable','is-degraded');
}

async function check(){
  checking();
  const controller=new AbortController();
  const timeout=setTimeout(()=>controller.abort(),9000);
  try{
    const response=await fetch(ENDPOINT,{cache:'no-store',signal:controller.signal});
    const body=await response.json().catch(()=>({}));
    response.ok&&body?.ok===true?healthy():degraded();
  }catch{
    degraded();
  }finally{
    clearTimeout(timeout);
  }
}

$('[data-status-refresh]')?.addEventListener('click',check);
check();
setInterval(check,45000);
