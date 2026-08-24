const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
const fine=matchMedia('(hover:hover) and (pointer:fine)').matches;

function setupHero(){
  const stage=document.querySelector('[data-hero-stage]');
  const deck=document.querySelector('[data-hero-console]');
  if(deck)requestAnimationFrame(()=>deck.classList.add('animated'));
  if(stage&&deck&&fine&&!reduced){
    let raf=0;
    stage.addEventListener('pointermove',e=>{
      if(raf)return;
      raf=requestAnimationFrame(()=>{
        raf=0;
        const r=stage.getBoundingClientRect();
        const x=(e.clientX-r.left)/r.width-.5;
        const y=(e.clientY-r.top)/r.height-.5;
        deck.style.setProperty('--hero-ry',`${x*5.5-2.5}deg`);
        deck.style.setProperty('--hero-rx',`${y*-3.5+1}deg`);
      });
    },{passive:true});
    stage.addEventListener('pointerleave',()=>{
      deck.style.setProperty('--hero-ry','-3deg');
      deck.style.setProperty('--hero-rx','1deg');
    });
  }
  const value=document.querySelector('[data-live-value]');
  if(value&&!reduced){
    let tick=0;
    setInterval(()=>{
      if(document.hidden)return;
      tick+=1;
      const base=Number(value.dataset.base||184260);
      const delta=Math.round((Math.sin(tick*.7)+1)*37+tick*3);
      value.textContent=`$${(base+delta).toLocaleString()}`;
    },2600);
  }
}

function setupAuthoritySwitches(){
  const notes={
    observe:'Malach recommends. You decide what gets executed.',
    approval:'Malach prepares the action and waits for your approval.',
    canary:'Malach runs a controlled test inside the approved boundary.',
    full:'Malach executes certified actions within configured safeguards.'
  };
  document.querySelectorAll('[data-authority-switch]').forEach(group=>{
    const note=group.parentElement.querySelector('[data-authority-note]');
    group.querySelectorAll('button').forEach(btn=>btn.addEventListener('click',()=>{
      group.querySelectorAll('button').forEach(b=>b.classList.toggle('active',b===btn));
      if(note)note.textContent=notes[btn.dataset.mode]||'';
    }));
  });
}

function setupProductSignals(){
  const signals=[...document.querySelectorAll('[data-product-signal]')];
  if(!signals.length)return;
  const decision=document.querySelector('.v7-decision-card h3');
  const copy=document.querySelector('.v7-decision-card>p');
  const map={
    aster:['Increase high-intent search while margin remains protected.','Conversion quality cleared break-even. Aster Lamp margin and return risk remain inside the approved range.'],
    sora:['Expand remarketing where repeat demand is strongest.','Sora Carryall has retained contribution across three measured windows with stable return behavior.'],
    ember:['Contain prospecting until return-adjusted profit recovers.','Ember Throw demand remains healthy, but returns pushed contribution below the approved operating range.'],
    drift:['Test a focused shopping expansion with a controlled budget.','Drift Shelf margin supports a canary test while product-level conversion quality remains stable.']
  };
  signals.forEach(btn=>btn.addEventListener('click',()=>{
    signals.forEach(b=>b.classList.toggle('active',b===btn));
    const next=map[btn.dataset.productSignal];
    if(next&&decision&&copy){decision.textContent=next[0];copy.textContent=next[1];}
  }));
}

function setupClarity(){
  const root=document.querySelector('[data-clarity-root]');
  if(!root)return;
  const buttons=[...root.querySelectorAll('[data-clarity]')];
  const panels=[...root.querySelectorAll('[data-clarity-panel]')];
  const copy=root.querySelector('[data-clarity-copy]');
  const messages={
    fragmented:'Disconnected dashboards create delayed, reactive decisions.',
    unified:'Malach turns the same signals into one verified, profit-driven operating picture.'
  };
  buttons.forEach(btn=>btn.addEventListener('click',()=>{
    const key=btn.dataset.clarity;
    buttons.forEach(b=>b.classList.toggle('active',b===btn));
    panels.forEach(panel=>panel.classList.toggle('active',panel.dataset.clarityPanel===key));
    if(copy)copy.textContent=messages[key]||'';
  }));
}

function setupVision(){
  const buttons=[...document.querySelectorAll('[data-vision-channel]')];
  if(!buttons.length)return;
  const value=document.querySelector('[data-vision-value]');
  const bars=[...document.querySelectorAll('.v7-vision-bars i')];
  const states={
    portfolio:{value:'$438,200',bars:['88%','54%','34%']},
    google:{value:'$284,000',bars:['100%','12%','6%']},
    meta:{value:'$96,000',bars:['26%','100%','18%']},
    tiktok:{value:'$58,000',bars:['15%','24%','100%']}
  };
  const activate=btn=>{
    const state=states[btn.dataset.visionChannel];
    if(!state)return;
    buttons.forEach(b=>b.classList.toggle('active',b===btn));
    if(value)value.textContent=state.value;
    bars.forEach((bar,i)=>bar.style.setProperty('--w',state.bars[i]||'0%'));
  };
  buttons.forEach(btn=>btn.addEventListener('click',()=>activate(btn)));
}

