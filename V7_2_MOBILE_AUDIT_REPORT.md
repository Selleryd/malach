# Malach Public Website V7.2 — Mobile Perfection Audit

V7.2 preserves the approved V7.1 desktop experience and adds a purpose-built mobile presentation layer rather than merely collapsing desktop grids.

## Mobile corrections

- Rebuilt the hero for 320–899px widths with contained typography, full-width CTAs and no min-content overflow.
- Reflowed the main command deck from a three-column desktop instrument into a native one-column mobile console.
- Removed reserved scrollbar gutter on phones and added safe-area support for modern iOS devices.
- Rebuilt navigation as a full-height mobile drawer with large touch targets, Solutions/Company accordions, and persistent Sign in / Start trial actions.
- Converted long feature and authority stacks into horizontal, scroll-snap product stories with mobile progress dots.
- Rebuilt Agent Canvas, channel tabs, model tabs and orchestration flow for thumb-friendly horizontal navigation.
- Replaced absolute-positioned desktop system diagrams with responsive native mobile grids.
- Reduced section heights, type scale, micro-label density, padding and heavy desktop effects on small screens.
- Disabled unnecessary perspective/tilt work on coarse pointers.
- Refined pricing, FAQ, forms, Chat, legal, Status and subpages for narrow screens.
- Added dedicated mobile JavaScript for snap indicators, active-tab visibility and drawer behavior.

## Audited widths

Targeted layout audits were performed at 320, 390, 430 and 768 CSS pixels. Core homepage content, command deck and primary sections remain inside the viewport at each target width.

## Desktop boundary

The V7.2 presentation layer is scoped below 900px so the approved V7.1 desktop design remains unchanged.