function setupFlow(){
  const root=document.querySelector('[data-flow-root]');
  if(!root)return;
  const buttons=[...root.querySelectorAll('[data-flow-step]')];
  const title=root.querySelector('[data-flow-title]');
  const output=root.querySelector('[data-flow-output]');
  const copy=root.querySelector('[data-flow-copy]');
  const states={
    connect:['CONNECTED ECONOMICS','One verified operating picture','Malach connects channel activity to actual store economics before making a recommendation.'],
    analyze:['PROFIT MODEL','Risk-adjusted opportunity','Malach evaluates contribution margin, break-even thresholds, attribution confidence and expected upside.'],
    act:['GOVERNED AUTHORITY','Recommendation or controlled action','Malach uses Observe, Approval, Canary or Full Auto according to the authority you selected.'],
    learn:['OUTCOME LOOP','A better next decision','Malach confirms what changed, measures the result and preserves the evidence for the next decision.']
  };
  buttons.forEach(btn=>btn.addEventListener('click',()=>{
    const state=states[btn.dataset.flowStep];
    buttons.forEach(b=>b.classList.toggle('active',b===btn));
    if(state){if(title)title.textContent=state[0];if(output)output.textContent=state[1];if(copy)copy.textContent=state[2];}
  }));
}

function setupChannels(){
  const root=document.querySelector('[data-channel-command]');
  if(!root)return;
  const buttons=[...root.querySelectorAll('[data-channel]')];
  const tier=root.querySelector('[data-channel-tier]');
  const title=root.querySelector('[data-channel-title]');
  const copy=root.querySelector('[data-channel-copy]');
  const metric=root.querySelector('[data-channel-metric]');
  const finding=root.querySelector('[data-channel-finding]');
  const link=root.querySelector('[data-channel-link]');
  const states={
    google:['CORE FOUNDATION','Google Ads intelligence with real commerce context.','Malach connects campaign behavior, search demand and spend to verified margin, attribution and contribution—not platform ROAS alone.','+$4,760','High-intent demand remains profitable below the rational CPC ceiling.','/solutions/google-ads/','Explore Google Ads →'],
    shopify:['CORE FOUNDATION','Shopify economics behind every advertising decision.','Orders, product cost, fees, shipping, discounts and returns give Malach the economic truth behind channel performance.','$184,260','Contribution remains healthy after every major commerce cost.','/solutions/shopify/','Explore Shopify Intelligence →'],
    meta:['PORTFOLIO','Meta demand inside the full contribution picture.','Malach Vision shows where prospecting creates assisted value instead of judging Meta only by last-click results.','$96,000','Prospecting is creating measurable assisted Google conversion value.','/vision/','Explore Malach Vision →'],
    tiktok:['PORTFOLIO','TikTok creative signals connected to profit.','Malach helps identify which creative directions retain lift across measured windows and downstream store outcomes.','+$58,000','Sora Carryall creative lift held across three measured windows.','/vision/','Explore Malach Vision →'],
    amazon:['PORTFOLIO · PLANNED','Amazon Ads through the same profit lens.','Amazon Ads is the next planned Portfolio integration and will use the same contribution and authority model as the rest of Malach.','COMING SOON','Planned integration. No active Amazon Ads execution is being claimed today.','/channels/#amazon','Explore Channels →']
  };
  buttons.forEach(btn=>btn.addEventListener('click',()=>{
    const state=states[btn.dataset.channel];
    if(!state)return;
    buttons.forEach(b=>b.classList.toggle('active',b===btn));
    tier.textContent=state[0];title.textContent=state[1];copy.textContent=state[2];metric.textContent=state[3];finding.textContent=state[4];link.href=state[5];link.textContent=state[6];
  }));
}

function setupAuthorityCards(){
  const cards=[...document.querySelectorAll('[data-authority-card]')];
  const status=document.querySelector('[data-authority-status]');
  if(!cards.length)return;
  const messages={
    observe:'Observe mode · No ad-platform execution',
    approval:'Approval mode · Malach prepares, you approve',
    canary:'Canary mode · Controlled test authority',
    full:'Full Auto · Certified actions inside your safeguards'
  };
  cards.forEach(card=>card.addEventListener('click',()=>{
    cards.forEach(c=>c.classList.toggle('active',c===card));
    if(status)status.textContent=messages[card.dataset.authorityCard]||'';
  }));
}


function setupModelLab(){
  const root=document.querySelector('[data-model-lab]');
  if(!root)return;
  const buttons=[...root.querySelectorAll('[data-model-case]')];
  const margin=root.querySelector('[data-model-margin]');
  const confidence=root.querySelector('[data-model-confidence]');
  const cpc=root.querySelector('[data-model-cpc]');
  const market=root.querySelector('[data-model-market]');
  const probability=root.querySelector('[data-model-probability]');
  const probabilityLabel=root.querySelector('[data-model-probability-label]');
  const title=root.querySelector('[data-model-title]');
  const reason=root.querySelector('[data-model-reason]');
  const upside=root.querySelector('[data-model-upside]');
  const states={
    aster:{margin:'$84',confidence:'89%',cpc:'$3.84',market:'+12%',prob:'82.6%',title:'Increase high-intent search 12%.',reason:'Margin buffer, verified attribution and demand strength support a controlled expansion.',upside:'+$4,760'},
    sora:{margin:'$67',confidence:'86%',cpc:'$3.16',market:'+7%',prob:'76.4%',title:'Expand remarketing around repeat demand.',reason:'Stable contribution and repeat-purchase behavior support a measured expansion.',upside:'+$2,940'},
    ember:{margin:'$49',confidence:'81%',cpc:'$2.42',market:'−4%',prob:'58.7%',title:'Hold prospecting and protect margin.',reason:'Return-adjusted contribution weakened while category costs rose. The evidence favors containment.',upside:'+$1,180 protected'}
  };
  const apply=key=>{
    const s=states[key];if(!s)return;
    buttons.forEach(b=>b.classList.toggle('active',b.dataset.modelCase===key));
    if(margin)margin.textContent=s.margin;if(confidence)confidence.textContent=s.confidence;if(cpc)cpc.textContent=s.cpc;if(market)market.textContent=s.market;
    if(probability){probability.style.setProperty('--prob',s.prob);probability.style.width=s.prob;}
    if(probabilityLabel)probabilityLabel.textContent=`${s.prob} likely profitable`;
    if(title)title.textContent=s.title;if(reason)reason.textContent=s.reason;if(upside)upside.textContent=s.upside;
    root.classList.remove('v71-model-flash');void root.offsetWidth;root.classList.add('v71-model-flash');
  };
  buttons.forEach(btn=>btn.addEventListener('click',()=>apply(btn.dataset.modelCase)));
}

function setupOpsClock(){
  document.querySelectorAll('[data-ops-clock]').forEach(root=>{
    const clock=root.querySelector('[data-ops-time]');
    const events=[...root.querySelectorAll('.v71-ops-events article')];
    const renderTime=()=>{
      if(!clock)return;
      const d=new Date();
      clock.textContent=d.toLocaleTimeString([], {hour:'2-digit',minute:'2-digit',second:'2-digit',hour12:false});
    };
    renderTime();
    if(!reduced)setInterval(renderTime,1000);
    if(events.length&&!reduced){
      let index=0;
      setInterval(()=>{
        if(document.hidden)return;
        index=(index+1)%events.length;
        events.forEach((event,i)=>event.classList.toggle('active',i===index));
      },2100);
    }
  });
}

function setupAgentCanvas(){
  document.querySelectorAll('[data-v71-canvas]').forEach(root=>{
    const buttons=[...root.querySelectorAll('[data-canvas-step]')];
    const kicker=root.querySelector('[data-canvas-kicker]');
    const title=root.querySelector('[data-canvas-title]');
    const copy=root.querySelector('[data-canvas-copy]');
    const states={
      signal:['OPPORTUNITY DETECTED','High-intent demand moved above the profit-safe threshold.','Malach is watching the opportunity and collecting the business, attribution and market signals needed to judge it.'],
      evidence:['EVIDENCE ASSEMBLED','The economics support a controlled expansion.','Agent Canvas gathered margin, break-even CPC, attribution confidence, competitor pressure and recent outcomes into one evidence packet.'],
      decision:['DECISION MODELED','Increase high-intent search 12%.','Malach’s proprietary decision models estimate an 82.6% chance of a profitable result with +$4,760 in expected contribution.'],
      action:['WORK PREPARED','The action is ready for the authority you chose.','In Approval, Malach waits for you. In Canary, it runs a controlled test. In Full Auto, eligible work can execute within your safeguards.'],
      outcome:['OUTCOME MEASURED','Measured contribution exceeded the model.','Malach confirmed the change, measured +$4,120 in contribution and preserved the result as evidence for the next decision.']
    };
    buttons.forEach(btn=>btn.addEventListener('click',()=>{
      const state=states[btn.dataset.canvasStep];if(!state)return;
      buttons.forEach(b=>b.classList.toggle('active',b===btn));
      if(kicker)kicker.textContent=state[0];if(title)title.textContent=state[1];if(copy)copy.textContent=state[2];
      root.classList.remove('v71-canvas-flash');void root.offsetWidth;root.classList.add('v71-canvas-flash');
    }));
  });
}

setupHero();
setupAuthoritySwitches();
setupProductSignals();
setupClarity();
setupVision();
setupFlow();
setupChannels();
setupAuthorityCards();
setupModelLab();
setupOpsClock();
setupAgentCanvas();
document.documentElement.dataset.v7HomeReady='true';
